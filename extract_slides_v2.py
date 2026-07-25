#!/usr/bin/env python3
"""
从原始 HTML 文件中提取幻灯片内容（改进版）
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
    
    # 使用更精确的方法提取 slide
    slides = []
    
    # 找到所有 slide 的开始和结束位置
    slide_starts = []
    for match in re.finditer(r'<div class="slide[^"]*"[^>]*>', content):
        slide_starts.append(match.start())
    
    # 为每个 slide 提取完整内容
    for i, start in enumerate(slide_starts):
        # 找到这个 slide 的结束位置
        if i + 1 < len(slide_starts):
            end = slide_starts[i + 1]
        else:
            # 最后一个 slide，找到 </div>\s*<!-- Navigation 或文档结束
            nav_match = re.search(r'</div>\s*<!-- Navigation', content[start:])
            if nav_match:
                end = start + nav_match.start() + len('</div>')
            else:
                end = len(content)
        
        slide_html = content[start:end]
        
        # 清理：只保留完整的 div 结构
        # 计算 div 的嵌套层级
        div_count = 0
        clean_end = 0
        for j, char in enumerate(slide_html):
            if char == '<':
                # 检查是否是 div 开始或结束标签
                if slide_html[j:j+4] == '<div':
                    div_count += 1
                elif slide_html[j:j+6] == '</div>':
                    div_count -= 1
                    if div_count == 0:
                        clean_end = j + 6
                        break
        
        if clean_end > 0:
            slide_html = slide_html[:clean_end]
        
        slides.append(slide_html)
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 为每个 slide 创建文件
    for i, slide_html in enumerate(slides):
        # 创建完整的 HTML 内容
        full_html = f"""<div class="slide-container">
{slide_html}
</div>

<style>
/* 通用样式 */
:root {{
  --bg: #0a0a0f;
  --surface: #12121a;
  --surface-2: #1a1a26;
  --accent: #00e5ff;
  --accent-2: #7c4dff;
  --accent-3: #ff6d00;
  --text-primary: #eef0f6;
  --text-muted: #6b6d7b;
  --green: #00e676;
  --grid-cell: #1e1e2e;
  --grid-border: #2a2a3d;
  --highlight: #ffab00;
  --danger: #ff6b6b;
  --yellow: #ffab00;
  --orange: #ff8c42;
  --purple: #a855f7;
}}

* {{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}}

.slide-container {{
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 60px 80px;
  position: relative;
  overflow: hidden;
  background: var(--bg);
  color: var(--text-primary);
  font-family: 'Noto Sans SC', 'Inter', sans-serif;
}}
</style>"""
        
        # 写入文件
        output_file = os.path.join(output_dir, f'{prefix}{i}.html')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        print(f'Created: {output_file}')
    
    return len(slides)

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