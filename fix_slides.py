import re

with open('public/workspaces/deep-learning/cv-learning-path/presentation.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 使用正则表达式修复所有slide的结构
# 匹配模式：slide-header后面的多余</div>

# 修复 slide-header 后面的多余 </div>
content = re.sub(
    r'(<div class="slide-header">\s*\n\s*<div class="section-tag"[^>]*>.*?</div>\s*\n\s*<h2>.*?</h2>\s*\n\s*)</div>\s*\n\s*(<div class="slide-body">)',
    r'\1</div>\n\2',
    content,
    flags=re.DOTALL
)

with open('public/workspaces/deep-learning/cv-learning-path/presentation.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed slide structure issues')