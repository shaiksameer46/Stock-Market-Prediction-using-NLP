# %%
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, TweetTokenizer
from nltk.stem.porter import PorterStemmer
import spacy

# nltk.download('stopwords')
# $ python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")


# %%
news = 'There\'s A New Trading Tool That Allows Traders To Trade ' \
       'Cannabis With Leverage'
news_l = word_tokenize(news)
print(news_l)
# > ['There', "'s", 'A', 'New', 'Trading', 'Tool', 'That', 'Allows',
# > 'Traders', 'To', 'Trade', 'Cannabis', 'With', 'Leverage']


# %%
news_doc = nlp(news)
print(news_doc)
# > There's A New Trading Tool That Allows Traders To Trade Cannabis
# > With Leverage
print(type(news_doc[0]))
# > <class 'spacy.tokens.token.Token'>
print([i for i in news_doc if not i.is_stop])
# > [New, Trading, Tool, Allows, Traders, Trade, Cannabis, Leverage]


# %%
stemmer = PorterStemmer()
print([stemmer.stem(i.lemma_) for i in news_doc])
# > ['there', 'be', 'a', 'new', 'trade', 'tool', 'that', 'allow', 'trader',
# > 'to', 'trade', 'cannabi', 'with', 'leverag']


# %%
news = 'There\'s A New Trading Tool That Allows Traders To Trade ' \
       'Cannabis With Leverage'
stemmer = PorterStemmer()
news_doc = nlp(news)
news_l = [i.lemma_ for i in news_doc if not i.is_stop]
news_l = [stemmer.stem(i) for i in news_l]
print(news_l)
# > ['new', 'trade', 'tool', 'allow', 'trader', 'trade', 'cannabi', 'leverag']


# %%
tweet = "RT @Twitter @chapagain Hello There! Have a great day. :) #good " \
        "#morning http://chapagain.com.np"
stemmer = PorterStemmer()
stopwords_english = stopwords.words('english')
# remove stock market tickers like $GE
tweet = re.sub(r'\$\w*', '', tweet)
# remove old style retweet text "RT"
tweet = re.sub(r'^RT[\s]+', '', tweet)
# remove hyperlinks
# tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
tweet = re.sub(r'https?://[^\s\n\r]+', '', tweet)
# remove hashtags
# only removing the hash # sign from the word
tweet = re.sub(r'#', '', tweet)
# tokenize tweets
tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                           reduce_len=True)
tweet_tokens = tokenizer.tokenize(tweet)

tweets_clean = []
for word in tweet_tokens:
    if (word not in stopwords_english and  # remove stopwords
            word not in string.punctuation):  # remove punctuation
        # tweets_clean.append(word)
        stem_word = stemmer.stem(word)  # stemming word
        tweets_clean.append(stem_word)

print(tweets_clean)
# > ['hello', 'great', 'day', ':)', 'good', 'morn']
