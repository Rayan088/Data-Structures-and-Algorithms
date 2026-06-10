from src.preprocess import clean_text, tokenisation, remove_stop_words
from src.kgrams import Kgrams
from src.similarity import Similarity
from src.analysis import Analysis

def run_pipeline(text1, text2):
    tokens1 = remove_stop_words(tokenisation(clean_text(text1)))
    tokens2 = remove_stop_words(tokenisation(clean_text(text2)))

    sim = Similarity()
    score, label = sim.jaccard_similarity(tokens1, tokens2)

    kgram = Kgrams()
    kgrams1 = kgram.generate_kgrams(tokens1, 3)
    kgrams2 = kgram.generate_kgrams(tokens2, 3)

    analysis = Analysis()

    longest_phrase = analysis.longest_copied_phrase(kgrams1, kgrams2)
    most_common_word = analysis.top_matching_phrase(tokens1, tokens2)

    return {
        "score": score,
        "label": label,
        "longest_phrase": longest_phrase,
        "most_common": most_common_word
    }