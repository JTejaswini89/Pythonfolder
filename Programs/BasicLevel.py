#Write a Python function to count the number of vowels in a given string.
def vowels_count(string):
    vowels=["a","e","i","o","u"]
    count=0
    for char in string.lower():
        if char in vowels:
            count+=1
    return count
a="Hello world"
print("The no of vowels in the string",vowels_count(a))

#Write a program that takes a list of integers and returns the second largest element.
def second_largest(numbers):
    if len(numbers)<2:
        return None
    sorted_numbers=sorted(numbers,reverse=True)
    return sorted_numbers[1]
numbers=[4,5,7,9,6]
print("the second  largest number from the list is:",second_largest(numbers))

#Two strings are anagrams if they contain the same characters in different
#order. Write a function to check this.
def anagrams(string1,string2):
    return sorted(string1.lower()) == sorted(string2.lower())
string1="Listen"
string2="help"
print("yes"if anagrams(string1,string2) else "no")

#Given an integer, repeatedly sum its digits until the result is a single digit.

def sum(number):
    while number >= 10:
        total = 0
        while number > 0:
            total += number % 10  
            number //= 10  
        number = total  

    return total

number=1452
print(sum(number))


#write a python program to do aritehmatical operations addtion and subtraction.
a=4
b=5
sum_result=a+b
sub_result=a-b
print("The addition of tw numbers",sum_result)
print("The subtraction of two numbers",sub_result)

#write a python program to find area of triangle
a=5
b=4
area=0.5*a*b
print(area)


#write a pyhton program to swap two variables
a=5
b=6
print(a)
print(b)
temp=a
a=b
b=temp
print(a)
print(b)
a,b=b,a
print(a)
print(b)

#write a python program to generate a random number
import random
print(random.randint(1,100))

#convert the kilometers into miles
a_kilometers=85
conversion=0.62137119
a_miles=a_kilometers*conversion
print("the miles are:",a_miles)

#write  a python program to convert celcius to farenheit
celcius=39
farenheit=celcius*(9/5)+32
print(farenheit)

#write a python program to print calender
import calendar
year=2024
month=12
cal=calendar.month(year,month)
print(cal)

#write a python program to solve teh quadratic equation
import math
a=3
b=5
c=6
discriminant=b**2-4*a*c
if discriminant>0:
    root1=(-b+math.sqrt(discriminant))/(2*a)
    root2=(-b-math.sqrt(discriminant))/(2*a)
    print("Root1:",root1)
    print("Root2:",root2)
elif discriminant==0:
    root1=-b/2*a
    print("Root1:",root1)
else:
    real_part=-b/2*a
    imaginary_part=math.sqrt(abs(discriminant))/2*a
    print("root1:",real_part+imaginary_part)
    print("root1:",real_part-imaginary_part)


#write a python program to check if a number is positive ,neagtive,or zero.
number=4
if number>0:
    print("The number is positive")
elif number<0:
    print("The number is negative")
else:
    print("The number is zero")

#write a python program to check if the number is even or odd
number=5
if number%2==0:
    print("The number is even")
else:
    print("The number is odd")


#write  apyhton program to check if the year is leap year or not
year=2024
if (year%400==0) and (year%100==0):
    print("the year is a century and a leap year")
elif (year%4==0) and (year%100!=0):
    print("The year is not acentury year but it is ac entury year")
else:
    print("the year not a century year nor a leap year")


#write a python program to check if it is a prime number or not
number=27
flag=False
if number<0:
    print("Enter a valid number")
elif number==1:
    print("1 is a prime number")
else:
   for i in range(2,number):
       if (number%i==0):
           flag=True
           break
if flag:
    print("Not prime")
else:
    print("a prime")


#write a python program to print al the prime number between 1-10
for num in range(1,11):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
           print("Prime",num)

#wrtie a python program to find factorial of number
number=5
fact=1
for i in range(1,number+1):
    fact=fact*i
print(fact)



#write a python program to print fibonacci
nterms=10
n1=0
n2=1
count=0
if nterms<0:
    print("enter a valid number")
elif nterms==1:
    print("the fibonnaci of",nterms,"is",n2)
else:
    print("The fibonnaci sreis")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1

# Write a Python Program to Find the Sum of Natural Numbers.
def natural_num(numbers):
    sum=0
    for i in range(1,numbers):
        sum+=i
    return sum
numbers=11
print(natural_num(numbers))


# Write a Python Program to Find LCM.
def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if ((greater%x==0) and (greater%y==0)):
            lcm=greater
            break
        greater+=1
    return lcm
num1=54
num2=24
print("their lcm is:",lcm(num1,num2))

#write a Python Program to Find HCF.
def hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if ((x%i==0) and (y%i==0)):
            hcf=i
    return hcf
num1=54
num2=24
print("Their hcf is:",hcf(num1,num2))


#Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.
num=5
print(num,"binary number is:",bin(num))
print(num,"octal number is:",oct(num))
print(num,"hexadecimal number is:",hex(num))

# Write a Python Program To Find ASCII value of a character.
char="p"
print(ord(char))


