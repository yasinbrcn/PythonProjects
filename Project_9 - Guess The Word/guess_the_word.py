import random
j=1
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
#chosen_word = "baby"
#for i in range(len(chosen_word)):
#    chosen_word_list.insert(i,chosen_word[i:j])
#    j=j+1
    
user_letter = input("Please enter a letter: ")

print(chosen_word)
#print(chosen_word_list)
#print(chosen_word_list.index(user_letter))
'''
for k in range(chosen_word_lenght):
    if chosen_word[k] == user_letter and chosen_word_lenght == 4:
        #print(str(k)+ ". eleman " + user_letter + " a eşittir.")
        line_list_4[k] = user_letter
        #print(listString(line_list_4))
    elif chosen_word[k] == user_letter and chosen_word_lenght == 5:
        line_list_5[k] = user_letter
        #print(listString(line_list_5))
    else:
        print(listString(line_list_4))
    

#print(line_list.index("b"))
'''
'''
for k in range(chosen_word_lenght):
    if chosen_word[k] == user_letter:
        find_letter_list.append(k)
    else:
        find_letter_list = find_letter_list

print(find_letter_list)
print(len(find_letter_list))

'''
        
if chosen_word_lenght == 4:
    for k in range(chosen_word_lenght):
        if chosen_word[k] == user_letter:
            line_list_4[k] = user_letter
    print(listString(line_list_4))

elif chosen_word_lenght == 5:
    for k in range(chosen_word_lenght):
        if chosen_word[k] == user_letter:
            line_list_5[k] = user_letter
    print(listString(line_list_5))

    
