from tabulate import tabulate
from Square import Square
from WordPlacer import WordPlacer

board = [
    ["","","","",""],
    ["*","*","","*",""],
    ["*","","","",""],
    ["","*","","",""],
    ["","","","","",""],
    ["","*","*","","*"] 
    ]

wordList = ["aft","ale","eel","heel","hike","hoses","keel","knot","laser","lee","line","line","sails",
            "sheet","steer","tie"]

"""Construct the list of placers in the given puzzle. An alternative way to keep the WordPlacers would
involve only keeping its start square and keeping whether it is horizontal or vertical. That information
would also be enough as a WordPlacer will continue until encountering a "*" obstacle or the end of the board.
However, this approach would involve for constantly checking if a WordPlacer encounters a "*" in its path.
As such, I keep the end point square for simplicity as well. By keeping this extra data, I don't need
to calculate for obstacles each time."""
placers = [
    WordPlacer(1,Square(0,0),Square(0,4)),
    WordPlacer(2,Square(0,2),Square(4,2)),
    WordPlacer(3,Square(0,4),Square(4,4)),
    WordPlacer(4,Square(2,1),Square(2,4)),
    WordPlacer(5,Square(2,3),Square(5,3)),
    WordPlacer(6,Square(3,0),Square(5,0)),
    WordPlacer(7,Square(3,2),Square(3,4)),
    WordPlacer(8,Square(4,0),Square(4,4))
    ]
print(tabulate(board,tablefmt="grid"))