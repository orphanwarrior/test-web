import json
import re

# 读取原始文件内容
with open('专题1-题库.json', 'r', encoding='utf-8') as f:
    content = f.read()

# 使用正则表达式匹配"解析"字段的值部分
def fix_analysis_field(match):
    prefix = match.group(1)  # "解析": "
    analysis_content = match.group(2)  # 解析内容
    suffix = match.group(3)  # "

    # 在解析内容中进行替换
    # 1. 将英文双引号替换为中文冒号
    fixed_content = analysis_content.replace('"', '：')
    # 2. 将英文逗号后紧跟中文冒号改为中文逗号
    fixed_content = re.sub(r',\s*：', '，', fixed_content)

    return prefix + fixed_content + suffix

# 匹配模式：捕获"解析": "内容"
pattern = r'("解析":\s*")([^"\\]*(?:\\.[^"\\]*)*?)(")'
content = re.sub(pattern, fix_analysis_field, content)

# 写回文件
with open('专题1-题库.json', 'w', encoding='utf-8') as f:
    f.write(content)

# 验证JSON格式
try:
    with open('专题1-题库.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f'修复成功！共有 {len(data["题目"])} 道题目')
except json.JSONDecodeError as e:
    print(f'JSON格式错误: {e}')
