def selection_sort(array):
    for i in range(len(array)):
        min_index=i
        for j in range(i+1,len(array)):
            if array[j]<array[min_index]:
                min_index=j
        array[i],array[min_index]=array[min_index],array[i]
    return array

array=[5,1,4,2,6,3]
print(selection_sort(array))
