'''
Coded By: Yasin BİRCAN
Date:     08.05.2021
'''
key=1
while key == 1:
    number = input("Please enter a number:")
    try:
        number = int(number)
        if(number%2 == 0):
            print("Number is a even.")
        else:
            print("Number is a odd.")
        key=0
    except:
        try:
            number = float(number)
            print("Please enter a integer number.")
        except:
            print("Please enter number only.")
