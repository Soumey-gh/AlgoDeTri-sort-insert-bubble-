print('Algo de tri')

#Variable
def algoTri1 ():
    i = 0
    tab_list = [8,7,6,5,4,3,2,1,0]
    for i in range (0,len(tab_list)):
        j= i
        for j in range (0,len(tab_list)):
            if (tab_list[j] >  tab_list [i]) :
                tab_list[j], tab_list[i] = tab_list[i], tab_list[j]

    return tab_list
print(algoTri1())










