#sorted through the list in order

list = [4,5,6,7,8,1,2,3]
list.sort()
print (list)

#created an empty list, got user input and added it to the empty list then sorted it
userlist = []

user_1 = int (input('Enter Number 1: '))
user_2 = int (input('Enter Number 2: '))
user_3 = int (input('Enter Number 3: '))
user_4 = int (input('Enter Number 4: '))
user_5 = int (input('Enter Number 6: '))

userlist.append(user_1)
userlist.append(user_2)
userlist.append(user_3)
userlist.append(user_4)
userlist.append(user_5)

userlist.sort()
print (userlist)