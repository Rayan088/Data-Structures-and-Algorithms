class Kgrams:
    def generate_kgrams(self, tokens, k):
        k_grams = []

        for i in range(len(tokens) - k + 1): #Looping to avoid going out of bounds
            phrase = " ".join(tokens[i:i+k]) #Converts list into string
            k_grams.append(phrase)

        return k_grams
    
#Function that splits tokens into kgrams of length k