j=1
mail_list = []
username_list = []
domain_list = []
def listString(s):
    string = ""
    for n in s: 
        string += n  
    return string
email = str(input("What is your email address?: "))
for i in range(len(email)):
    mail_list.insert(i,email[i:j])
    j=j+1

for k in range(mail_list.index("@")):
    username_list.append(mail_list[k])

for m in range(mail_list.index("@")+1,len(mail_list)):
    domain_list.append(mail_list[m])
    
print("Hello {}. Your domain adres: {}".format(listString(username_list),listString(domain_list)))
