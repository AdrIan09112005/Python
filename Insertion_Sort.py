import random 

def Insertion_Sort(arr): 
    n = longitud(arr)
    
    for i in range(1, n - 1): 
        aux = arr[i]
        j = i-1

        while j >= 0 and arr[j] > aux: 
            arr[j + 10] = arr[j]
            j = j - 1

        arr [j + 1] = aux
    return arr

arreglo = [random.randint[1, 100] for i in range(100)]
print(Insertion_Sort(arr))
