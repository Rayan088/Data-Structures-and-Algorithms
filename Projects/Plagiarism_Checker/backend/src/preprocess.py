import string
import re

def clean_text(text):
    text = text.lower() #Converted to lower case
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator) #Removes punctuation
    text = text.replace("-", " ") #Replaces hyphens with white space
    text = re.sub(r'\d+', '', text) #Removes numbers
    cleaned_text = " ".join(text.split()) #Removes unnecessary white space

    return cleaned_text

#Function that cleans text and returns string of cleaned_text

def tokenisation(cleaned_text):
    tokens = cleaned_text.split()

    return tokens

#Function that returns list of indivisual words as tokens

def remove_stop_words(tokens):
    stop_words = {"a","an","the","and","or","but","if","while","is","are","was","were","be","been","being",
    "of","in","to","from","on","for","with","about","as","at","by","this","that","these","those",
    "he","she","it","they","his","her","its","their","them","we","you","i","me","my","mine","your","yours",
    "so","than","then","too","very","not","no"}
    #Dictionary of common words that don't carry meaningul content to improve accuracy

    filtered_tokens = []

    for token in tokens:
        if token not in stop_words:
            filtered_tokens.append(token)
    #List that does not contain any stop words

    return filtered_tokens

#Function that removes skip words from list of tokens and returns filtered_tokens list