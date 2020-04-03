# a demonstration of classmethods and how they differ from regular methods

class Car:

    category = ["Hypercar", "Sportscar", "Familycar"]
    def __init__(self, year, first, last):
        self.year = year
        self.first = first
        self.last = last

    # regular mathods take one must-take args as "self"
    def getInfo(self):
        print("{} {} from the year {}".format(self.first, self.last, self.year))


    # thats how a classmethod is different from regular methods
    # first it is decorator-ized with "classmethod"
    # second it takes a must-take arg in the form of cls
    # by this we can change the class level attribute values
    @classmethod
    def category_inclusion (cls, categoryname):
        if categoryname in cls.category:
            print("Error: name Already there bud!")
        else:
            cls.category.append(categoryname) 

    # best usage of class methods are for alternative constructors
    @classmethod
    def fromstring(cls, string):
        year, first, last = string.split('-')
        return cls(year, first, last)

    # a third kind of method. not regular, not class, hence doesn't auto-pass
    # self or cls. it is just like normal function with some logical connections
    # to the class, hence the inclusion here in the class
    @staticmethod
    def isBefore1996(year):
        if int(year) < 1996:
            return True
        return False


car1 = Car(1996, "Bugatti", "Veyron")

# the following shows the namespace or the properties of the instance
# which are year, first and last only. not the category
print(car1.__dict__)

# by default the instance can have the access to the class level stuff
# but it cant change it, whenever it tries to do it, it becomes its
# own instance level attribute, the OG remains unchanged
car1.category = ["japanese bomb"]
print(car1.category)
car2 = Car(1950,"Volkswagen", "Beetle")
print(car2.category)

# the only way to access class level attribute is via the class level
# methods
Car.category_inclusion("Familycar")
print(Car.category)

# instance can also access the classmethods which seems strange
car2.category_inclusion("DeeJay")
print(car2.category)
print(Car.category)


# best usage of class methods are for alternative constructors
string = "1885-Marcedes-Velo"
car3 = Car.fromstring(string)
print(car3.getInfo())

# static method also deosn't care who is calling it
print(car3.isBefore1996(car3.year))