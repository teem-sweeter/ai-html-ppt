#!/usr/bin/env python3
"""扫描 public/workspaces 目录，自动生成配置文件"""

import json, os
from pathlib import Path

def scan_workspaces(public_dir):
    workspaces_dir = public_dir / 'workspaces'
    if not workspaces_dir.exists():
        print('No workspaces directory found')
        return

    workspaces = []

    for ws_dir in sorted(workspaces_dir.iterdir()):
        if not ws_dir.is_dir():
            continue

        ws_id = ws_dir.name
        presentations = []

        for pres_dir in sorted(ws_dir.iterdir()):
            if not pres_dir.is_dir():
                continue

            # 检查是否有 presentation.html
            if (pres_dir / 'presentation.html').exists():
                presentations.append({
                    'id': pres_dir.name,
                    'title': pres_dir.name.replace('-', ' ').title(),
                    'description': '',
                    'file': 'presentation.html',
                    'totalSlides': 8  # 默认值，可以手动调整
                })

        if presentations:
            workspace = {
                'id': ws_id,
                'name': ws_id.replace('-', ' ').title(),
                'description': '',
                'presentations': presentations
            }
            workspaces.append(workspace)

            # 写入工作空间配置
            ws_config = ws_dir / 'workspace.json'
            with open(ws_config, 'w', encoding='utf-8') as f:
                json.dump(workspace, f, ensure_ascii=False, indent=2)
            print(f'Created: {ws_config}')

    # 写入索引文件
    index_file = workspaces_dir / 'index.json'
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(workspaces, f, ensure_ascii=False, indent=2)
    print(f'Created: {index_file}')

if __name__ == '__main__':
    base_dir = Path(__file__).parent / 'public'
    scan_workspaces(base_dir)