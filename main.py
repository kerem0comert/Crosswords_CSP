from Square import Square
from WordPlacer import WordPlacer
from Board import Board


layout = [
    ["","","","",""],
    ["*","*","","*",""],
    ["*","","","",""],
    ["","*","","",""],
    ["","","","",""],
    ["","*","*","","*"] 
    ]


wordList = ["aft","ale","eel","heel","hike","hoses","keel","knot","laser","lee","line","line","sails",
            "sheet","steer","tie"]
wordList.sort(key=lambda w: len(w), reverse=True)
#print(wordList)

"""Construct the list of placers in the given puzzle. An alternative way to keep the WordPlacers would
involve only keeping its start square and keeping whether it is horizontal or vertical. That information
would also be enough as a WordPlacer will continue until encountering a "*" obstacle or the end of the board.
However, this approach would involve for constantly checking if a WordPlacer encounters a "*" in its path.
As such, I keep the end point square for simplicity as well. By keeping this extra data, I don't need
to calculate for obstacles each time. Similarly, it also makes sense to keep the length of WordPlacer
at compile time statically."""
placers = [
    WordPlacer(0,Square(0,0),Square(0,4)),
    WordPlacer(1,Square(0,2),Square(4,2)),
    WordPlacer(2,Square(0,4),Square(4,4)),
    WordPlacer(3,Square(2,1),Square(2,4)),
    WordPlacer(4,Square(2,3),Square(5,3)),
    WordPlacer(5,Square(3,0),Square(5,0)),
    WordPlacer(6,Square(3,2),Square(3,4)),
    WordPlacer(7,Square(4,0),Square(4,4))
    ]

"""It should be better to start from the WordPlacers with higher length, so that the roots of the 
CSP Tree are constructed from longer WordPlacers. Intiutively I thought that having shorter WordPlacers
at the roots will result in more backtracking work to be done, however this idea of mine might be
irrelevant. In any case I decided to sort the WordPlacers and start with the ones that have the 
highest length."""
#placers.sort(key=lambda p: p.length, reverse=True)
#for p in placers: print(p.id)

board = Board(layout, wordList, placers)
#print(board.placersList[6].length)




def placeWord(wordPlacer, word):
    print(f"Trying {word}")
    if board.fillPlacerWithWord(wordPlacer, word, False): 
        wordPlacer.word = word
        board.filledPlacers.append(wordPlacer)
        board.remainingWordsList.remove(word)
        board.printBoard()
        print(f"Put {word} to {wordPlacer.id}")
        return True
    print(f"{word} could not be placed to {wordPlacer.id}")
    return False


currentPos = 0
while currentPos < len(board.placersList):
    currentPlacer = board.placersList[currentPos]
    print(f"Trying {currentPlacer.id}")
    isPlaced = False
    for word in board.getWordsOfLength(currentPlacer.length, []): #for all words of length = wordPlacer.length    
        if placeWord(currentPlacer, word):
            isPlaced = True
            currentPos = currentPlacer.id + 1
            break
            
    while not isPlaced: #none of the remaining words could be placed, need backtracking.
        excludedWords = []
        print(f"Nothing could be placed to placer: {currentPlacer.id}")
        for p in board.filledPlacers: print(p.id, end = ",")
        print("\n")
        lastWordPlacer = board.filledPlacers.pop() #get the last filled WordPlacer
        currentPos -= 1
        print(f"Backtracking to {lastWordPlacer.id} that had {lastWordPlacer.word}")
        excludedWords.append(lastWordPlacer.word)
        lastWordPlacer.word = None
        board.clearWordPlacer(lastWordPlacer)
        board.printBoard()
        for word in board.getWordsOfLength(lastWordPlacer.length, excludedWords):      
            if placeWord(lastWordPlacer, word): 
                isPlaced = True
                currentPos = lastWordPlacer.id + 1
                break
        #board.printBoard()"""
   
    


#board.fillWordPlacerWithWord(board.placersList[0], board.wordsList[0])
#board.printBoard()


