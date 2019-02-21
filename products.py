import itertools

input1 = input().split()
input2 = input().split()

def productItertools (input1, input2):
    a = [int(i) for i in input1]
    b = [int(j) for j in input2]
    listItertools = []
    for i in itertools.product(a,b):
        listItertools.append(i)
    converToString = [str(i) for i in listItertools]  
    makeChange = ' '.join(converToString)

    return makeChange

print (productItertools(input1, input2))