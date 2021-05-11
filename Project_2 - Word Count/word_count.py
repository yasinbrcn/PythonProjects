'''
Coded By: Yasin BİRCAN
Date:     08.05.2021
'''
word = str(input("Please Enter The Word:"))
wordlist=[]
j=1
for i in range(len(word)):
    wordlist.insert(i,word[i:j])
    j=j+1
print("Character Count: " + str(len(word) - wordlist.count(" ")))
print("Word Count: " + str(wordlist.count(" ")+1))
