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
    

def part01():
    # named tuples are immutable just like tuples
    person = namedtuple("person",  "name age")
    pat = person(name = "Pat", age = "21" )

    try:
        pat.age = str(22)
    except AttributeError as attr:
        print(attr)


    # named typle cant have python keyword as attribute name, nor repeating words
    try:
        namedtuple("person", "try person age")
    except ValueError as identifier:
        print(identifier)




def part02():
    
    class Vector():
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __add__(self, other):
            return Vector(self.x+other.x, self.y+ other.y)

        def __repr__(self):
                return f"Vector({self.x},{self.y})"
                
    s = Vector(2, 3)
    d = Vector(3, 4)
    print(s+d)
            
part02()