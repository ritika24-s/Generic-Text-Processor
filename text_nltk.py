# Class to demonstrate the functions of nltk

import nltk
# nltk.download()
import string
import re

class nltk:
    def __init__(self, filename) -> None:
        self.load_file(filename)
        self.close_file()
        self.tokenise()
        self.lower_case()
        self.remove_punctuation()
        self.remove_stopwords()
        self.stemming()

    # load the file
    def load_file(self, filename):
        self.file = open(filename, 'r') 
        self.text = self.file.read()

    # close the file
    def close_file(self):
        self.file.close()

    # tokenise the text
    def tokenise(self):
        # to tokenise each sentence
        from nltk import sent_tokenize, word_tokenize

        self.data = sent_tokenize(self.text)
        print("length of original Text", len(self.text))

        # to tokenise word from the entire text irrespective
        # of sentence, use word_tokenize()
        # to preserve line-wise tokenisation, use 
        # preserve_line = True
        # this function captures all the punctuations as well
        self.tokens = word_tokenize(self.text)
            
    # convert to lower case
    def lower_case(self):
        self.tokens = [word.lower() for word in self.tokens]

    def remove_punctuation(self):
        # to remove punctuations either use isalpha()
        # but this method remove words like armour-like
        # thus use re.sub to remove punctuation from each token

        # remove punctuation from each individual token
        punc = re.compile('[%s]' % re.escape(string.punctuation))
        self.tokens = [punc.sub("", w) for w in self.tokens]

        # now remove all the punctuations from the list of tokens
        self.tokens = [word for word in self.tokens if word.isalpha() ]
        
    def remove_stopwords(self):
        # remove stop words
        from nltk.corpus import stopwords
        stop_words = stopwords.words("english")

        stop_words += ['ive','nt', 'ï']
        self.tokens = [words for words in self.tokens if words not in stop_words]
        # print(sorted(self.tokens))

    # find relevant stem of each word
    def stemming(self):
        from nltk.stem.porter import PorterStemmer
        porter = PorterStemmer()
        self.stems = [porter.stem(word) for word in self.tokens]
        print(sorted(self.stems))
        
filename = "metamorphosis_clean.txt"
text = nltk(filename)