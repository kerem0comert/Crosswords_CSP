from Point import Point

class WordPlacer:
    def __init__(self, id: int, start: Point, end: Point):
        self.id = id
        self.start = start
        self.end = end
        
    def getLength(self):
        #First check whether it is horizontal or vertical
        if(self.start.row == self.end.row): 
            return self.start.column - self.end.column
        else: return self.start.row - self.end.row