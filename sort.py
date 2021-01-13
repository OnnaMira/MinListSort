
def sort_list_min(list):
    minL = list[0]
    i = 0
    while (i< len(list)):
        minI= list.index(min(list[i:len(list)]))
        minV = min(list[i:len(list)])
        list[minI] = list[i]
        list[i]=minV
        i +=1 
    return list
    
        
print("\n------------Initial List------------")
lise = [-1, 5, 15 ,0 ,14,-6]
print(lise)
print("\n------------Sorted List------------")
print(sort_list_min(lise))