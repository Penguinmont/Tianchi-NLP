import re
pattern = r'"topic": "(.*?)"'
# 打开TXT文件
f = open("D:/Program Files (x86)/test_a.txt", "r", encoding="utf-8")
# 读取所有行
lines = f.readlines()
# 关闭文件
f.close()
# 定义一个空列表存储提取的文本
extracted_text = []
# 遍历每一行
for line in lines:
    # 如果行以字母摘要开头
    matches = re.findall(pattern, line)

    # 添加到列表中
    extracted_text.append(matches[0])
# 打印结果
print(extracted_text)