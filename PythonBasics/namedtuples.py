from collections import namedtuple
from math import sqrt

# a clear demonstration of the differences between namedtuple and standard 
# tuple

def ntuplevstuple():
    # a standard point in (x,y) coord in tuple
    pttuple1 = (25, -66)
    pttuple2 = (11, 19)

    # linear distance calculation
    line_length = sqrt((pttuple1[0]-pttuple2[0])**2 + (pttuple1[1]-pttuple2[1])**2)
    print(f"line length using a tuple --> {line_length}")


    # not quite a class but a subclass with no inherent functions
    # more readble, hence more pythonic
    Point = namedtuple("Point", ['x', 'y'])
    pnamedtuple1 = Point(25, -66)
    pnamedtuple2 = Point(11, 19)
    

    # standard indexing supported
    line_length_mod = sqrt((pnamedtuple1[0]-pnamedtuple2[0])**2 + (pnamedtuple1[1]-pnamedtuple2[1])**2)
    print(f"line length using a tuple --> {line_length_mod}")

    # supports unpacking as well
    x, y = pnamedtuple1
    print(f"point1 using namedtuple has xvalue of {x} and yvalue of {y}")

    print(type(Point))
    

def test():
    Card = namedtuple("Card", "suit rank".split())
    
    suits = "spades diamond clubs hearts".split()
    ranks = [str(n) for n in range(2, 11)] + "J Q K A".split() 
    _cards = [Card(var1 ,var2) for var1 in suits
                                for var2 in ranks]

    for card in _cards:
        print(card)

test()