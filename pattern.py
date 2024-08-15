x = int(input("Enter the number: "))
print('Entered nuber is: ', x)
print("\n")
flag = False
index = 0
for i in range(x):
    for j in range(index):
        print(" ")
    print("*")
    if index == 2:
        flag = True
    elif index == 0:
        flag = False
    if flag:
        index -= 1
    else:
        index += 1











 