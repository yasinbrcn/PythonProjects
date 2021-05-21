'''
Coded By: Yasin BİRCAN
Date:     11.05.2021
'''

key=1
mail_list = []
username_list = []
domain_list = []
com_list = []

def listString(s):
    string = ""
    for n in s: 
        string += n  
    return string

def checkEmail(e):
    j=1
    for i in range(len(e)):
        mail_list.insert(i,e[i:j])
        j=j+1

    try:
        mail_list.index("@")!=0
        check = 1
    except:
        mail_list.clear()
        username_list.clear()
        domain_list.clear
        com_list.clear()
        check = 0
    return check

def checkCom():
    com = ""
    try:
        for k in range(mail_list.index("@")):
            username_list.append(mail_list[k])

        for m in range(mail_list.index("@")+1,len(mail_list)):
            domain_list.append(mail_list[m])
            
        for n in range (domain_list.index("."),len(domain_list)):
            com_list.append(domain_list[n])
            com = str(listString(com_list))
    except:
        mail_list.clear()
        username_list.clear()
        domain_list.clear()
        com_list.clear()
    if com == ".com" and domain_list.index(".") != 0:
        checkcom = 1
    else:
        mail_list.clear()
        username_list.clear()
        domain_list.clear()
        com_list.clear()
        checkcom = 0
    return checkcom

while key == 1:
    email = str(input("What is your email address?: "))
    if checkEmail(email) == 1 and checkCom() == 1 and listString(username_list) != "":
        key=0
    else:
        print("Invalid email address. Please enter a valid email address.")
        mail_list.clear()
        username_list.clear()
        domain_list.clear()
        com_list.clear()
        key=1
        
print("Hello {}! Your domain adres: {}".format(listString(username_list),listString(domain_list)))
