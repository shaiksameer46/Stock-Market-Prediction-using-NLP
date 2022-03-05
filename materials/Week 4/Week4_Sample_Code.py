# %%
from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity
from gensim.models import KeyedVectors

# %%
model = KeyedVectors.load_word2vec_format(
    r'data/GoogleNews-vectors-negative300.bin', binary=True)
dog = model['dog']
print(type(dog))
print(dog.shape)
print(dog[:5])

# %%
egg, food, disease = [5, 15], [20, 40], [30, 20]
print(euclidean_distances([egg], [food]))
print(euclidean_distances([food], [disease]))
print(cosine_similarity([egg], [food]))
print(cosine_similarity([food], [disease]))
