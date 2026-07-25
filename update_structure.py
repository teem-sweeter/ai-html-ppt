import re

with open('public/workspaces/deep-learning/cv-learning-path/presentation.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 更新 slide-content 结构
# 匹配模式：slide-content 开始标签后，section-tag 和 h2
lines = content.split('\n')
new_lines = []
in_slide_content = False
slide_content_indent = ''
header_added = False

i = 0
while i < len(lines):
    line = lines[i]
    
    # 检测 slide-content 开始
    if 'class="slide slide-content"' in line and 'data-index=' in line:
        in_slide_content = True
        header_added = False
        new_lines.append(line)
        i += 1
        continue
    
    # 在 slide-content 内
    if in_slide_content:
        # 检测 section-tag
        if '<div class="section-tag"' in line and not header_added:
            # 添加 slide-header 开始
            indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(f'{indent}<div class="slide-header">')
            new_lines.append(line)
            
            # 查找 h2
            j = i + 1
            while j < len(lines) and '<h2>' not in lines[j]:
                j += 1
            
            # 添加 h2
            if j < len(lines):
                new_lines.extend(lines[i+1:j+1])
                # 添加 slide-header 结束
                new_lines.append(f'{indent}</div>')
                # 添加 slide-body 开始
                new_lines.append(f'{indent}<div class="slide-body">')
                header_added = True
                i = j + 1
                continue
        
        # 检测 slide-content 结束
        if '</div>' in line and in_slide_content and header_added:
            # 检查是否是 slide-content 的结束
            # 简单判断：如果缩进级别回到 slide-content 的级别
            indent = line[:len(line) - len(line.lstrip())]
            if len(indent) <= 2:  # 假设 slide-content 的缩进是2个空格
                # 添加 slide-body 结束
                new_lines.append(f'{indent}  </div>')
                new_lines.append(line)
                in_slide_content = False
                i += 1
                continue
    
    new_lines.append(line)
    i += 1

new_content = '\n'.join(new_lines)

with open('public/workspaces/deep-learning/cv-learning-path/presentation.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated all slide headers')