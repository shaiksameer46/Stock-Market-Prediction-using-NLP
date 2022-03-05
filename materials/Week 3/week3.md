# Week 3 - Naïve Bayes Model


## Reference

- [Naive Bayes Classifier - Wikipedia](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
- [Naive Bayes - Scikit Learn Documentation](https://scikit-learn.org/stable/modules/naive_bayes.html#multinomial-naive-bayes)
- [CountVectorizer - Scikit Learn Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)


## Methodology

### Introduction

Given the following messages,
- "I am rather excited"
- "You are rather happy"
- "I am happy"
- "I am tired"

we can count the frequecy and generate a table.

| Word    | Positive | Negative |
|---------|----------|----------|
| I       | 2        | 1        |
| am      | 2        | 1        |
| rather  | 1        | 1        |
| excited | 1        | 0        |
| You     | 1        | 0        |
| are     | 1        | 0        |
| happy   | 2        | 0        |
| tired   | 0        | 1        |

Further, we can calculate a probability table,

| Word    | Positive | Negative |
|---------|----------|----------|
| I       | 0.2      | 0.25     |
| am      | 0.2      | 0.25     |
| rather  | 0.1      | 0.25     |
| excited | 0.1      | 0        |
| You     | 0.1      | 0        |
| are     | 0.1      | 0        |
| happy   | 0.2      | 0        |
| tired   | 0        | 0.25     |

from which we can apply the Bayes' Rule to represent the sentiment of a single word. For example,

<img src="https://render.githubusercontent.com/render/math?math=P(\text{sentiment})=\frac{P(positive|am)}{P(negative|am)}=\frac{\frac{P(am, positive)}{\sum_{s=pos,neg}P(am|s)P(s)}}{\frac{P(am, negative)}{\sum_{s=pos,neg}P(am|s)P(s)}}=\frac{P(am, positive)}{P(am, negative)}.">

Naturally, for sentences,

<img src="https://render.githubusercontent.com/render/math?math=P(\text{sentence sentiment})=\prod P(\text{word sentiment}).">

**Question 1**: What will happen if the sentence is `I am thrilled`?

**Question 2**: What will happen if `excited` and `tired` appear in one single sentence?


## Prior Probability and Laplace Smoothing

### Prior Probability

<img src="https://render.githubusercontent.com/render/math?math=\text{Prior Probability}=\frac{N_{pos}}{N_{neg}}.">

**Question 3**: Calculate the sentiment coefficient of the message in `Question 1` again, what do you find?

### Laplace Smoothing

See Reference #2.

| Word    | Positive | Negative |
|---------|----------|----------|
| I       | 0.17     | 0.17     |
| am      | 0.17     | 0.17     |
| rather  | 0.11     | 0.17     |
| excited | 0.11     | 0.08     |
| You     | 0.11     | 0.08     |
| are     | 0.11     | 0.08     |
| happy   | 0.17     | 0.08     |
| tired   | 0.06     | 0.17     |


## Error Analysis

### Word Order

The two sentences have the same rating, but the sentiment is totally different.

> I'm not tired. Rather, I'm happy.

> I'm not happy. Rather, I'm tired.

### Adversarial Attacks

These include sarcasm, irony, euphemisms.


## Example

```Python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

text = ['i am happy', 'i am tricked', 'i am sad', 'i am tired', 'i am tired']
label = [1, 0, 0, 0, 0]
cv = CountVectorizer()
cv_text = cv.fit_transform(text)
print(cv.get_feature_names_out())
# > ['am' 'happy' 'sad' 'tired' 'tricked']
mnb = MultinomialNB()
mnb.fit(cv_text, label)
print(mnb.feature_count_)
# > [[4. 0. 1. 2. 1.]
# >  [1. 1. 0. 0. 0.]]
```
