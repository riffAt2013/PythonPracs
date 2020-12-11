import time
import random

my_guess = 9
low = 1
high = 10


while True:
    
    computers_guess = random.randint(low, high)
    time.sleep(2)
    print(f"Computer: Is it {computers_guess}?")

    if computers_guess < my_guess:
        print("Me: Too Low AI!")
        low = computers_guess + 1

    elif computers_guess > my_guess:
        print("Me: Too high! AI!")
        high = computers_guess - 1
    
    else:
        print("Me: Correctamundo!")
        break

