print('Algo de tri')

#Sorting Algorithm
def algoSort ():
    i = 0
    tab_list = [8,7,6,5,4,3,2,1,0]
    for i in range (0,len(tab_list)):
        j= i
        for j in range (0,len(tab_list)):
            if (tab_list[j] >  tab_list [i]) :
                tab_list[j], tab_list[i] = tab_list[i], tab_list[j]

    return tab_list
print(algoSort())

#Insert Algorithm

def algoInsert ():
    T = [9,8,7,6,5,4,3,2,1,0]
    for i in range(1, len(9)):
        moove = T[i]
        j = i
        while (j >=0 and T[j-1] >moove) :
            T[j] = T[j-1]
            j = j-1
            T[j] = moove
    return T
print(algoInsert())









