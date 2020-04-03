# var = input("type a number: ")

# try:
#     print ("dividing it via a number "+ str(55/int(var)))
# except (ZeroDivisionError, ValueError) as e:
#     print ("Youre trying to divide by zero or you're entering negative numbers")

                ###### OR ######

def ask():
    check = input("How many eyes do you have? ")

    try:
        return print(int(check) == 2)
    except ValueError:
        print("type a number")

ask()
ask()