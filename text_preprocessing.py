import string
import re

class Text:
    def __init__(self, filename) -> None:
        self.load_file(filename)
        self.close_file()
        self.clean_data_nltk()

    # load the file
    def load_file(self, filename):
        self.file = open(filename, 'r') 
        self.text = self.file.read()

    # close the file
    def close_file(self):
        self.file.close()

    # clean the data
    def clean_data(self):
        # split text into all the tokens
        # can also regex here to split the text  
        # re.split('\W+', self.text)
        # but important punctuations might be lost
        # like what's
        self.data = self.text.split()

        # normalise casing of the letters 
        # helps in identifying duplicate letters
        self.data = [word.lower() for word in self.data]

        # remove duplicates
        self.data = sorted(set(self.data))

        # print("sorted list", self.data)    
        
        # now to replace all the punctuations with "" 
        # use string.punctuation to get a string of all the punctuations
        # and use regex to substitute it with ""

        # [%s] is used to put all punctuatons inside bracket
        # re.escape puts the \ sign in front of every punctuation mark
        punc = re.compile('[%s]' % re.escape(string.punctuation))
        stripped = [punc.sub("", w) for w in self.data]
        # remove duplicates
        stripped = sorted(set(stripped))

        # can also use the translate method. faster than re
        #stripped =  [w.translate(str.maketrans("","", string.punctuation))  for w in self.data]

        # to remove non-printable characters
        non_print_punc = re.compile('[^%s]' % re.escape(string.printable))
        result = [non_print_punc.sub("", w) for w in self.data]

        #print("result", result)
        print("stripped", stripped)
      

filename = "metamorphosis_clean.txt"
text = Text(filename)