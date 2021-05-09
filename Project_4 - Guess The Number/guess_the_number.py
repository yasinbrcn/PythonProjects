'''
Coded By: Yasin BİRCAN
Date:     09.05.2021
'''
import random
key=1
guess_number = 0
number_list = []
for i in range (1,51):
    number_list.append(i)
real_number = random.choice(number_list)

while key==1:
    user_choice = int(input("Please guess a number: ")) 
    guess_number = guess_number + 1 
    if user_choice > 50 or user_choice <=0: 
        print("Please guess a number between 1-50.")
        print("Your guess number has not increased.")
        guess_number = guess_number - 1
    elif user_choice == real_number: 
        print("Congratulations!")
        print('Guess Number: ' , guess_number )
        key=0
    elif user_choice > real_number:
        print("Wrong Guess")
        print("Hint: Down")
        key=1
    elif user_choice < real_number:
        print("Wrong Guess")
        print("Hint: Up")
        key=1

    
    
    
   
