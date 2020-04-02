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

part03()