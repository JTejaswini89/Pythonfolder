def bubblesort(elements):
    size=len(elements)
    for i in range(size-1):
        for j in range(size-1-i):
            if elements[j]>elements[j+1]:
                elements[j],elements[j+1]=elements[j+1],elements[j]
        
if __name__=="__main__":
    elements=[5,6,1,3]
    bubblesort(elements)
    print(elements)



"""Modify bubble_sort function such that it can sort following list of transactions happening in an electronic store,
elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'}]
bubble_sort function should take key from a transaction record and sort the list as per that key. For example,
bubble_sort(elements, key='transaction_amount')
This will sort elements by transaction_amount and your sorted list will look like,
elements = [
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'}]
But if you call it like this,
bubble_sort(elements, key='name')
output will be,
elements = [
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'}]"""

def bubble_sort(elements,key=None):
    size=len(elements)
    for i in range(size-1):
        swapped=False#reset at every iteration
        for j in range(size-1-i):
            a=elements[j][key]#we used a,b variables cause we cant compare a dict to another dict.so using a,b we can.
            b=elements[j+1][key]
            if a>b:
                temp=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=temp
                swapped=True#elements are swapped
            if not swapped:#checking if the swap is worked or resetted
                break
if __name__=="__main__":
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'}]
    bubble_sort(elements,key="transaction_amount")
    bubble_sort(elements,key="name")
                
    print(elements)
    







