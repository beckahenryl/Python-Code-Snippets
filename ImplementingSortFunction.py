items = [4,1,2,12,98,58]

def min(items):
  temp = items[0]
  for items in items:
    if (item <= temp):
      temp = item
return temp


def sort(items):
  empty_list[]
  for i in range (0, len(items)):
    empty_list.append(min(items))
    items.remove(min(items))
return empty_list

print (sort(items))