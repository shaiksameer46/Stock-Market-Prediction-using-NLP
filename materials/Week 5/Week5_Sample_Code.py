# %%
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# %%
sentence = ['to be or not to be that is the question']
vectorizer_2g = CountVectorizer(ngram_range=(1, 2))
sample = vectorizer_2g.fit_transform(sentence)
print(sample.shape)

# %%
train = ['to be or not to be that is the question',
         'i love logistic regression']
label = np.array([0, 1]).reshape(-1, 1)
train = vectorizer_2g.fit_transform(train)
test = vectorizer_2g.transform(['this is a test sentence'])
lr = LogisticRegression()
lr = lr.fit(train, label)
prediction = lr.predict(test)
