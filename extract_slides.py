#!/usr/bin/env python3
"""
从原始 HTML 文件中提取幻灯片内容
"""

import re
import os
from pathlib import Path

def extract_slides(html_file, output_dir, prefix='slide'):
    """从 HTML 文件中提取幻灯片"""
    
    # 读取 HTML 文件
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取 CSS 样式（在 <style> 标签中）
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    css_content = style_match.group(1) if style_match else ''
    
    # 提取所有 slide div
    # 匹配 <div class="slide ...">...</div>
    slide_pattern = r'<div class="slide[^"]*"[^>]*>(.*?)</div>\s*(?=<div class="slide|</div>\s*<!-- Navigation)'
    
    slides = re.findall(slide_pattern, content, re.DOTALL)
    
    # 如果没有找到，尝试更宽松的匹配
    if not slides:
        # 找到所有 slide 的开始位置
        slide_starts = [m.start() for m in re.finditer(r'<div class="slide[^"]*"[^>]*>', content)]
        
        for i, start in enumerate(slide_starts):
            # 找到下一个 slide 的开始或文档结束
            if i + 1 < len(slide_starts):
                end = slide_starts[i + 1]
            else:
                end = len(content)
            
            slide_html = content[start:end]
            # 提取完整的 div
            div_match = re.search(r'(<div class="slide[^"]*"[^>]*>.*?</div>)', slide_html, re.DOTALL)
            if div_match:
                slides.append(div_match.group(1))
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 提取 CSS 变量和通用样式
    common_css = extract_common_css(css_content)
    
    # 为每个 slide 创建文件
    for i, slide_html in enumerate(slides):
        # 提取这个 slide 特定的 CSS
        slide_css = extract_slide_css(css_content, slide_html)
        
        # 创建完整的 HTML 内容
        full_html = f"""{slide_html}

<style>
{common_css}
{slide_css}
</style>"""
        
        # 写入文件
        output_file = os.path.join(output_dir, f'{prefix}{i}.html')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        print(f'Created: {output_file}')
    
    return len(slides)

def extract_common_css(css_content):
    """提取通用的 CSS 样式"""
    common_patterns = [
        r':root\s*\{[^}]*\}',
        r'\*\s*\{[^}]*\}',
        r'body\s*\{[^}]*\}',
        r'@keyframes\s+\w+\s*\{[^}]*(?:\{[^}]*\}[^}]*)*\}',
    ]
    
    common_css = []
    for pattern in common_patterns:
        matches = re.findall(pattern, css_content, re.DOTALL)
        common_css.extend(matches)
    
    return '\n'.join(common_css)

def extract_slide_css(css_content, slide_html):
    """提取特定 slide 需要的 CSS 样式"""
    # 从 slide HTML 中提取使用的类名
    class_pattern = r'class="([^"]*)"'
    classes = set()
    for match in re.finditer(class_pattern, slide_html):
        for cls in match.group(1).split():
            classes.add(cls)
    
    # 提取这些类的 CSS 规则
    css_rules = []
    for cls in classes:
        # 匹配 .className { ... }
        pattern = rf'\.{re.escape(cls)}\s*\{{[^}}]*\}}'
        matches = re.findall(pattern, css_content)
        css_rules.extend(matches)
        
        # 匹配 .parent .className { ... }
        parent_pattern = rf'[^}}]*\.{re.escape(cls)}\s*\{{[^}}]*\}}'
        matches = re.findall(parent_pattern, css_content)
        css_rules.extend(matches)
    
    return '\n'.join(css_rules)

def main():
    """主函数"""
    base_dir = Path(__file__).parent
    
    # 池化 PPT
    pooling_html = base_dir.parent / '池化PPT.html'
    if pooling_html.exists():
        print(f'Processing: {pooling_html}')
        count = extract_slides(
            pooling_html,
            base_dir / 'workspaces' / 'deep-learning' / 'pooling',
            'slide'
        )
        print(f'Extracted {count} slides for pooling')
    
    # 激活函数 PPT
    activation_html = base_dir.parent / '激活函数.html'
    if activation_html.exists():
        print(f'Processing: {activation_html}')
        count = extract_slides(
            activation_html,
            base_dir / 'workspaces' / 'deep-learning' / 'activation',
            'slide'
        )
        print(f'Extracted {count} slides for activation')
    
    # ResNet PPT
    resnet_html = base_dir.parent / 'ResNet.html'
    if resnet_html.exists():
        print(f'Processing: {resnet_html}')
        count = extract_slides(
            resnet_html,
            base_dir / 'workspaces' / 'deep-learning' / 'resnet',
            'slide'
        )
        print(f'Extracted {count} slides for resnet')

if __name__ == '__main__':
    main()