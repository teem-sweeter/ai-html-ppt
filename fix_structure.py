import re

with open('public/workspaces/deep-learning/cv-learning-path/presentation.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 修复 slide-header 和 slide-body 的缩进
# 匹配模式：slide-header 和 slide-body 内的内容需要正确的缩进

lines = content.split('\n')
new_lines = []
in_slide_content = False
slide_indent = ''

i = 0
while i < len(lines):
    line = lines[i]
    
    # 检测 slide-content 开始
    if 'class="slide slide-content"' in line and 'data-index=' in line:
        in_slide_content = True
        slide_indent = line[:len(line) - len(line.lstrip())]
        new_lines.append(line)
        i += 1
        continue
    
    # 在 slide-content 内
    if in_slide_content:
        # 修复 slide-header
        if '<div class="slide-header">' in line:
            indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(f'{indent}<div class="slide-header">')
            i += 1
            
            # 处理 section-tag
            if i < len(lines) and '<div class="section-tag"' in lines[i]:
                new_lines.append(f'{indent}  {lines[i].strip()}')
                i += 1
            
            # 处理 h2
            if i < len(lines) and '<h2>' in lines[i]:
                new_lines.append(f'{indent}  {lines[i].strip()}')
                i += 1
            
            # 闭合 slide-header
            new_lines.append(f'{indent}</div>')
            continue
        
        # 修复 slide-body
        if '<div class="slide-body">' in line:
            indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(f'{indent}<div class="slide-body">')
            i += 1
            
            # 处理内容
            content_indent = f'{indent}  '
            while i < len(lines) and '</div>' not in lines[i]:
                new_lines.append(f'{content_indent}{lines[i].strip()}')
                i += 1
            
            # 闭合 slide-body
            if i < len(lines):
                new_lines.append(f'{indent}</div>')
                i += 1
            continue
        
        # 检测 slide-content 结束
        if '</div>' in line and in_slide_content:
            indent = line[:len(line) - len(line.lstrip())]
            if len(indent) <= len(slide_indent):
                in_slide_content = False
    
    new_lines.append(line)
    i += 1

new_content = '\n'.join(new_lines)

with open('public/workspaces/deep-learning/cv-learning-path/presentation.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Fixed all slide structures')