import string
import re

def clean_text(text):
    text = text.lower() #Converted to lower case
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator) #Removes punctuation
    text = text.replace("-", " ") #Replaces hyphens with white space
    text = re.sub(r'\d+', '', text) #Removes numbers
    text = " ".join(text.split()) #Removes unnecessary white space