from pyspark import SparkContext, SparkConf
import nltk
from nltk.stem.porter import *
from sklearn.feature_extraction import stop_words
import string
from collections import Counter

# Spark Setup
app_name = "most_common_word_review"
conf = SparkConf().setAppName(app_name)
sc = SparkContext(conf=conf)

def tokenize(text):
    """
    Tokenize text and return a non-unique list of tokenized words
    found in the text. Normalize to lowercase, strip punctuation,
    remove stop words, drop words of length < 3, strip digits.
    """
    text = text.lower() # get lower case
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text)  # remove all punctuation + numbers
    nopunct = re.sub(r"\s+", ' ', nopunct) # replace multiple spaces with one space
    words = nltk.word_tokenize(nopunct)
    words = [w for w in words if len(w) > 2] # drop words of length < 3
    words = [w for w in words if w not in stop_words.ENGLISH_STOP_WORDS] # drop stop words
    words = stemwords(words)  # call stemwords() to get words stemmed
    return words

def stemwords(words):
    """
    Given a list of tokens/words, return a new list with each word
    stemmed using a PorterStemmer.
    """
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(w) for w in words]
    return stemmed

def most_common_n(filename, n):
    rdd = sc.textFile(filename, 8)
    rdd_listed = rdd.flatMap(lambda x: tokenize(x))
    ctr = Counter(rdd_listed.collect())
    most_common_list = ctr.most_common(n)
    return most_common_list

filenames = ["reviews_10000.txt",
            "reviews_2below_stars_10000.txt",
            "reviews_4above_stars_10000.txt"]
n = 50

with open(f"most_common_{n}.txt", "w") as f:
    for filename in filenames:
        f.write(f'{filename}\n')
        for item in most_common_n(filename, n):
            f.write(f'{item}\n')
        f.write('------------\n')

sc.stop()