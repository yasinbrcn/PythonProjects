'''
Coded By: Yasin BİRCAN
Date:     09.05.2021
'''
word = str(input("Please enter a word: "))
key1 = 1
key2 = 1
character_list = []
i=1
j=1
for i in range(len(word)):
    character_list.insert(i,word[i:j])
    j=j+1

if len(word)%2 == 0:
    y = len(word)
    y2 = y-1
    y3 = 0

    while key1 == 1:
        if character_list[y2] == character_list[y3]:
             y2 = y2-1
             y3 = y3+1
             if y3 > y2:
                key1=1
             else:
                print("Palidrome")
                key1=0
        elif character_list[y2] != character_list[y3]:
            print("Not Palidrome")
            key1=0
else:
    n = len(word)
    n2 = n-1
    n3 = 0
    n4 = int((n/2)+1)

    while key2 == 1:
        
        if character_list[n2] == character_list[n3]:
            n2 = n2-1
            n3 = n3+1
            if n3 != n4-1:
                key2=1
            else:
                print("Palidrome")
                key2=0
        elif character_list[n2] != character_list[n3]:
            print("Not Palidrome")
            key2=0
