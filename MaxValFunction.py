#create a maximum val function
lis_ted = [4,20,56,25,29,40,70,76,89,1000,10001]

def max_cal_func(lis_ted):
    for i in range(0, len(lis_ted)):
        temp = lis_ted[0]
        if temp < lis_ted[i]:
            temp = lis_ted[i]
    return temp
        
print (max_cal_func(lis_ted)) 