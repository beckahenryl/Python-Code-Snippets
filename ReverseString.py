string_to_be_reversed =input() #got input
def FirstReverse(string_to_be_reversed):
    str_ing_return = ''.join(list(reversed(string_to_be_reversed))) #created list then converted to string
    return(str_ing_return) #returned new string
print (FirstReverse(string_to_be_reversed)) #called function