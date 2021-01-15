from Square import Square

HORIZONTAL = "horizontal"
VERTICAL = "vertical"

class WordPlacer:
    def __init__(self, id: int, start: Square, end: Square):
        self.id = id
        self.start = start
        self.end = end
        self.length = self.getLength()
        self.word = None #no word is placed initially
        self.excludedWords = set()
        
    def getLength(self):
        if self.start.row == self.end.row: 
            self.orientation = HORIZONTAL
            return self.end.column - self.start.column + 1
        else: 
            self.orientation = VERTICAL
            return self.end.row - self.start.row + 1