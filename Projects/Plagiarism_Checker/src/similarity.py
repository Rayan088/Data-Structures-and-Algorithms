class Similarity:
    def frequency_counting(self, tokens):
        count = {}

        for token in tokens:
            if token in count:
                count[token] += 1
            else:
                count[token] = 1

        return count

    def jaccard_similarity(self, tokens1, tokens2):
        set1 = set(tokens1)
        set2 = set(tokens2)

        intersection = len(set1 & set2)
        union = len(set1 | set2)

        calculation = abs(intersection) / abs(union)

        if union == 0 or intersection == 0:
            return 0
        else:
            return calculation