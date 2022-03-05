# Week 5 N-gram Model and Machine Learning Models

## Reference

- [n-gram - Wikipedia](https://en.wikipedia.org/wiki/N-gram)
- [sklearn.linear_model.LogisticRegression — scikit-learn 1.0.2 documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html?highlight=logistic#sklearn.linear_model.LogisticRegression)
- [sklearn.svm.LinearSVC — scikit-learn 1.0.2 documentation](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html?highlight=svm#sklearn.svm.LinearSVC)
- [sklearn.ensemble.RandomForestClassifier — scikit-learn 1.0.2 documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html?highlight=random#sklearn.ensemble.RandomForestClassifier)

## N-gram Model

### Example

- Original Sentence: ... to be or not to be ...
- 1-gram Sequence: ..., to, be, or, not, to, be, ...
- 2-gram Sequence: ..., to be, be or, or not, not to, to be, ...
- 3-gram Sequence: ..., to be or, be or not, or not to, not to be, ...

### Python Implementation

```Python
from sklearn.feature_extraction.text import CountVectorizer

sentence = ['to be or not to be that is the question']
vectorizer_2g = CountVectorizer(ngram_range=(1, 2))
sample = vectorizer_2g.fit_transform(sentence)
print(sample.shape)
## (1, 16)
```

From the above example, we can see that the CountVectorizer function helps us create a container with shape (1, 16). The second number is exactly the number of unique words / word pairs in the sentence.

### Major Problem

What to do with stop words?


## Machine Learning Models

### Common Models

- Logistic Regression
- Support Vector Machine
- Random Forest

### Python Implementation

```Python
import numpy as np
from sklearn.linear_model import LogisticRegression

train = ['to be or not to be that is the question',
         'i love logistic regression']
label = np.array([0, 1]).reshape(-1, 1)
train = vectorizer_2g.fit_transform(train)
test = vectorizer_2g.transform(['this is a test sentence'])
lr = LogisticRegression()
lr = lr.fit(train, label)
prediction = lr.predict(test)
```
