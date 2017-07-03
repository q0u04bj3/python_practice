import re

def name_score(file):
    pat = r'[A-Z]+'
    score = []
    sortedFile = sorted(re.findall(pat, file))
    
    for index, element in enumerate(sortedFile):
        score.append(sum([ord(letter) - 64 for letter in element]) * (index + 1))

    return score