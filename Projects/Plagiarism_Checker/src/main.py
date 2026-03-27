from preprocess import clean_text, tokenisation, remove_stop_words
from kgrams import Kgrams
from similarity import Similarity
from analysis import Analysis

def read_file(file):
    try:
        with open(file, "r", encoding="utf8") as rfile:
            return rfile.read()
    except FileNotFoundError:
        print(f"Error: {file} not found.")
        return ""

print("------------------Plagiarism Checker---------------------")
#Funtion that reads files into strings
    
doc1 = read_file("Projects/Plagiarism_Checker/data/sample1.txt")
doc2 = read_file("Projects/Plagiarism_Checker/data/sample2.txt")

#Reads both files into strings

tokens1 = remove_stop_words(tokenisation(clean_text(doc1)))
tokens2 = remove_stop_words(tokenisation(clean_text(doc2)))

#Removes stop words

sim = Similarity()
score = sim.jaccard_similarity(tokens1, tokens2)

print(score)

#Calculates similarity through Jaccard Similarity

kgram = Kgrams()
kgrams1 = kgram.generate_kgrams(tokens1, 6)
kgrams2 = kgram.generate_kgrams(tokens2, 6)

#Generates 3 grams for each document

analysis = Analysis()

longest_phrase = analysis.longest_copied_phrase(kgrams1, kgrams2)
most_common_word = analysis.top_matching_phrase(tokens1, tokens2)

print(longest_phrase)
print(most_common_word)

#Calculates longest phrase of k gram and the most common word