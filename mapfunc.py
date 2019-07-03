items = [
    ["Gucci", 2999],
    ["Louis Vuitton", 3555],
    ["Balenciaga", 2855]
]

# naive approach of extracting the ints from the items list

naive_price = []
for item in items:
    naive_price.append(item[1])

print(naive_price)


# using map function to map one iterable to another
# map uses 2 args, first one is a function for processing stuffs
# a lambda function is preferable since we're not reusing it anywhere else
# 2nd arg is defintiely the iterable
# map() returns map object which is not an iterable, use list()
# or tuple() to get one
mapped_list = map(lambda x:x[1], items)
mapped_list = list(mapped_list)
print("Map version", mapped_list)
