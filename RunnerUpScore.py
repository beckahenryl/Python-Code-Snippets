run = int(input())
arry = input()
spliti = [int (x) for x in arry.split()]

def set_of_runner_ups (run, spliti):
	create_set = set (spliti) 		     #create set to get no duplicates
	create_set.remove(max(create_set)) #remove max in set
	new_set_max = max(create_set)      #find new max in new set
	return new_set_max			           #return new max runner up

print (set_of_runner_ups(run, spliti))