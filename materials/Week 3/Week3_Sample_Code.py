# %%
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# %%
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
