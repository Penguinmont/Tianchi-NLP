# -*- coding:utf-8 -*-
import re
import json
with open('output_vocab.txt', 'r') as file:
    data = json.loads(file.read())
    print(data)

with open('class_output.txt', 'r', encoding='UTF-8') as file:
    text = json.loads(file.read().replace("'", '"'))
    print(text)
print(len(data))
print(len(text))
