import random
j=1
key=1
guess_4 = 3
guess_5 = 4
chosen_word_list = []
find_letter_list = []
line_list_4 = ["_ ","_ ","_ ","_ "]
line_list_5 = ["_ ","_ ","_ ","_ ","_ "]

def listString(s):
    string = ""
    for n in s: 
        string += n  
    return string

word_list = ["able","baby","city","heart","world","angel"]
chosen_word = random.choice(word_list)
chosen_word_lenght = len(chosen_word)

if chosen_word_lenght == 4:
    print("You have four guesses.")
    line_list_4[0] = chosen_word[0]
    print(listString(line_list_4))
else:
    print("You have five guesses.")
    line_list_5[0] = chosen_word[0]
    print(listString(line_list_5))

while key == 1:
    user_letter = input("Please enter a letter: ")
    
    if chosen_word_lenght == 4:
        
        for k in range(chosen_word_lenght):
            if chosen_word[k] == user_letter:
                line_list_4[k] = user_letter
                
        print(listString(line_list_4))
        if guess_4 != 0 and line_list_4.count("_ ") != 0:
            guess_4 = guess_4 - 1
            key = 1
        elif line_list_4.count("_ ") == 0:
            print("Correct...")
            key = 0
        elif guess_4 == 0:
            print("Word is: " + chosen_word)
            key = 0
        
    elif chosen_word_lenght == 5:

        for k in range(chosen_word_lenght):
            if chosen_word[k] == user_letter:
                line_list_5[k] = user_letter
                
        print(listString(line_list_5))
        if guess_5 != 0 and line_list_5.count("_ ") != 0:
            guess_5 = guess_5 - 1
            key = 1
        elif line_list_5.count("_ ") == 0:
            print("Correct...")
            key = 0
        elif guess_5 == 0:
            print("Word is: " + chosen_word)
            key = 0
