from itertools import permutations
permi = input().split()
do_int = int(permi[1])
hold = str (do_int)
int_1 = int(hold)
first = permi[0]
hold_2 = str(first)
make_sort = ''.join(sorted(hold_2))
li = list(permutations(make_sort, int_1))
change = str (li).replace("'", "").replace('[', '').replace(']', '').replace(' ', '').replace(',', '').replace(')', '\n').replace('(', '')
print (change)