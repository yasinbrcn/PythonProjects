'''
Coded By: Yasin BİRCAN
Date:     14.05.2021
'''

import random
key_word = 1
key_number = 1
key_char = 1
word_list = []
number_list = []
char_list = []

def listString(s):
    string = ""
    for n in s: 
        string += n  
    return string

def checkWord(r_word):
    try:
        r_word = int(r_word)
        print("Please enter word only. Not integer value.")
        r_word_check = 1
    except:
        try:
            r_word = float(r_word)
            print("Please enter word only. Not float value.")
            r_word_check = 1
        except:
            if len(r_word) >= 6:
                r_word_check = 0
            else:
                print("Please enter more than 5 letters.")
                r_word_check = 1
    return r_word_check

def checkNumber(r_number):
    try:
        if len(r_number) >=6:
            r_number = int(r_number)
            r_number_check = 0
        elif len(r_number) < 6:
            print("Please enter more than 5 digits.")
            r_number_check = 1
    except:
        try:
            r_number = float(r_number)
            print("Please enter integer value only. Not float value.")
            r_number_check = 1
        except:
            print("Please enter integer value only. Not string value.")
            r_number_check = 1
    return r_number_check

def checkCharacter(r_char):
    valid_chars = '!#$%&*+,-./:;<=>?@[\]_{|}'
    if len(r_char) != 1:
        print("Please enter one character.")
        r_char_check = 1
    elif r_char not in valid_chars:
        print("Please enter special character only from list.")
        print("!#$%&*+,-./:;<=>?@[\]_{|}")
        r_char_check = 1
    else:
        r_char_check = 0
    return r_char_check

def showPassword(r_word,r_number,r_char):
    i=1
    j=1
    for w in range(len(r_word)):
        word_list.insert(w,r_word[w:i])
        i=i+1
    chosen_letters = random.choices(word_list,k=3)
    string_letters = listString(chosen_letters)
    
    for n in range(len(r_number)):
        number_list.insert(n,r_number[n:j])
        j=j+1
    chosen_digits = random.choices(number_list,k=3)
    string_digits = listString(chosen_digits)
    password = string_letters + string_digits + r_char
    print("Your password: " + password)
    
while key_word == 1:
    word = input("Please enter the word (Min. 6 character): ")
    key_word = checkWord(word)
while key_number == 1:
    number = input("Please enter the number: ")
    key_number = checkNumber(number)
while key_char == 1:
    char = input("Please enter the special character: ")
    key_char = checkCharacter(char)

print("Chosen word: " + word)
print("Chosen number: " + str(number))
print("Chosen special character: " + str(char))
showPassword(word,number,char)
