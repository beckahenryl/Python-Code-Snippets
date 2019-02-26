from collections import Counter
num_words = int (input())
list_creation = []
for i in range (0, num_words):
    get_words = input()
    list_creation.append(get_words)
def distinctions (list_creation):    
    setting = set(list_creation) #distinct
    find_len = len (setting) #3-final result

    make_counter = Counter(list_creation)
    list_for_counters = [] #hold all other appearances final result
    for j in make_counter:
        list_for_counters.append(make_counter[j])
    make_sort = sorted(list_for_counters)
    append_reversed = []
    for l in reversed (make_sort):
        append_reversed.append(l)
    str_of_len_set = str (find_len)
    str_of_counter = str (append_reversed).replace ('[', '').replace (']', '').replace (',', '')   
    print (str_of_len_set + '\n' + str_of_counter)
    return ''
print (distinctions(list_creation))    
