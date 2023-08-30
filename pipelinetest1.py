from transformers import pipeline

classifier = pipeline("sentiment-analysis")
ans= ['杨树茂破产', '李岱昆重紫烟熏妆', '建议每周单休月末连休5天', '上海野生动物园多次抽查发现问题', '国考', '全红婵长成大女孩了', '彭冠英王楚然兑现flag', 'Lisa新加坡芭莎封面', '王一博祝福周艺轩陈梦瑶', '这玩偶一天能走两万步', '王茂蕾李一桐演父女', '恋爱中的少典有琴', ]


for i in range(len(ans)):

    res = classifier(ans[i])
#I've been waiting for a HuggingFace course my whole life.

    print(res, i)