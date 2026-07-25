#!/usr/bin/env python3
"""
PPT HTML 生成器
用法: python create_ppt.py <workspace> <ppt-id> <title>
示例: python create_ppt.py deep-learning transformers "Transformer架构"
"""

import sys
import os
import json
from pathlib import Path

def create_ppt(workspace, ppt_id, title):
    base_dir = Path(__file__).parent
    template_file = base_dir / 'templates' / 'ppt-template.html'
    output_dir = base_dir / 'public' / 'workspaces' / workspace / ppt_id
    
    # 检查模板是否存在
    if not template_file.exists():
        print(f'错误: 模板文件不存在 {template_file}')
        return False
    
    # 创建输出目录
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 读取模板
    with open(template_file, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # 替换变量
    html = template.replace('{{TITLE}}', title)
    html = html.replace('{{TAG}}', f'Deep Learning · {ppt_id.replace("-", " ").title()}')
    html = html.replace('{{MAIN_TITLE}}', title)
    html = html.replace('{{SUBTITLE}}', f'{title}详解')
    
    # 写入文件
    output_file = output_dir / 'presentation.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f'已创建: {output_file}')
    
    # 更新 index.json
    update_index(base_dir, workspace, ppt_id, title)
    
    return True

def update_index(base_dir, workspace, ppt_id, title):
    index_file = base_dir / 'public' / 'workspaces' / 'index.json'
    
    # 读取现有索引
    if index_file.exists():
        with open(index_file, 'r', encoding='utf-8') as f:
            workspaces = json.load(f)
    else:
        workspaces = []
    
    # 查找工作空间
    ws = next((w for w in workspaces if w['id'] == workspace), None)
    if not ws:
        ws = {
            'id': workspace,
            'name': workspace.replace('-', ' ').title(),
            'description': '',
            'presentations': []
        }
        workspaces.append(ws)
    
    # 检查PPT是否已存在
    pres = next((p for p in ws['presentations'] if p['id'] == ppt_id), None)
    if not pres:
        pres = {
            'id': ppt_id,
            'title': title,
            'description': '',
            'file': 'presentation.html',
            'totalSlides': 4
        }
        ws['presentations'].append(pres)
    
    # 写入索引
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(workspaces, f, ensure_ascii=False, indent=2)
    
    print(f'已更新: {index_file}')

def main():
    if len(sys.argv) < 4:
        print('用法: python create_ppt.py <workspace> <ppt-id> <title>')
        print('示例: python create_ppt.py deep-learning transformers "Transformer架构"')
        sys.exit(1)
    
    workspace = sys.argv[1]
    ppt_id = sys.argv[2]
    title = sys.argv[3]
    
    create_ppt(workspace, ppt_id, title)

if __name__ == '__main__':
    main()