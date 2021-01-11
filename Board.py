from WordPlacer import WordPlacer, HORIZONTAL
from tabulate import tabulate
from os import system
from time import sleep

class Board:
    def __init__(self, layout, wordsList, placersList):
        self.layout = layout
        self.remainingWordsList = set(wordsList)
        self.placersList = placersList
        self.filledPlacers = set() #make it a set to make sure it contains unique elements

    def canFillPlacerWithWord(self, wordPlacer: WordPlacer, word):
        tempLayout = self.layout 
        isPossible = True
        if len(word) != wordPlacer.length: 
            raise Exception("The length of the word is different from the wordPlacer")
        if wordPlacer.orientation == HORIZONTAL:
            for index in range(wordPlacer.length):          
                if not self.isSquareAvailable(tempLayout[wordPlacer.start.row][index], word[index]):
                    isPossible = False
                    break
                tempLayout[wordPlacer.start.row][index] = word[index]
        else:
            for index in range(wordPlacer.length):
                if not self.isSquareAvailable(tempLayout[index][wordPlacer.start.column], word[index]):
                    isPossible = False
                    break
                tempLayout[index][wordPlacer.start.column] = word[index]     
        
        #if the filling was a success, now we have the new board.   
        if isPossible: 
            self.layout = tempLayout
            return True
        else: return False
        
        
    #if the current square is empty or the same as the candidate, then it is a pass
    def isSquareAvailable(self, current, candidate): return current in ['', candidate]
    
    #given the word list, returns all words of the requested length
    def getWordsOfLength(self, n): return [word for word in self.remainingWordsList if len(word) == n]
    
    def printBoard(self): 
        system("cls")
        print(tabulate(self.layout,tablefmt="grid"))
        sleep(1)

        

        