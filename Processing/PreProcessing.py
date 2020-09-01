from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk

import numpy as np
import re

# inflect import function
import inflect

p = inflect.engine()

# Downloading package

# to avoid error when run without internet connection
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('words')

words = set(nltk.corpus.words.words())


# Source: https://towardsdatascience.com/tf-idf-for-document-ranking-from-scratch-in-python-on-real-world-dataset-796d339a4089
def convert_lower_case(data):
    return np.char.lower(data)


def extract_words(data):
    data = " ".join(w for w in nltk.wordpunct_tokenize(data) if w.lower() in words or not w.isalpha())
    return data


def remove_stop_words(data):
    stop_words = stopwords.words('english')
    words = word_tokenize(str(data))
    new_text = ""
    for w in words:
        if w not in stop_words and len(w) > 1:
            new_text = new_text + " " + w
    return new_text.strip()


def remove_punctuation(data):
    symbols = '!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n'
    for i in range(len(symbols)):
        data = np.char.replace(data, symbols[i], ' ')
        data = np.char.replace(data, "  ", " ")
    data = np.char.replace(data, ',', '')
    return data


def remove_apostrophe(data):
    return np.char.replace(data, "'", "")


def stemming(data):
    """
    Reducing multiple word variation
    Example: Consult, Consultant,Consulting,Consultants -->consult  (only in english-vocabs)

    Args:

        data (String): html website
    Returns:
        newText: text with only one word variation
    """
    stemmer = PorterStemmer()
    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        new_text = new_text + " " + stemmer.stem(w)
    return new_text


def convert_numbers(data):
    """
    Convert number to words
    :param data:
    :return: text without numbers -> 2 to "two"
    """
    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        try:
            # example
            w = p.number_to_words(int(w))
        except:
            a = 0
        new_text = new_text + " " + w
    new_text = np.char.replace(new_text, "-", " ")
    return new_text


def preprocess(data):
    data = formate_text_bayes(data)
    data = convert_lower_case(data)
    data = remove_stop_words(data)
    # data = stemming(data)
    data = extract_words(data)
    # data = formate_text_bayes(data)

    return data


"""
def create_dataset(document_list):
    dataset=[]
    for i in range(len(document_list)):

    return dataset
"""


def extrac_data(dataset):
    """
    Extract document-body,title and query
    :param dataset:
    :returns processed_text,processed_title: Cleaned text from document and titel

    """

    processed_text = (word_tokenize(str(preprocess(dataset[0]))))
    processed_title = (word_tokenize(str(preprocess(dataset[1]))))
    processed_query = (word_tokenize(str(preprocess(dataset[2]))))

    return processed_text, processed_title, processed_query


def process_body_text(dataset):
    processed_text = []
    for i in range(len(dataset)):
        processed_text += (word_tokenize(str(preprocess(dataset[i][0]))))

    return processed_text


def formate_text(text):
    text = re.sub('[^a-zA-Z0-9_]', '  ', text)
    return text


def formate_text_bayes(text):
    text = re.sub('[^a-zA-Z]', '  ', text)
    return text


def formate_text_class(text):
    text = re.sub('[^a-zA-Z]', '  ', text)

    return text
def formate_text2(text):
    text = re.sub('[^a-zA-Z0-9_-]', '  ', text)
    return text

"""
text: List with filename
return List"""


def formate_name(array):
    array = [re.sub('(\.class)', '', file) for file in array]

    array = [re.sub('(/)', '.', file) for file in array]
    array = [re.sub('(^\.)', '', file) for file in array]
    return array

def delete_not_class(list):
    new_list=[]
    for item in list:
        if re.match("([\w]+\.[\w]+\.[A-Za-z0-9_\.]+)", item) is not None:
            new_list.append(item)

    return new_list