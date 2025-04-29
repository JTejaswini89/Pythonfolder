def insertion_sort(elements):
    for i in range(1,len(elements)):
        key=elements[i]
        j=i-1
        while j>=0 and elements[j]>key:
            elements[j+1]=elements[j]
            j-=1
        elements[j+1]=key
    return elements
ele=[5,2,3,4,6,1]
print(insertion_sort(ele))

        
