import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('popular')
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'['+string.punctuation+']', '', text)
    text = [word for word in text.split(' ') if word not in stop_words]
    text = [stemmer.stem(word) for word in text]
    return text 