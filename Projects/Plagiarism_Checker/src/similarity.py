class Similarity:
    def frequency_counting(self, tokens):
        count = {}

        for token in tokens:
            if token in count:
                count[token] += 1
            else:
                count[token] = 1

        return count
    
    #Function that counts occurences of indivisual tokens

    def jaccard_similarity(self, tokens1, tokens2):
        set1 = set(tokens1)
        set2 = set(tokens2)

        intersection = len(set1 & set2) #Calculation of intersection
        union = len(set1 | set2) #Calculation of union

        calculation = abs(intersection) / abs(union) #Formula of Jaccard Similarity
        calculation = format(calculation, "0.2g") #Rounded to 2 decimal points
        calculation = float(calculation)

        if union == 0:
            return f"Jaccard score: ({calculation}) signifies No Similarity"
        elif  0.0 < calculation <= 0.1:
            return f"Jaccard score: ({calculation}) signifies Very Low Similarity"
        elif 0.1 < calculation <= 0.3:
            return f"Jaccard score: ({calculation}) signifies Low Similarity"
        elif 0.3 < calculation <= 0.5:
            return f"Jaccard Score ({calculation}) signifies Moderate Similarity"
        elif 0.5 < calculation <= 0.7:
            return f"Jaccard Score ({calculation}) signifies High Similarity"
        else:
            return f"Jaccard Score ({calculation}) signifies Very High Similarity"

        #Result of Jaccard Score
        
    #Function that calculated Jaccard Similarity