#add items to list and then sort from largest to smallest number. Shout out to AR
items = [4,1,2,12,98,58]  
#user to add items to list
def user_input (items):
    user_in = (int(input("Enter an integer: ")))
    items.append(user_in)
    return items
#sort function with AR
def sort(items):
    empty_list = []
    for i in range (0, len(items)):
        empty_list.append(max(items))
        items.remove(max(items))
    return empty_list
#print results
print (sort(items))   