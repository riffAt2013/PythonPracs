## Tutorial On Deque: Double Ended Queue
## This supports not only operations on the front of the structure
## but also the back end. Hence obfuscating stacks and queues. For
## High Performance, list is out of the Question
from collections import deque


"""Creation of the deque as well
as basic methods
"""
def part01():
    # main param is an iterable like 'string'
    data = deque('abcdefg')
    print(type(data), data)

    # deque supports normal indexing and __len__() hence not confusing in any ways
    # for the beginners
    print('Lenght of the Deque:', len(data))
    print('Left end:', data[0])
    print('Right end:', data[-1])

    # removing data
    data.remove('c')
    print('after removing "c" --> ',data)


"""Adding Data from left and right in 
deque
"""
def part02():

    ## blank deques creatiion, with adding from the right operations
    data1 = deque()
    data1.extend('123456')
    print(data1)

    data1.append('A')
    print("'A', added to the right",data1)

    # notice the extendleft(), it ranges over 0,10 but essentially not going in
    # from the right. last of the range i.e: excluded 10 = 9 is the first elem in the struct
    data2 = deque()
    data2.extendleft(range(10))
    print(data2)
    # appendleft is a mirror to append above, i.e: takes a whole input not an iterable
    data2.appendleft('SAX')
    
    print("S added from the left", data2)

    


"""Data subtraction from left and right
with some software engineering discipline
"""
def part03():
    data = deque('abcde')
    print(data)
    print("Consumed from the right:")

    while True:
        try:
            # popped from the right, retval is single item
            print(data.pop(), end='\t')
        except IndexError:
            break
    
    print()
    data = deque('1234567')
    print(data)
    print("Consumed from the left:")

    while True:
        try:
            print(data.popleft(), end='\t')
        except IndexError:
            break

"""rotating is a very powerful aspect of deque
it supports both left and right rotation
"""
def part04():
    data1 = deque(range(9))
    print("Normal deque: ", data1)
    
    # rotate with a positive int makes a right rotation
    # imagine dialling an old school telephone.
    # 3 of the final elements are moved to the left.
    # rotate function is inplace
    data1.rotate(3)
    print("Rotated right: ", data1)


    data2 = deque(range(9))
    # negative int makes a left rotation
    #  3 values from the left makes a transition leftward
    # and takes place of the right most values 
    data2.rotate(-3)
    print("rotated left: ", data2)



# the most powerful part to me is the maxlen prop
# it allows for C-array like capabilty to contain a fixed
# amount of numbers
def part05():
    data = deque(maxlen=5)
    for i in range(50):
        # even if appending 50 numbers to the deque
        # it only have size of 5, hence the final five is added only 
        # the other elements are ommitted
        data.append(i)

    print(data)