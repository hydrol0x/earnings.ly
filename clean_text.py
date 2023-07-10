from summa import keywords
from summa.summarizer import summarize

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def get_keywords(text:str) -> list:
    # Open the file in read mode
    # with open(textfile, 'r') as file:
    #     # Read the contents of the file
    #     text = file.read()

    # Extract keywords using TextRank
    extracted_keywords = keywords.keywords(text)

    # Print the extracted keywords
    return extracted_keywords

"""
Use in order to filter down the number of words in the text, removes 'stop' words (and, or,is, etc.)
"""
# nltk.download('punkt')
# nltk.download('stopwords')

def remove_stopwords(text:str) -> str:
       # Set of common stopwords
    stop_words = set(stopwords.words('english'))

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove the stopwords
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

    # Reconstruct the sentence
    filtered_sentence = ' '.join(filtered_tokens)
    return filtered_sentence