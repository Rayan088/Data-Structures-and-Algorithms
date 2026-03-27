from collections import Counter

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
        
    def top_matching_phrase(self, k_grams1, k_grams2):
        common_words = []

        for i in k_grams1:
            for j in k_grams2:
                if i == j:
                    common_words.append(i)
        #Finding common words in both passages

        frequency_count = Counter(common_words)
        #Counting frequency of common words

        most_common_word = None
        max_frequency = 0

        for word, frequency in frequency_count.items():
            if frequency > max_frequency:
                max_frequency = frequency
                most_common_word = word
        #Finding the maximum frequency of the most common word

        if most_common_word != None:
            return f"Most common word: {most_common_word} (appears {max_frequency} times)"
        else:
            return f"No matching words found"
        
    #Method which finds the frequency of common words