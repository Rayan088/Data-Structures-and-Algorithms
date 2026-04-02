### Overview

A Python based plagiarism detection tool that compares two texts by using text-preprocessing, k-gram phrase matching, Jaccard Similarity, and frequency based analysis.

### How it works

**Preprocessing (preprocess.py)**  
Cleans text by converting to lower case letters, removing punctuation and excess whitespace  
Tokenises texts into words  
Removes stop words (e.g. a, the, then, is)

**Generates k grams (kgrams.py)**
Converts cleaned tokens into kgrams of length k (length of k=6 used)

**Similarity Calculation (similarity.py)**  
Converts tokens into sets and finds similarity through Jaccard Similarity  
Returns a labelled similarity score:

- Very Low
- Low
- Moderate
- High
- Very High

**Analysis (analysis.py)**
Finds longest copied phrase utilising sets for fast lookup (O(n))  
Finds most common phrase by using Counter to track frequency and identify most repeated shared phrase

### How to Run

Project requres python installed (preferred: python 3.13)

Run program using:  
python.main.py

Make sure your entered files exist at:  
Projects/Plagiarism_Checker/data/sample1.txt  
Projects/Plagiarism_Checker/data/sample2.txt

### Example Output

------------------Plagiarism Checker---------------------  
Jaccard Score (0.32) signifies Moderate Similarity  
Longest phrase: modified genetically modified organisms gmos first  
Most common word: gmos (appears 19 times)

### Limitations

Limitations include:

- Only detects exact matches
- Fixed k-gram size (Currently k=6)

Cannot detect:

- Paraphrasing
- Synonyms
- Reorded Setences
