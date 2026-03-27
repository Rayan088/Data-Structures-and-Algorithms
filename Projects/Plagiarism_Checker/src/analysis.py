class Analysis:
    def longest_copied_phrase(self, k_grams1, k_grams2):
        longest_phrase = None

        for i in k_grams1:
            for j in k_grams2:
                if i == j:
                    longest_phrase = i
                    break
        #Checking for longest a matching phrase

        if longest_phrase == None:
            return "No matching phrase found"
        else:
            return f"Longest phrase: {longest_phrase}"
        
    #Method which finds longest phrase of length k of k_grams
        
    def top_matching_phrase(self):
        pass