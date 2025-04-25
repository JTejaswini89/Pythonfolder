arr = [1, 2, 2, "apple", 4, 5.5]

arr.append(3)  # [1, 2, 2, "apple", 4, 5.5, 3]
arr.pop(2)     # Removes element at index 2 → [1, 2, "apple", 4, 5.5, 3]
arr.remove(2)  # Removes first occurrence of 2 → [1, "apple", 4, 5.5, 3]
arr.extend([2]) # Extends list with [2] → [1, "apple", 4, 5.5, 3, 2]

print("Before Reverse:", arr)  # [1, "apple", 4, 5.5, 3, 2]

arr.reverse()  # Reverses the list in place
print("After Reverse:", arr)  # [2, 3, 5.5, 4, "apple", 1]

print("Index of 3:", arr.index(3))  # Finds the index of 3
print("Count of 2:", arr.count(2))  # Counts occurrences of 2
print("Final List:", arr)#=====================ARRAYS===================================
#Let us say your expense for every month are listed below,
#January - 2200
#February - 2350
#March - 2600
#April - 2130
#May - 2190
#Create a list to store these monthly expenses and using that find out,

#1. In Feb, how many dollars you spent extra compare to January?
#2. Find out your total expense in first quarter (first three months) of the year.
#3. Find out if you spent exactly 2000 dollars in any month
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#5. You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this

exp=[2200,2350,2600,2130,2190]
print(" In february dollars you spent extra compare to January:",exp[1]-exp[0])
print("Your total expense for the first five months are:" , exp[0]+exp[1]+exp[2]+exp[3]+exp[4],"dollars")
for i in range(len(exp)):
    if exp[i]==2000:
        print(exp[i] ,"You spent exactly 2000 on this month")
    else:
        print("You didnt spent exactly 2000 on any month")
        break
exp.append(1980)
print(exp)
exp[3]=2800
print(exp)

#another way of taking user input for list 
exp = list(map(int, input("Enter the values you spent in the first five months (space-separated): ").split()))


# when you take input from user in other way
exp = []  # Empty list to store expenses
print("Enter the values you spent in the first five months:")

for i in range(5):
    amount = int(input(f"Month {i+1}: "))  # Take input and convert to integer
    exp.append(amount)  # Append to list

print("Your expenses for the first five months:", exp)



#You have a list of your favourite marvel super heros.
#heros=['spider man','thor','hulk','iron man','captain america']
#Using this find out,

#1. Length of the list
#2. Add 'black panther' at the end of this list
#3. You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'
#4. Now you don't like thor and hulk because they get angry easily :)
#   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#   Do that with one line of code.
#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros=['spider man','thor','hulk','iron man','captain america']
heros.append('black panther')
print(heros)
heros.remove('black panther')
print(heros)
heros.insert(3,'black panther')
heros[1:3]=['doctor strange']
heros.sort()
print(len(heros))
print(heros)



#Create a list of all odd numbers between 1 and a max number.
#Max number is something you need to take from a user using input() function

max_num=int(input("Enter your Number:"))
odd=[]
for i in range(1,max_num):
    if i%2==1:
        odd.append(i)
print(odd)

max_num=22
min_num=2
odd=[]
for i in range(2,22):
    if i%2==1:
        odd.append(i)
print(odd)



#Given an array, find the maximum and minimum element.

arr=[2,3,4,5,6,7]
print(max(arr))
print(min(arr))
#another way of find min and max with out using built in functions
def find_min_max(arr):
    if not arr:
        return None,None
    min_num=arr[0]
    max_num=arr[0]

    for i in arr[1:]:
        if i<min_num:
            min_num=i
        elif i>max_num:
            max_num=i

    return min_num,max_num
arr=list(map(int,input("Enter your array:").split()))
minimum,maximum=find_min_max(arr)
print(minimum,maximum)
print(arr[::-1]) #Given an array, reverse the elements 

#Given an array, find the second largest element without sorting.
arr=[2,3,4,5]
print(max(arr))

#Given an array, check if it is sorted in non-decreasing order.
def sort_arr(arr):
    arr.sort()
    return arr

arr=[2,3,6,5]
print(arr)
if arr.sort==True:
    print(arr)
else:
    print("Not yet.. processing...",sort_arr(arr),"Done")


#Given a sorted array, remove duplicate elements in-place.

arr = list(map(int, input("Enter your array: ").split()))
arr = list(set(arr))  # Remove duplicates
print("Array after removing duplicates:", arr)
#====
def remove_dup(arr):
    unique_ele=[]
    for i in arr:
        if i not in unique_ele:
            unique_ele.append(i)
    return unique_ele
arr= list(map(int, input("Enter your array: ").split()))
print(remove_dup(arr))



#Given two arrays, find their union and intersection


arr1 = list(map(int, input("Enter your array: ").split()))
arr2 = list(map(int, input("Enter your array: ").split()))
arr1=(set(arr1))
arr2=(set(arr2))
union=(arr1.union(arr2))
intersection=(arr1.intersection(arr2))
print(list(union))
print(list(intersection))
