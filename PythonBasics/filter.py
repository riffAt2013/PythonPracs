items = [
    ("p1", 12),
    ("p2", 9),
    ("p3", 11),
    ("p4", 2)
]


## filter takes a predicate to work properly, map cant work with it
## hence the different result we saw
# ('p2', 9)
# ('p4', 2)
# False
# True
# False
# True

filter_iter = filter(lambda x: x[1]<10, items)
map_iter = map(lambda x: x[1]<10, items)

for x in filter_iter:
    print(x)

for x in map_iter:
    print(x)


# comprehension format for filter()
filtered = [x for x in items if x[1]<10]
print(filtered)

# comprehension format for map
mapped = [x[1] for x in items]
print(mapped)


price = [x[1] for x in items if x[1]<10]
print(price)