#write a python program to print the largest element from teh array

def largest_element(array):
    if not array:
        return "Array is empty"
    largest_ele=array[0]
    for element in array:
        if element>largest_ele:
            largest_ele=element
    return largest_ele

array=[10,20,30,80,40]
print("largest element from teh array",largest_element(array))


#write a python program to print array rotation
def rotate_arr(arr,d):
    n=len(arr)
    if d<0 or d>=n:
        return "Invalid array position"
    rotated_array=[0]*n
    for i in range(n):
        rotated_array[i]=arr[(i+d)%n]
    return rotated_array
arr=[1,2,3,4,5]
d=2
print("array rotation",rotate_arr(arr,d))


# Write a Python Program to Split the array and add the first part to the end?
def split(array,k):
    if k<0 or k>len(arr):
        return arr
    first_part=arr[:k]
    second_part=arr[k:]
    result =second_part+first_part
    return result
array=[1,2,3,4,5]
k=3
print("Split the array and add the first part to the end",split(array,k))

# Write a Python Program to Sort Words in Alphabetic Order.

def sort_alp(my_str):
    words=my_str.split()
    words=[word.capitalize() for word in words]
    words.sort()
    return words
my_str="hello everyone weelcom"
print(sort_alp(my_str))


def aplha_sort(my_str):
    words=[my_str.split()]
    for word in words:
        words.sort()
    return words
my_str="hello mom welcome yaar"
print(aplha_sort(my_str))


my_str="hello welceome mom to me"
wordss=[my_str.split()]
for word in wordss:
    word.sort()
print(word)


# write a pyhton program to  remove puncutation from the string


punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str="hello! welcome, feel free.."
no_p=""
for char in my_str:
    if char not in punctuations:
        no_p=no_p+char
print(no_p)
        

# Write a Python program to check if the given number is a Disarium Number.
def is_disarium(number):
    str_num=str(number)
    total=0
    for index in range(len(str_num)):
        num=int(str_num[index])
        total+=num**(index+1)  #index+1 strat from 0 values instead of 1 ante
        #index vachi 0 but plus chesi aa value in add chestham
    return total==number
numm=89
print(is_disarium(numm))


# Write a Python program to print all disarium numbers between 1 to 100.

def is_disa(number):
    str_num=str(number)
    total=0
    for index in range(len(str_num)):
        num=int(str_num[index])
        total+=num**(index+1)    
    return total==number

print("The disarium numbers")
for num in range(1,101):
    if is_disa(num):
        print(num)

print()

#Write a Python program to determine whether the given number is a HarshadNumber    
number=43
total=0
for i in (str(number)):
    int_num=int(i)
    total+=int_num
if number%total==0:
    print("it is HarshadNumber")
else:
    print("checkonce")
print()

#with interval
def harshand_number(number):
    total=0
    for i in (str(number)):
        int_num=int(i)
        total+=int_num
    return number%total==0

for i in range(1,101):
    if harshand_number(i):
        print("HarshadNumber",i)
print()
print("pronic Numbers")
    

#write a python program to print pronic numbers


def is_pronic(number):
    for i in range(1,number+1):
        if i*(i+1)==number:
            return True
    return False    
number=101
for i in range(1,number):
    if is_pronic(i):
        print("pronic numbers",i)
print()
print("sum the elements in a arary")
    
#write a python program to write and  sum the elements in a arary

numbers=[10,20,30,40,50]
total=0
for i in range(len(numbers)):
    total+=numbers[i]
print("the sum of the array:",total)
print()

#write a python program to print multiply all the numbers in the list.

numbers=[1,2,3,4,5]
total=1
for i in range(len(numbers)):
    total*=numbers[i]
print("The multiply all the numbers in the list:",total)
print()


#write a python program to print the smallest number
number=[10,20,30,-4]
number.sort()
smallest_number=number[0]
for i in number:
    if i<smallest_number:
        smallest_number=i
print(smallest_number,"is the smallest number")
#===========
print("using built in function")
numbers=[1,2,3,-4]
print(min(numbers))
#write a python program to print the largest element of the list

number=[10,2,3,40-45,50]
largest_number=number[0]
for i in number:
    if i>largest_number:
        largest_number=i
print(i,"is the largest number")

print("Using built in function")
numbers=[1,2,3,-7,-5]
print(max(numbers))


#write a python program to print second largest element.
number=[10,20,30,40,50,70,90]
number.sort(reverse=True)
for i in number:
    if len(number)>=2:
        second_largest=number[1]
print(second_largest)


# Write a Python program to find N largest elements from a list.
def n_largest_numbers(numbers,n):
    sorted_list=sorted(numbers,reverse=True)
    largest_elements=sorted_list[:n]
    return largest_elements
numbers=[10,20,453,100,569,41]
N=3
print(n_largest_numbers(numbers,N))

# Write a Python program to Remove empty List from List.
list_of_list=[[1,2,3,4],[1,2],[],[1]]
filtered_lst=[]
for i in list_of_list:
    if i:
        filtered_lst.append(i)
print(filtered_lst)



















