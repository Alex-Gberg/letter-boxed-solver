def letterSetsContain(inp, letterSets):
    for a in inp:
        for s in letterSets:
            if a in s:
                return True
    return False

def getLettersManual():
    sides = ["top", "right", "bottom", "left"]
    
    print("=== Insert the letters! ===")
    
    letterSets = []
    for i in range(4):
        while (True):
            inp = input(f"Type the {sides[i]} side letters: ")
            if len(inp) == 3 and not letterSetsContain(inp, letterSets):
                letterSets.append(inp)
                break
            else:
                print("invalid input")

    return letterSets

def nextPossibleLetters(letter, letterSets):
    if not letterSetsContain(letter, letterSets):
        return None
    possibleLetters = []
    for s in letterSets:
        if letter not in s:
                possibleLetters += s
    
    return possibleLetters

def findWordsStartingWith(letter, letterSets):
    if not letterSetsContain(letter, letterSets):
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
    remainingLetters = set([letter for letterSet in letterSets for letter in letterSet])
    
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

# TODO
# create a hash map when finding all possible words and organize by starting letter, then only look for next word in that set
import itertools
import math
def bruteForceAlgorithm(letterSets):
    words = findAllPossibleWords(letterSets)
    
    bestWordCount = math.inf
    bestSolutions = []
    r = 1
    while True:
        for perm in itertools.permutations(words, r=r):
            currWordCount = 0
            currSolution = []
            remainingLetters = set([letter for letterSet in letterSets for letter in letterSet])
            for word in perm:
                if currSolution and currSolution[-1][-1] != word[0]:
                    break

                currWordCount += 1
                currSolution.append(word)

                for a in word:
                    if a in remainingLetters:
                        remainingLetters.remove(a)

                if not remainingLetters:
                    if currWordCount < bestWordCount:
                        bestWordCount = currWordCount
                        bestSolutions = [currSolution]
                    elif currWordCount == bestWordCount:
                        bestSolutions.append(currSolution)
                    break
        if bestSolutions:
            break
        r += 1

    return bestSolutions

# TODO make s in solution(s) conditional on length of solutions
def displaySolutions(solutions):
    print(f"=== {len(solutions)} Solution(s) Found! ===")
    for x, seq in enumerate(solutions):
        print(f"{x+1}: ", end="")
        for i in range(len(seq)):
            print(f"{seq[i]}, ", end="") if i != len(seq)-1 else print(seq[i])

# TODO let the user chooose which algo to use
if __name__ == "__main__":
    letterSets = getLettersManual()
    displaySolutions(bruteForceAlgorithm(letterSets))