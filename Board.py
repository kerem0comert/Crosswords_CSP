from WordPlacer import WordPlacer, HORIZONTAL
from tabulate import tabulate

class Board:
    def __init__(self, layout, wordsList, placersList):
        self.layout = layout
        self.wordsList = wordsList
        self.placersList = placersList

    def fillWordPlacerWithWord(self, wordPlacer: WordPlacer, word):
        tempLayout = self.layout 
        isPossible = True
        if len(word) != wordPlacer.length: 
            raise Exception("The length of the word is different from the wordPlacer")
        if wordPlacer.orientation == HORIZONTAL:
            for index in range(wordPlacer.length):          
                
                tempLayout[wordPlacer.start.row][index] = word[index]
        else:
            for index in range(wordPlacer.length):
                tempLayout[index][wordPlacer.start.column] = word[index]
                
        if isPossible: self.layout = tempLayout
    
    #given the word list, returns all words of the requested length
    def getWordsOfLength(self, n): return [word for word in self.wordsList if len(word) == n]
    
    def printBoard(self): print(tabulate(self.layout,tablefmt="grid"))

        

        