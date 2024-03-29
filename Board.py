from WordPlacer import WordPlacer, HORIZONTAL, VERTICAL
from tabulate import tabulate
#from os import system
from time import sleep
from copy import deepcopy

class Board:
    def __init__(self, layout, wordsList, placersList):
        self.layout = layout
        self.remainingWordsList = set(wordsList)
        self.placersList = placersList
        self.filledPlacers = []

        
    """clearing all of the letters in a given wordPlacer. Need to check for clashes, as I 
    wouldn't want to clear letters that are clashing with other wordPlacers."""
    def clearWordPlacer(self, wordPlacer: WordPlacer):
        if wordPlacer.orientation == HORIZONTAL:
            placedVerticals = [p for p in self.filledPlacers if p.orientation == VERTICAL]
            for column in range(wordPlacer.start.column, wordPlacer.end.column + 1):
                isClashing = False
                for p in placedVerticals:    
                    if (p.start.column == column and p.start.row <= wordPlacer.start.row and 
                        p.end.row >= wordPlacer.start.row): #This square is the clashing point.
                        isClashing = True
                        break
                if not isClashing: self.layout[wordPlacer.start.row][column] = ""
        else:
            placedHorizontals = [p for p in self.filledPlacers if p.orientation == HORIZONTAL]
            for row in range(wordPlacer.start.row, wordPlacer.end.row + 1):
                isClashing = False
                for p in placedHorizontals:    
                    if (p.start.row == row and p.start.column <= wordPlacer.start.column and 
                        p.end.column >= wordPlacer.start.column): #This square is the clashing point.
                        isClashing = True
                        break
                if not isClashing: self.layout[row][wordPlacer.start.column] = ""
            
        

    def fillPlacerWithWord(self, wordPlacer: WordPlacer, word, override: bool):
        tempLayout = deepcopy(self.layout) #IMPORTANT! Assigning by value, not by reference. 
        isPossible = True
        if len(word) != wordPlacer.length: 
            raise Exception("The length of the word is different from the wordPlacer")
        if wordPlacer.orientation == HORIZONTAL:
            wordIndex = 0    
            for column in range(wordPlacer.start.column, wordPlacer.end.column + 1):      
                if (not override and not self.isSquareAvailable(
                    tempLayout[wordPlacer.start.row][column], word[wordIndex])):
                    isPossible = False
                    break
                tempLayout[wordPlacer.start.row][column] = word[wordIndex]
                wordIndex += 1
        else:
            wordIndex = 0
            for row in range(wordPlacer.start.row, wordPlacer.end.row + 1):
                if (not override and not self.isSquareAvailable
                    (tempLayout[row][wordPlacer.start.column], word[wordIndex])):
                    isPossible = False
                    break
                tempLayout[row][wordPlacer.start.column] = word[wordIndex] 
                wordIndex += 1    
        
        #if the filling was a success, now we have the new board.   
        if isPossible: 
            self.layout = deepcopy(tempLayout)
            return True
        else: return False
        
        
    #if the current square is empty or the same as the candidate, then it is a pass
    def isSquareAvailable(self, current, candidate): return current in ['', candidate]
    
    #given the word list, returns all words of the requested length, excluding
    #the already visited words.
    def getWordsOfLength(self, n, restraints): 
        return [word for word in self.remainingWordsList 
                if len(word) == n and word not in restraints]
    
    def printBoard(self): 
        #system("cls")
        print(tabulate(self.layout,tablefmt="grid"))
        #sleep(0.5)
        pass

        

        