lis_ted = [1,9,25]

def mini_val_func (lis_ted):
    for i in lis_ted:
        temporary_val = lis_ted[0]
        if (temporary_val > lis_ted[i]):
            temporary_val = lis_ted[i]
        return temporary_val
print (mini_val_func(lis_ted))    