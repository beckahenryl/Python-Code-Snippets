from itertools import combinations
permi = input().split()
do_int = int(permi[1])
hold = str (do_int)
int_1 = int(hold)
first = permi[0]
hold_2 = str(first)
make_sort = ''.join(sorted(hold_2))
c = [comb for i in range (int_1) for comb in combinations (make_sort, i+1)]
change = str (c).replace("'", "").replace('[', '').replace(']', '').replace(' ', '').replace(',', '').replace(')', '\n').replace('(', '')
print (change)