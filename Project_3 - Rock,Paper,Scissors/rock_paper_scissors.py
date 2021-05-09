'''
Coded By: Yasin BİRCAN
Date:     08.05.2021
'''
import random
user_score = 0
pc_score = 0

for i in range(5):

    user_choice = str(input("Please select --> [1]:Rock , [2]:Paper , [3]:Scissors"))
    if user_choice == "1":
        user_choice = "Rock"
    elif user_choice == "2":
        user_choice = "Paper"
    elif user_choice == "3":
        user_choice = "Scissors"
    print("You Choice: " + user_choice)

    pc_choice_list=["Rock","Paper","Scissors"]
    pc_choice = random.choice(pc_choice_list)
    print("PC Choice: " + pc_choice)
    if user_choice == pc_choice:
        print("Scoreless")
        user_score = user_score
        pc_score = pc_score
        print("You Score: " + str(user_score))
        print("PC Score: " + str(pc_score))
    elif user_choice == "Rock" and pc_choice == "Paper":
        print("PC Win")
        user_score = user_score
        pc_score = pc_score + 1
        print("You Score: " + str(user_score))
        print("PC Score: " + str(pc_score))
    elif user_choice == "Rock" and pc_choice == "Scissors":
        print("You Win")
        user_score = user_score+1
        pc_score = pc_score
        print("You Score: " + str(user_score))
        print("PC Score: " + str(pc_score))
    elif user_choice == "Paper" and pc_choice == "Rock":
        print("You Win")
        user_score = user_score+1
        pc_score = pc_score
        print("You Score: " + str(user_score))
        print("PC Score: " + str(pc_score))
    elif user_choice == "Paper" and pc_choice == "Scissors":
        print("PC Win")
        user_score = user_score
        pc_score = pc_score+1
        print("You Score: " + str(user_score))
        print("PC Score: " + str(pc_score))
    elif user_choice == "Scissors" and pc_choice == "Rock":
        print("PC Win")
        user_score = user_score
        pc_score = pc_score+1
        print("You Score: " + str(user_score))
        print("PC Score: " + str(pc_score))
    elif user_choice == "Scissors" and pc_choice == "Paper":
        print("You Win")
        user_score = user_score+1
        pc_score = pc_score
        print("You Score: " + str(user_score))
        print("PC Score: " + str(pc_score))
if user_score == pc_score:
    print("Final: Scoreless!")
elif user_score > pc_score:
    print("Final: You Win!")
elif user_score < pc_score:
    print("Final: PC Win!")
