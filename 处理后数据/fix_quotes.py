with open('专题2-题库.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()

result = []
for line in lines:
    if '"解析":' in line:
        idx = line.find('"解析": "')
        if idx != -1:
            # 找到最后一个"的位置（这是JSON的结束引号）
            last_quote = line.rfind('"')
            if last_quote > idx + 8:
                prefix = line[:idx + 8]
                middle = line[idx + 8:last_quote]
                suffix = line[last_quote:]
                # 只替换middle部分的中文引号
                middle = middle.replace('"', '：').replace('"', '，')
                line = prefix + middle + suffix
    result.append(line)

with open('专题2-题库.json', 'w', encoding='utf-8') as f:
    f.writelines(result)

print('修复完成')
