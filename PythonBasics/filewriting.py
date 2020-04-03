def get_user(**user):
    return user

name = input("Whats your name: ")
age = input("Whats your age: ")
mobile_number = input("Enter your personal number: ")


user1 = get_user(name = name, age = age, phone = mobile_number)



for index,values in enumerate(user1.keys()):
    print("Info {} -->{}".format(index,user1[values]))


