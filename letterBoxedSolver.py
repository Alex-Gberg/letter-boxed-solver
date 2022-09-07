def setsContain(inp, letterSets):
    for a in inp:
        for s in letterSets:
            if a in s:
                return True
    return False

def getLettersManual():
    sides = ["top", "right", "bottom", "left"]
    letterSets = []

    for i in range(4):
        while (True):
            inp = input(f"Type the {sides[i]} side letters: ")
            if len(inp) == 3 and not setsContain(inp, letterSets):
                letterSets.append(inp)
                break
            else:
                print("invalid input")

    return letterSets

def nextPossibleLetters(letter, letterSets):
    if not setsContain(letter, letterSets):
        return None
    possibleLetters = []
    for s in letterSets:
        if letter not in s:
            for a in s:
                possibleLetters.append(a)
    
    return possibleLetters

def findWordsStartingWith(letter, letterSets):
    if not setsContain(letter, letterSets):
        return None
    
    words = []
    with open("filtered_words.txt") as wordList:
        for word in wordList:
            word = word.strip()
            if word[0] != letter or len(word) < 3:
                continue
            prevLetter = letter
            for i in range(1, len(word)):
                validWord = True
                if word[i] not in nextPossibleLetters(prevLetter, letterSets):
                    validWord = False
                    break
                prevLetter = word[i]
            if validWord:
                words.append(word.strip())
    return words

def findAllPossibleWords(letterSets):
    words = []
    for s in letterSets:
        for a in s:
            words.extend(findWordsStartingWith(a, letterSets))
    return words

def greedyAlgorithm(letterSets):
    words = findAllPossibleWords(letterSets)

    remainingLetters = set()
    for s in letterSets:
        for a in s:
            remainingLetters.add(a)
    
    solution = []
    while (remainingLetters):
        bestWord = None
        bestLetters = -1
        for word in words:
            if (solution and word[0] != solution[-1][-1]):
                continue
            wordLetters = set()
            for a in word:
                if a in remainingLetters:
                    wordLetters.add(a)
            if len(wordLetters) > bestLetters:
                bestLetters = len(wordLetters)
                bestWord = word
        solution.append(bestWord)
        for a in bestWord:
            if a in remainingLetters:
                remainingLetters.remove(a)

    return solution

def displaySequence(seq):
    print("SOLUTION: ", end="")
    for i in range(len(seq)):
        print(f"{seq[i]}, ", end="") if i != len(seq)-1 else print(seq[i])

if __name__ == "__main__":
    letterSets = getLettersManual()
    displaySequence(greedyAlgorithm(letterSets))