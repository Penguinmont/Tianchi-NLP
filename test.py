import pandas as pd
data = pd.read_csv("data/test_a.csv", header=0, usecols=[1], sep="\t")
with open('data/test_a.csv', encoding="utf-8") as f_handle:
    train_df = pd.read_csv(f_handle,  sep='\t')
print(train_df.columns)
print(train_df.index.names)
train_df['text_len'] = train_df['text'].apply(lambda x: len(x.split(' ')))
print(train_df['text_len'].describe())
