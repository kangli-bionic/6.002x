import pylab
import numpy as np

# You may have to change this path
WORDLIST_FILENAME = "/home/peter/6.002x/week2/L4P5/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    wordLengths = []
    vowelNum = []
    for word in wordList:
        wordLengths.append(len(word))
        count = 0
        for letter in word:
            if letter == 'a' or letter == 'e' or letter =='i'or letter == 'o' or letter =='u':
                count = count+1

        vowelNum.append(count)
    npWordLength = np.array(wordLengths, dtype=float)
    npVowelNum = np.array(vowelNum, dtype=float)
    vowelRatio = npVowelNum/npWordLength
    pylab.hist(vowelRatio, numBins)

  
if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)

