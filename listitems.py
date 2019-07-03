lists = [1,2,3,4,5]

try:
    print(lists.index(6))
except ValueError:
    print("Not in lists")


if 6 in lists:
    print("THere there")
else:
    print("Not there")