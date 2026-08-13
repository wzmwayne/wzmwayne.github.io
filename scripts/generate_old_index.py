import json
import os


def extract_categories(js_content):
    """从 data/links.js 中提取 categories 字典（JS 对象 -> JSON）"""
    brace_start = js_content.find('{')
    if brace_start == -1:
        raise ValueError("未找到 categories 对象的起始花括号")

    depth = 0
    for i in range(brace_start, len(js_content)):
        if js_content[i] == '{':
            depth += 1
        elif js_content[i] == '}':
            depth -= 1
            if depth == 0:
                json_text = js_content[brace_start:i + 1]
                return json.loads(json_text)

    raise ValueError("未找到 categories 对象的匹配闭合花括号")


def extract_array(js_content, marker):
    """从 JS 文件中提取数组（如 var announcements = [...] -> list）"""
    idx = js_content.find(marker)
    if idx == -1:
        raise ValueError(f"未找到 {marker}")

    bracket = js_content.find('[', idx)
    if bracket == -1:
        raise ValueError(f"未找到 {marker} 数组的起始括号")

    depth = 0
    for i in range(bracket, len(js_content)):
        if js_content[i] == '[':
            depth += 1
        elif js_content[i] == ']':
            depth -= 1
            if depth == 0:
                return json.loads(js_content[bracket:i + 1])

    raise ValueError(f"未找到 {marker} 数组的匹配闭合括号")


def escape(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def render_group(lines, group, depth):
    """递归渲染一组链接。忽略 setting（折叠规则）；嵌套分组通过嵌套 <ul> 实现缩进。"""
    for key, value in group.items():
        if key == 'setting':
            continue
        pad = '    ' * (depth + 1)
        if isinstance(value, dict):
            lines.append(f'{pad}<li>{escape(key)}')
            lines.append(f'{pad}    <ul>')
            render_group(lines, value, depth + 1)
            lines.append(f'{pad}    </ul>')
            lines.append(f'{pad}</li>')
        elif isinstance(value, str) and value.startswith('[text]'):
            lines.append(f'{pad}<li>{escape(value[6:])}</li>')
        else:
            lines.append(f'{pad}<li><a href="{escape(value)}">{escape(key)}</a></li>')


def generate_html(categories, announcements):
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
        if category_name == 'setting':
            continue
        lines.append(f'    <h2>{escape(category_name)}</h2>')
        lines.append('    <ul>')
        render_group(lines, links, 0)
        lines.append('    </ul>')

    lines.append('')
    lines.append('    <h2>公告</h2>')
    if announcements:
        for a in announcements:
            parts = []
            if a.get('date'):
                parts.append(str(a['date']))
            if a.get('title'):
                parts.append(str(a['title']))
            head = ' '.join(parts)
            content = a.get('content')
            if content:
                lines.append(f'    <p>{escape(head)}：{escape(str(content))}</p>')
            elif head:
                lines.append(f'    <p>{escape(head)}</p>')
    else:
        lines.append('    <p>暂无公告</p>')

    lines.append('</body>')
    lines.append('</html>')
    return '\n'.join(lines) + '\n'


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)

    links_path = os.path.join(repo_root, 'data', 'links.js')
    announcements_path = os.path.join(repo_root, 'data', 'announcements.js')
    old_dir = os.path.join(repo_root, 'old')
    old_index_path = os.path.join(old_dir, 'index.html')

    with open(links_path, 'r', encoding='utf-8') as f:
        js_content = f.read()
    with open(announcements_path, 'r', encoding='utf-8') as f:
        announcements_content = f.read()

    categories = extract_categories(js_content)
    announcements = extract_array(announcements_content, 'var announcements =')
    output = generate_html(categories, announcements)

    # 旧版页面必须为纯静态 HTML：无计算逻辑、无加载逻辑、无样式
    forbidden = ['<script', '<style', 'style=', 'onclick', 'onload', 'onerror', '<link', '<img', '<iframe']
    lowered = output.lower()
    for token in forbidden:
        if token in lowered:
            raise ValueError(f'旧版页面禁止出现 {token}')

    os.makedirs(old_dir, exist_ok=True)
    with open(old_index_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f'Generated {old_index_path}')


if __name__ == '__main__':
    main()
