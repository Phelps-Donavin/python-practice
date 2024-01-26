import numpy as np, os

user_choice = True #Changes depending on user input to continue
rng = np.random.default_rng
while user_choice == True:
    print("Hello, welcome to the Number Guessing game!\n")
    print("Would you like to play? (Y/N)\n")

    user_choice = input()

    if user_choice == True:
        randomNumber = rng.random()
        print("Alright, lets begin!")
        ##Game Function Call
    else:
        os.system('clear')
        print("Goodbye!")
        break
    
print("Thanks for playing!")