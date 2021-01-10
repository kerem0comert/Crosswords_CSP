from Square import Square

class WordPlacer:
    def __init__(self, id: int, start: Square, end: Square):
        self.id = id
        self.start = start
        self.end = end
        self.length = self.getLength()
        
    def getLength(self):
        #First check whether it is horizontal or vertical
        if(self.start.row == self.end.row): 
            return self.end.column - self.start.column + 1
        else: return self.end.row - self.start.row + 1