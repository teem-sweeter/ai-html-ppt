import re

with open('public/workspaces/deep-learning/cv-learning-path/presentation.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 统计总页数
total_slides = len(re.findall(r'data-index="\d+"', content))

# 为每个 slide-content 添加页眉
def add_header(match):
    full_match = match.group(0)
    slide_start = match.group(1)
    index_match = re.search(r'data-index="(\d+)"', full_match)
    
    if index_match:
        index = int(index_match.group(1))
        # 标题页（index=0）不添加页眉
        if index == 0:
            return full_match
        
        # 添加页眉
        header = f'''
    <div class="slide-header">
      <span class="header-title">计算机视觉学习路线</span>
      <span class="header-page">{index} / {total_slides - 1}</span>
    </div>'''
        
        # 在 slide-content 开始标签后插入页眉
        return slide_start + header + full_match[len(slide_start):]
    
    return full_match

# 匹配 slide-content 开始标签
pattern = r'(<div class="slide slide-content" data-index="\d+">)'
new_content = re.sub(pattern, add_header, content)

with open('public/workspaces/deep-learning/cv-learning-path/presentation.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'Added headers to {total_slides - 1} slides')