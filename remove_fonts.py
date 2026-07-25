#!/usr/bin/env python3
"""移除HTML中的Google Fonts引用，并替换为系统字体"""

import re
from pathlib import Path

def process_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 移除 preconnect 链接
    content = re.sub(r'<link rel="preconnect"[^>]*fonts\.gstatic\.com[^>]*>\s*', '', content)
    content = re.sub(r'<link rel="preconnect"[^>]*fonts\.googleapis\.com[^>]*>\s*', '', content)
    
    # 移除 Google Fonts 样式表
    content = re.sub(r'<link href="https://fonts\.googleapis\.com[^>]*>\s*', '', content)
    
    # 替换字体为系统字体
    # 'Noto Sans SC' -> system-ui
    content = content.replace("'Noto Sans SC'", "system-ui")
    
    # 'JetBrains Mono' -> 'Cascadia Code', 'Fira Code', Consolas, monospace
    content = content.replace("'JetBrains Mono'", "'Cascadia Code', 'Fira Code', Consolas, monospace")
    content = content.replace("JetBrains Mono", "'Cascadia Code', 'Fira Code', Consolas, monospace")
    
    # 'Instrument Serif' -> Georgia, 'Times New Roman', serif
    content = content.replace("'Instrument Serif'", "Georgia, 'Times New Roman', serif")
    
    # 'Inter' -> system-ui
    content = content.replace("'Inter'", "system-ui")
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Updated: {html_file}')

def main():
    base_dir = Path(__file__).parent / 'public' / 'workspaces'
    
    for html_file in base_dir.rglob('presentation.html'):
        process_html(html_file)

if __name__ == '__main__':
    main()