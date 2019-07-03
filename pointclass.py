import math

class Point:
    # Class level attr
    co_ordinate_space = "Cartesian"

    # dunder method like this are called automatically by the interpreter 
    def __init__(self, x = 0, y = 0):
        self.y = y
        self.x = x
    # we saw that == operator is actually working with memory blocks and
    # not values to be compared with other objects
    # this dunder overrides the behaviour of == operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # overriden the dunder __repr__ to be printable and human readable
    # now you can use print(obj)
    def __repr__(self):
        return "Point ({},{})".format(self.x, self.y)

    # damn! now the print(obj) is working in tandem with __str__ and not __repr__
    def __str__(self):
        return "Point at ({},{})".format(self.x, self.y)

    def draw(self):
        print("Point object at co-ordinates -> {}, {}".format(self.x,self.y))

    def linear_distance(self, other):
        dist = math.sqrt((other.x- self.x)**2 + (other.y - self.y)**2) 
        print("Linear distance of ({},{}) and ({},{}) is {}".format(self.x,self.y,other.x,other.y,round(float(dist), 2)))


a =  Point()
# Instance level attributes, they are local to the object
a.data = "Hello world!"
print(a.data)
print(a.co_ordinate_space)
a.draw()
print(a)


b = Point(12,1)
# threw an error cause, .data was an instance attricbute for point obj 'a' not b
# but co_ordinate_space is shared between two since its a class atribute
# class attribute is public akin to JAVA, and changeable by default anywhere via
# Class reference 
# print(b.data)
print(b.co_ordinate_space)
b.draw()



## comparing objects
c = Point()
a.draw()
c.draw()
c = a
# this operator generally checks if the objects point at the same memory location
# if its same then true and vice-versa
# this is also why creating a new point object with exact same value doesnt help
# this statement making true since they are different memory blocks
print(a == c)

d = Point(5,5)
print(b == d)

# class based inplace fnction to calculate the linear distance between two points
b.linear_distance(a)
