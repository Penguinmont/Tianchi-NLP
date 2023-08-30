# -*- coding:utf-8 -*-
import pandas as pd
import json
with open('testoutput_vocab.txt', 'r') as file:
    lst = json.loads(file.read())

s = max(lst, key=len)
r = len(s)
print(s)
print(r)

lst = [str(sub[1:-1]).strip("[]").replace(",", "") for sub in lst] # 对每个元素进行处理
df = pd.DataFrame(lst) # 转换为数据框对象
df.to_csv('test_list.csv', index=False, header=False, encoding='GBK') # 保存为CSV文件


'''with open('class_output.txt', 'r', encoding='UTF-8') as file:
    text = json.loads(file.read().replace("'", '"'))'''



'''lst = [text[i] + '\t' +str(sub[1:-1]).strip("[]").replace(",", "") for i, sub in enumerate(lst)] # 对每个元素进行处理
df = pd.DataFrame(lst) # 转换为数据框对象
df.to_csv('list.csv', index=False, header=False, encoding='GBK') # 保存为CSV文件'''


'''i = 0
res = []
while i < len(lst):
    if lst[i] and text[i]:
        i += 1

    else:
        res.append(i)
        print(i)
        i += 1

print(res)
print(i)
if lst[i]:
    print(lst[i])
else:
    print(text[i])'''


s = max(lst, key=len)
r = len(s)
print(s)
print(r)



