#sorting characters in a string


string = str(input())

def alphabet_soup (string):
	create_list = string
	get = list (create_list)
	get.sort()
	join = ''.join(get)
	return join
print (alphabet_soup(string))