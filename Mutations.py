'''
indexes

Read a given string, change the character
at a given index and then print the modified 
string.
'''

string = input()
li = list (string)
user_index = input().split()
#exceptions function converts the 5 to int
#it leaves the k as is
def exceptions (user_index):
	try:
		return int(user_index)
	except (ValueError, TypeError):
		return user_index

the_list = [exceptions(i) for i in user_index]
		
#main function to make the changes
def do_strings (the_list, li):
	for j in li:
		li[the_list[0]] = the_list[1]
		make_join = ''.join(li)
	return make_join 

print (do_strings(the_list, li))