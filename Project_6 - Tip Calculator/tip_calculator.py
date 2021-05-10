staff_name_list = []
staff_point_list = []
staff_number=0
key=1
key2=1
key3=1
key4=1
i=0
j=-1
point_total=0
k=0
while key==1:
    try:
        staff_number = int(input("Please enter the number of staff: "))
        key=0
    except:
        print("Please enter a correct value!")
        key=1

while key2==1:
    i=i+1
    name = input("Please enter the " +str(i)+ ". staff name: ")
    try:
        name = int(name)
        print("Please enter a correct value!")
        staff_name_list.clear()
        print("All names deleted!")
        i=0
        #if i!=1:
            #i=i-1
        #else:
            #i=0
        key2=1
    except:
        #print("correct value!")
        staff_name_list.append(name)
        if i!=staff_number:
            key2=1
        else:
            key2=0
print("Staff List: ")
print(staff_name_list)

while key3==1:
    j=j+1
    point = input("Please enter the point " +staff_name_list[j]+ "'s: ")
    try:
        point = int(point)
        #print("correct value!")
        staff_point_list.append(point)
        point_total = point_total + point
        if j!=staff_number-1:
            key3=1
        else:
            key3=0
    except:
        print("Please enter a correct value!")
        staff_point_list.clear()
        point_total = 0
        print("All points deleted!")
        j=-1
        key3=1
print("Point List: ")
print(staff_point_list)

while key4==1:
    try:
        total_tip_value = int(input("Please enter the total tip : "))
        key4=0
    except:
        print("Please enter a correct value!")
        key4=1
print("Total Tip: ")
print(total_tip_value)
#print("Total Point: ")
#print(point_total)
point_tip = total_tip_value / point_total
for k in range(staff_number):
    print(staff_name_list[k] + "'nın alacağı tip: " + str(float(point_tip*staff_point_list[k])))
