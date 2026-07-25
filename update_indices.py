import re

with open('public/workspaces/deep-learning/cv-learning-path/presentation.html', 'r', encoding='utf-8') as f:
    content = f.read()

counter = 0

def replace_index(match):
    global counter
    result = f'data-index="{counter}"'
    counter += 1
    return result

new_content = re.sub(r'data-index="\d+"', replace_index, content)

with open('public/workspaces/deep-learning/cv-learning-path/presentation.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'Updated {counter} slide indices')