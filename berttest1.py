# -*- coding: utf-8 -*-
from transformers import BertTokenizer
# 加载中文BERT模型的分词器
tokenizer = BertTokenizer.from_pretrained("bert-base-chinese")
# 定义一个原始文本
text = "孃子孑孔孕孖字存孙孚孛孜孝孟孢季孤学孩孪孫孬孰孱孳孵學孺孽孿宁它宅宇守安宋完宏宓宕宗官宙定宛宜宝实実宠审客宣室宥宦宪宫宮宰害宴宵家宸容宽宾宿寂寄寅密寇富寐寒寓寛寝寞察寡寢寥實寧寨審寫寬寮寰寵寶寸对寺寻导対寿封専射将將專尉尊尋對導小少尔尕尖尘尚尝尤尧尬就尴尷尸尹尺尻尼尽尾尿局屁层屄居屆屈屉届屋屌屍屎屏屐屑展屜属屠屡屢層履屬屯山屹屿岀岁岂岌岐岑岔岖岗岘岙岚岛岡岩岫岬岭岱岳岷岸峇峋峒峙峡峤峥峦峨峪峭峯峰峴島峻峽崁崂崆崇崎崑崔崖崗崙崛崧崩崭崴崽嵇嵊嵋嵌嵐嵘嵩嵬嵯嶂嶄嶇嶋嶙嶺嶼嶽巅巍巒巔巖川州巡巢工左巧巨巩巫差己已巳巴巷巻巽巾巿币市布帅帆师希帐帑帕帖帘帚帛帜帝帥带帧師席帮帯帰帳帶帷常帼帽幀幂幄幅幌幔幕幟幡幢幣幫干平年并"
# 使用分词器将原始文本转换为词编号序列
input_ids = tokenizer.encode(text, add_special_tokens=True)
# 打印结果
print(input_ids)