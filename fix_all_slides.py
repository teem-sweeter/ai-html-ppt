import re

with open('public/workspaces/deep-learning/cv-learning-path/presentation.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到所有 slide-content 块
pattern = r'(<div class="slide slide-content" data-index="\d+">)(.*?)(</div>\s*\n\s*<!-- SLIDE|\s*<!-- SLIDE|\s*<div class="slide slide-title")'

def fix_slide(match):
    slide_start = match.group(1)
    slide_content = match.group(2)
    slide_end = match.group(3)
    
    # 修复 slide-header 和 slide-body 结构
    # 删除 slide-header 后面的多余 </div>
    slide_content = re.sub(
        r'(<div class="slide-header">\s*\n\s*<div class="section-tag"[^>]*>.*?</div>\s*\n\s*<h2>.*?</h2>\s*\n\s*)</div>\s*\n\s*(<div class="slide-body">)',
        r'\1</div>\n\2',
        slide_content,
        flags=re.DOTALL
    )
    
    return slide_start + slide_content + slide_end

new_content = re.sub(pattern, fix_slide, content, flags=re.DOTALL)

with open('public/workspaces/deep-learning/cv-learning-path/presentation.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Fixed all slide structures')