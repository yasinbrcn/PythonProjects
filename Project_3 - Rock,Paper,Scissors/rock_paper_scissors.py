'''
Coded By: Yasin BİRCAN
Date:     08.05.2021
'''
import random
import keyboard

print("Please select --> [1]:Rock , [2]:Paper , [3]:Scissors")
if keyboard.read_key() == "1":
    user_choice = "Rock"
    #print("You pressed 1")
elif keyboard.read_key() == "2":
    user_choice = "Paper"
    #print("You pressed 2")
elif keyboard.on_press_key("3", lambda _:print("You pressed 3")):
    user_choice = "Scissors"
    #print("You pressed 3")
print("You Choice: " + user_choice)

pc_choice_list=["Rock","Paper","Scissors"]
pc_choice = random.choice(pc_choice_list)
print("PC Choice: " + pc_choice)
if user_choice == pc_choice:
    print("Scoreless")
elif user_choice == "Rock" and pc_choice == "Paper":
    print("PC Win")
elif user_choice == "Rock" and pc_choice == "Scissors":
    print("You Win")
elif user_choice == "Paper" and pc_choice == "Rock":
    print("You Win")
elif user_choice == "Paper" and pc_choice == "Scissors":
    print("PC Win")
elif user_choice == "Scissors" and pc_choice == "Rock":
    print("PC Win")
elif user_choice == "Scissors" and pc_choice == "Paper":
    print("You Win")



   
    
            

