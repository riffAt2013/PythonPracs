# enum is for DIY type with iteration and comparison
# capabilities. It can be used to create well defined
# symbols for values

from sys import exc_info  # general error catch
from enum import Enum


class Status(Enum):

    # add class level attribute to work
    ALIVE = 0
    DEAD = 1
    INFECTED = 2


# creation of enumerated class and basic name-value attributing
def part1():
    # subclass Enum from enum to work and basically
    # making it an enumertaed class

    print("Member Name:", Status.ALIVE.name)
    print("Member Name:", Status.ALIVE.value)

    # enumerated classess can be iterated
    for status in Status:
        print(f"{status.name} has a status value of {status.value}")

    status1 = Status.ALIVE
    status2 = Status.DEAD

    # enums can be compared using eqlty and idtty
    print("Using equality operation: ", status1 ==
          status2, status1 == Status.ALIVE)

    print("Using Identity opertaion: ",
          status1 is status2, status1 is Status.ALIVE)

    # trying to order them is invain, use IntEnum to make the enum
    # behave like numbers
    try:
        print(X.value for X in sorted(Status))
    except:
        print(f"Can sort Status because {exc_info()[0]}")


part1()
