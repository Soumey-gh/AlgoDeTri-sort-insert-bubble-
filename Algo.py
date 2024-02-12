print('Algo de tri')


# Insert Algorithm
def insertSort(tab):
    for i in range(0, len(tab)):
        passage = tab[i]
        j = i
        while j > 0 and tab[j - 1] > passage:
            tab[j] = tab[j - 1]
            j = j - 1
            tab[j] = passage
    return tab


# Ex
tab = [78, 58, 41, 26, 15]
print(insertSort(tab))


# -----------------------------------------------#

# Selection sort
def algoSort(list):
    i = 0
    for i in range(0, len(list)):
        j = i
        for j in range(0, len(list)):
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]

    return list


# Ex
list = [5, 4, 3, 2, 1, 0]
print(algoSort(list))


# -----------------------------------------------#

# Bubble sort
# def bubble_sort(arr):
# n = len(arr)
# for i in range(n):
# for j in range(0, n - i - 1):
# if arr[j] > arr[j + 1]:
# arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Ex
# arr = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(arr)
# print("Le résultat ", arr)


# -----------------------------------------------#

def bubbleSort(tableau):
    inversion = True
    passage = 0
    while inversion == True:
        inversion = False
        passage = passage + 1
        for i in range(0, len(tableau) - passage):
            if tableau[i] > tableau[i + 1]:
                inversion = True
                tableau[i], tableau[i + 1] = tableau[i + 1], tableau[i]
    return tableau


# Ex
tableau = [64, 34, 25, 12, 22, 11]
print(bubbleSort(tableau))
