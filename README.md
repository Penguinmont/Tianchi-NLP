This code uses Bert to pre-train news data. For detailed code explanations, code to fine-tune BERT mainly forked from [Tianchi-NLP-Beginner](https://github.com/zhangxiann/Tianchi-NLP-Beginner)





The tensorflow version is 1.x.



The steps are as follows:


# 1. Data preparation

1.1 First, create `data` folder in `bert` folder, and put the training data `train_set.csv` and test data `test_a.csv` into `bert/data` folder. Run `prepare_data.py` and put the text data into a file, separating each article with a blank line
``
python prepare_data.py
```

1.2 Run `create_vocab.py`, to create a dictionary.
```
python create_vocab.py
```

# 2. MASK the data
```
bash create_pretraining_data.sh
```

# 3. Start training Bert
```
bash run_pretraining.sh
```

# 4. Convert Tensorflow models to PyTorch models.
Bert ``` bash convert_checkpoint.sh ``` # 4.
bash convert_checkpoint.sh
```

# 5. Fine-tuning the Bert model for text categorization
```
python finetune_bert.py
```
