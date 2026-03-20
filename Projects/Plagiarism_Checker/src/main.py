from preprocess import clean_text, tokenisation, remove_stop_words
from kgrams import Kgrams
from similarity import Similarity

def read_file(file):
    try:
        with open(file, "r") as rfile:
            return rfile.read()
    except FileNotFoundError:
        print(f"Error: {file} not found.")
        return ""

#Funtion that reads files into strings
    
doc1 = read_file("Projects/Plagiarism_Checker/data/sample1.txt")
doc2 = read_file("Projects/Plagiarism_Checker/data/sample2.txt")

#Reads both files into strings

tokens1 = remove_stop_words(tokenisation(clean_text(doc1)))
tokens2 = remove_stop_words(tokenisation(clean_text(doc2)))

#Removes stop words

sim = Similarity()
score = sim.jaccard_similarity(tokens1, tokens2)

#Calculates similarity through Jaccard Similarity

kgram = Kgrams()
kgrams1 = kgram.generate_kgrams(tokens1, 3)
kgrams2 = kgram.generate_kgrams(tokens2, 3)

#Generates 3 grams for each document