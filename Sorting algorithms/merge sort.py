def merge_sort(arr):
    sorted_lsst=[]
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:m]
        r=arr[m:]
    while i<l[i] and j<r[j]:
        if l[i]<=r[j]:
            sorted_list.append(l[i])
            i+=1
        else:
            sorted_list.append(r[i])
            j+=1
    return arr
arr=[1,7,5,6,4,8,2,3]
print(merge_sort(arr))
    
