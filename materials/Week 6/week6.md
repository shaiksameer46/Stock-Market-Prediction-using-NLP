# Week 6 TF-IDF Model

## Reference

- [tf–idf - Wikipedia](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
- [sklearn.feature_extraction.text.TfidfVectorizer — scikit-learn 1.0.2 documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)


## Methodology

### Definition

> In information retrieval, **TF–IDF**, short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus.

### Formula

Assume we have Corpus D = {d_1, d_2, ..., d_N}. Then, for a single word t,

<img src=https://wikimedia.org/api/rest_v1/media/math/render/svg/dd4f8a91dd0d28a11c00c94a13a315a5b49a8070>

<img src=https://wikimedia.org/api/rest_v1/media/math/render/svg/ac67bc0f76b5b8e31e842d6b7d28f8949dab7937>

<img src=https://wikimedia.org/api/rest_v1/media/math/render/svg/10109d0e60cc9d50a1ea2f189bac0ac29a030a00>

### Example

**Corpus D**

|    | Document                              |
|----|---------------------------------------|
| d1 | This is the first document.           |
| d2 | This document is the second document. |
| d3 | And this is the third one.            |
| d4 | Is this the first document?           |

**Word List**

['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third' 'this']

**Calculation**

<img src="https://render.githubusercontent.com/render/math?math=tf(\text{'document'}, d_1)=\frac{1}{5}=0.2,">

<img src="https://render.githubusercontent.com/render/math?math=idf(\text{'document'}, D)=\log\frac{4}{3}\approx0.2877,">

<img src="https://render.githubusercontent.com/render/math?math=TFIDF(\text{'document'}, d_1, D)=0.2\times0.2877\approx0.0575.">

## Python Implementation

```Python
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?']

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names_out())
## ['and' 'document' 'first' 'is' 'one' 'second' 'the' 'third' 'this']
print(X.shape)
## (4, 9)
```

# Summary

## Data Preprocessing

- Tokenization
- Stop Words
- Stemming

## Pure Probability Model

- Naïve Bayes Model
  - Based on single words

## Document Vector Model

- Vector Space Model
  - Based on single word vectors
  - Pretrained Dataset
  - Principal Component Analysis
  - Unsupervised Learning: Approximate K-Nearest Neighbors Method

## Sparse Data Model (Disordered Vectorization Model)

- Models
  - N-gram Model
  - TF-IDF Model
- Machine Learning Methods
  - Logistic Regression
  - Support Vector Machine
  - Random Forest
