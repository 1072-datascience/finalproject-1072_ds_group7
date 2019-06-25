import pandas as pd
filepath = 'train.tsv'
df = pd.read_csv(filepath, sep='\t')
sentences = df['Sentence']
target = df['RE_Type']

sentences.head()

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df = 1)
vectorizer.fit(sentences)
vectorizer.vocabulary_

voc_dic=vectorizer.vocabulary_
len(voc_dic) #共有16150個unique 
vectorizer.transform(sentences).toarray()

sentences = df['Sentence']
target = df['RE_Type']
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
sentences_train, sentences_test, y_train, y_test = train_test_split(sentences, target,
test_size=0.25, random_state=1000) #將data根據 1:3切成 test 和 train
vectorizer = CountVectorizer()
vectorizer.fit(sentences_train)
# train 和 test 分別做出feature vector (BOW)
X_train = vectorizer.transform(sentences_train)
X_test = vectorizer.transform(sentences_test)
classifier = LogisticRegression() #初始化 LR model
classifier.fit(X_train, y_train) # 訓練 LR model
score = classifier.score(X_test, y_test) #評估 LR model

score
