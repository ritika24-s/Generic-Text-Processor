from Preprocessing.preprocess import Vectoriser

def main():
    filename = "File\metamorphosis_clean.txt"
    count_vector = Vectoriser(filename=filename, vectorizer="count")

if __name__ == '__main__':
    main()