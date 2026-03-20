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

        if union == 0 or intersection == 0:
            return 0
        else:
            return calculation
        
    #Function that calculated Jaccard Similarity