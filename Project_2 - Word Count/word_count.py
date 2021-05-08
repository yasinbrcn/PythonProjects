'''
Coded By: Yasin BİRCAN
Date:     08.05.2021
'''
name = str(input("Please Enter a Word:"))
namelist=[]
j=1
for i in range(len(name)):
    namelist.insert(i,name[i:j])
    j=j+1
print("Character Count: " + str(len(name) - namelist.count(" ")))
print("Word Count: " + str(namelist.count(" ")+1))
