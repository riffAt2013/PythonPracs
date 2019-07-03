# try:
#     var = input("Give a number: ")
#     print(int(var)/0)
# except (ZeroDivisionError, ValueError) as error:  #we can store the error info as a var
#     print(error)
# else:       #only executed when no exception found for the block.
#     print("No exception found for the block")
# print("Hey its working still")



# try:
#     file = open("exception.py")
# except FileNotFoundError as error:
#     print(error)
# else:
#     print("No exceptions found")
# finally:
#     file.close()
#     print("Used for releasing external resources")



# try:
#     # with statement autometically releases external resources
#     # no need for flie.close to use on finally block
#     # with can only be used when object has __enter__ and __exit__
#     with open("exception.py") as file:
#         print("Do whatever you want to do")
# except FileNotFoundError:
#     print("Check check")



## raising custom exceptions


def check(age):
    if age <= 0:
        raise ValueError("Wrong shit")
    return 50/age

try:
    print(check(-10))
except ValueError:
    print("Erro handlkes")
