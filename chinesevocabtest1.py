# -*- coding:utf-8 -*-
from transformers import BertTokenizer

# 定义文本

text_list = ['美驻俄大使馆呼吁在俄公民立即撤离', '女子花100万在农村建120平3层房', '《乘风破浪的姐姐》：张雨绮请半熟恋人全组喝奶茶', '京东618全球年中购物节开启：京东百亿补贴已上线测试', '阿尔维斯打破巴西征战世界杯年龄记录', 'NASA计划2024年送宇航员上月球']
# 创建一个BertTokenizer对象
tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')

# 使用BertTokenizer对象将文本列表转换为数字
vocab_numbers_list = [tokenizer.encode(text.strip("'")) for text in text_list]

# 将二维数字列表转换为一维数字列表
# vocab_numbers_list_flat = [number for sublist in vocab_numbers_list for number in sublist]


print(vocab_numbers_list)
'''filename = 'testoutput_vocab.txt'
outfile = open(filename, 'w', encoding="utf-8")
outfile.writelines([str(i)+',' for i in vocab_numbers_list])
outfile.close()'''

# 打印结果
# print(vocab_numbers_list_flat)

