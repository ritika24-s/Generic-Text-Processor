# Class Vectoriser can deal with three different types 
# of vectorisers present in scikit learn

# 1. CountVectorizer - 
# Convert a collection of text documents to a matrix of token counts.

# 2. TfidfVectorizer - 
# Convert a collection of raw documents to a matrix of TF-IDF features
# TF-IDF are word frequency scores that try to highlight words that are 
# more interesting, e.g. frequent in a document but not across documents.
# The TfidfVectorizer will tokenize documents, learn the vocabulary
# and inverse document frequency weightings, and allow you to encode 
# new documents

# 3. hashingVectorizer

#from preprocess import preprocesser
from Preprocessing.preprocess import preprocesser

class Vectoriser (preprocesser):       
    def __init__(self, filename, vectorizer="count", lowercase=True, 
                n_gram = (1,2), max_df =1.0, min_df =1):
        super().__init__(filename)
        
        # create an instance of the vectorizer (count, tf-idf, hashing)
        print("vectoriser selecting")
        self.select_vectorizer(vectorizer, lowercase, n_gram, max_df, min_df)
        self.fit_and_transform_vect()
        super().close_file()

    def select_vectorizer(self, vectorizer, lowercase, n_gram, max_df, min_df):
        # create an instance of CountVectorizer class
        if vectorizer == "count":
            print("vectoriser selected")
            from sklearn.feature_extraction.text import CountVectorizer
            self.vectorizer = CountVectorizer(
                analyzer="word", # default
                lowercase= lowercase, # default, convert to lowercase
                tokenizer= self.tokenise(), # this step tokenizes the text
                # punctuation is removed
                stop_words= self.stop_words, # remove stop_words
                # token_pattern = define patterns to identify tokens 
                ngram_range= n_gram, # tuple to determine the range for n-grams
                max_df= max_df,
                min_df= min_df
            )
        
        # create an instance of TF-IDF Vectorizer class
        elif vectorizer == "tf-idf":
            from sklearn.feature_extraction.text import TfidfVectorizer
            self.vectorizer = TfidfVectorizer(

            )

    # call the fit and transform function
    def fit_and_transform_vect(self):  
        # call the fit() function to tokenize and learn vocabulary
        
        self.vectorizer.fit([self.text])        
        
        # access the vocabulary to see what exactly was tokenized
        print(self.vectorizer.vocabulary_)

        # Terms that were ignored
        # The stop_words_ attribute can get large and increase the model
        # size when pickling. This attribute can be safely removed using
        # delattr or set to None before pickling
        print(self.vectorizer.stop_words_)

        # call the transform() function to encode documents as vectors
        # Transform documents to document-term matrix
        vector = self.vectorizer.transform([self.text])

        # summarize encoded vector
        print(vector.shape)
        print(type(vector))

        # The vectors returned from a call to transform() will be sparse
        # vectors, and can transform back to NumPy arrays to look and better
        # understand what is going on by calling the toarray() function.
        print(vector.toarray())

filename = "File\metamorphosis_clean.txt"
count_vector = Vectoriser(filename=filename, vectorizer="count")
# tfidf_vector = Vectoriser(filename=filename, vectorizer="tf-idf")