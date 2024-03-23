import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')