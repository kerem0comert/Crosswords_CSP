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
    WordPlacer(Square(0,0),Square(0,4)),
    WordPlacer(Square)
    ]
print(tabulate(table,tablefmt="grid"))