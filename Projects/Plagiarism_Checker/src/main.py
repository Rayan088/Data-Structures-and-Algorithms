from preprocess import clean_text, tokenisation, remove_stop_words

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

tokens1 = remove_stop_words(tokenisation(clean_text(doc1)))
tokens2 = remove_stop_words(tokenisation(clean_text(doc2)))

print(f"Document 1 Tokens: {tokens1}")
print("\n")
print(f"Document 2 Tokens: {tokens2}")