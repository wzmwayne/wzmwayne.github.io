import json
import os


def extract_categories(html_content):
    """从 index.html 中提取 categories 字典（JS 对象 -> JSON）"""
    start_marker = 'const categories = '
    start_idx = html_content.find(start_marker)
    if start_idx == -1:
        raise ValueError("未在 index.html 中找到 const categories =")

    brace_start = html_content.find('{', start_idx)
    if brace_start == -1:
        raise ValueError("未找到 categories 对象的起始花括号")

    depth = 0
    for i in range(brace_start, len(html_content)):
        if html_content[i] == '{':
            depth += 1
        elif html_content[i] == '}':
            depth -= 1
            if depth == 0:
                json_text = html_content[brace_start:i + 1]
                return json.loads(json_text)

    raise ValueError("未找到 categories 对象的匹配闭合花括号")


def escape(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def generate_html(categories):
    lines = [
        '<!DOCTYPE html>',
        '<html lang="zh-CN">',
        '<head>',
        '    <meta charset="UTF-8">',

        '    <title>玩坏电脑的小站 - 导航（旧版）</title>',
        '</head>',
        '<body>',
        '    <h1>玩坏电脑的小站</h1>',
    ]

    for category_name, links in categories.items():
        lines.append(f'    <h2>{escape(category_name)}</h2>')
        lines.append('    <ul>')
        for link_name, url in links.items():
            lines.append(f'        <li><a href="{escape(url)}">{escape(link_name)}</a></li>')
        lines.append('    </ul>')

    lines.append('</body>')
    lines.append('</html>')
    return '\n'.join(lines) + '\n'


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)

    index_path = os.path.join(repo_root, 'index.html')
    old_dir = os.path.join(repo_root, 'old')
    old_index_path = os.path.join(old_dir, 'index.html')

    with open(index_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    categories = extract_categories(html_content)
    output = generate_html(categories)

    os.makedirs(old_dir, exist_ok=True)
    with open(old_index_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f'Generated {old_index_path}')


if __name__ == '__main__':
    main()
