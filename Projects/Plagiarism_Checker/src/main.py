def read_file(file):
    try:
        with open(file, "r") as rfile:
            return rfile.read()
    except FileNotFoundError:
        print(f"Error: {file} not found.")
        return ""

#Funtion that reads files into strings
    
doc1 = read_file("Projects/Plagiarism_Checker/data/sample1.txt")
doc2 = read_file("Projects/Plagiarism_Checker/data/sample2.txt")