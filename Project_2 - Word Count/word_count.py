'''
Coded By: Yasin BİRCAN
Date:     08.05.2021
'''
word = input("Please enter the sentence:")
try:
    word = int(word)
    print("Please do not enter number.")
except:
    try:
        word = float(word)
        print("Please do not enter number.")
    except:
        word=word.strip()
        wordlist=[]
        j=1
        for i in range(len(word)):
            wordlist.insert(i,word[i:j])
            j=j+1
print("Character Count: " + str(len(word) - wordlist.count(" ")))
if wordlist.count(" ") == 0:
    print("Word Count: " + str(wordlist.count(" ")))
else:
    print("Word Count: " + str(wordlist.count(" ")+1))
