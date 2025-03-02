#=========================VARIABLES=======================
#Create a variable called break and assign it a value 5.
#See what happens and find out the reason behind the behavior that you see.
break=5

#===============
#Create two variables.One to store your birthyear and another oneto store current year.
#Now calculate your age using these two variables
birth_date=2003
current_date = 2025
age=current_date-birth_date
print(age)

#=============
#store your first, middle and last name in three different variables and
#then print your full name using these variables
first_name="Jonnagaddala"
middle_name="Tejaswini"
last_name="Nagaraju"
print(first_name+ " " +middle_name+" "+last_name)

#===============
#Answer which of these are invalid variable names:
# _nation 1record record1 record_one record-one record^one continue
1record record-one record^one continue



#=================NUMBERS==================
#You have a football field that is 92 meter long and 48.8 meter wide.
#Find out total area using python and print it.
length=92
width=48.8
area=length*width
print("The area of teh Football field is:" ,area)


#You bought 9 packets of potato chips from a store.
#Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python,
#how many dollars is the shopkeeper going to give you back?

num_packets=9
one_pack=1.49
total=num_packets*one_pack
given_to_sp=20
received_by_sp=(paid-total)
print("The amount you receive from the shopkeeper is: ", receive)


#You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
#If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.
#Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)

side=5.5
area_square=side**2
cost_per_tile=500
total_cost=area_square*cost_per_tile
print(area_square)
print("The total cost required to repalce the tiles in the bathroom is: " , total_cost)



#Print binary representation of number 17
num = 17
print("The binary representation of number 17 is:", format(num, 'b'))

#=================STRINGS==================
# 1. Create 3 variables to store street, city and country, now create address variable to
# store entire address. Use two ways of creating this variable, one using + operator and the
#other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line
street = "Hanuman Ghatt"
city = "Bengalore"
country = "Electronic city"
address = street + '\n' + city + '\n' + country
print("Address using + operator:",address)
address = f'{street}\n{city}\n{country}'
print("Address using f-string:",address)

#Create a variable to store the string "Earth revolves around the sun"
#Print "revolves" using slice operator
#Print "sun" using negative index

sentence="Earth revolves around the sun"
print(sentence[6:14])
print(sentence[-4:])

#Create two variables to store how many fruits and vegetables you eat in a day.
#Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
#Use python f string for this.
veggies="5"
fruits="6"
print(f'i eat {veggies} veggies and {fruits} fruits daily.')

#I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement,
#the correct statement is 'maine 10 samosa khaye'.
#Replace incorrect words in original strong with new ones and print the new string.
#Also try to do this in one line
s='maine 200 banana khaye'
s=s.replace('banana' , 'samosa').replace('200','10')
print(s)

#=======================IF STATEMENTS========================
#Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#Ask user to enter his fasting sugar level
#If it is below 80 to 100 range then print that sugar is low
#If it is above 100 then print that it is high otherwise print that it is normal

sugar_level=input("Enter your sugar level:")
sugar_level=float(sugar_level)
if sugar_level<80:
    print("Your sugar level is low")
elif sugar_level>100:
    print("Your sugar level is high")
else:
    print("Your sugar level is normal")

#Using following list of cities per country,
#india = ["mumbai", "banglore", "chennai", "delhi"]
#pakistan = ["lahore","karachi","islamabad"]
#bangladesh = ["dhaka", "khulna", "rangpur"]
#Write a program that asks user to enter a city name and it should tell which country the city belongs to
#Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
#For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and
#dhaka it should print "They don't belong to same country"


india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city_name=input("Enter your city name:")
if city_name in india:
    print("You are in India")
elif city_name in pakistan:
    print("You are in Pakistan")
elif city_name in bangladesh:
    print("You are in Bangladesh")
else:
    print("Not a valid city name")
#===============================================

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city1=input("Enter your first city name:")
city2=input("Enter your second city name:")
if city1 in india and city2 in india:
    print("Both cities are in same country India.")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in same country Pakistan.")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in same country Bangladesh.")
else:
    print("Both cities are not in same country")

#==========================LOOPS==================================

#Print square of all numbers between 1 to 10 except even numbers

for i in range(11):
    if i%2==0:
        continue
    print(i*i)


#Your monthly expense list (from Jan to May) looks like this,
#expense_list = [2340, 2500, 2100, 3100, 2980]
#Write a program that asks you to enter an expense amount and program should tell you in
#which month that expense occurred.
#If expense is not found then it should print that as well.

month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
expense = int(input("Enter expense amount: "))

month = -1
for i in range(len(expense_list)):
    if expense == expense_list[i]:
        month = i
        break

if month != -1:
    print(f'You spent {expense} in {month_list[month]}')
else:
    print(f'You didn\'t spend {expense} in any month')



#After flipping a coin 10 times you got this result,
#result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
#Using for loop figure out how many times you got heads

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count=0
for item in result:
    if item == "heads":
        count+=1
        print(count)


#Lets say you are running a 5 km race. Write a program that,

#Upon completing each 1 km asks you "are you tired?"
#If you reply "yes" then it should break and print "you didn't finish the race"
#If you reply "no" then it should continue and ask "are you tired" on every km
#If you finish all 5 km then it should print congratulations message

race_distance=5
for i in range(race_distance):
    print("You ran",i+1 ,"miles")
    ask1=input("Are you tired?")
    if ask1=='yes':
        print("You didnt finsih the race")
        break
    else:
        print("Congrats , you finished the race.")
#================(or)=====================

for i in range(5):
    print(f"You ran {i+1} miles") # i starts with zero hence adding 1
    tired = input("Are you tired? ")
    if tired == 'yes':
        break

if i == 4: # 4 because the index starts from 0
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print("You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")


#Write a program that prints following shape

#*
#**
#***
#****
#*****

for i in range(1,6):
    s=" "
    for j in range(i):
        s+="*"
    print(s)


#=============================FUNCTIONS=============================

#Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
#area = (1/2)*base*height

def calculate_area(base,height):
    area = (1/2)*base*height
    return area
area_of_triangle=calculate_area(5,6)
print("Area of the triangle:" ,area_of_triangle)
#================================================================
def calculate_area(d1,d2,s="triangle"):
    if s=='triangle':
        area = (1/2)*d1*d2
    elif s=='rectangle':
        area=d1*d2
    else:
        print("Enter a valid shape")
    return area
base=10
height=5
triangle_area=calculate_area(base,height,"triangle")
print("Area of triangle is:",triangle_area)

length=20
width=30
rectangle_area=calculate_area(length,width,"rectangle")
print("Area of rectangle is:",rectangle_area)

triangle_area=calculate_area(base,height) 
print("Area of triangle with no shape supplied: ",triangle_area)

#========================DICTIONARY=========================================

#We have following information on countries and their population (population is in crores),

#Country	Population
#China	143
#India	136
#USA	32
#Pakistan	21
#Using above create a dictionary of countries and its population
#Write a program that asks user for three type of inputs,
#print: if user enter print then it should print all countries with their population in this format,
#china==>143
#india==>136
#usa==>32
#pakistan==>21
#add: if user input add then it should further ask for a country name to add.
#If country already exist in our dataset then it should print that it exist and do nothing.
#If it doesn't then it asks for population and add that new country/population in our dictionary and print it
#remove: when user inputs remove it should ask for a country to remove.
#If country exist in our dictionary then remove it and print new dictionary using format shown above in (a).
#Else print that country doesn't exist!
#query: on this again ask user for which country he or she wants to query.
#When user inputs that country it will print population of that country.

count_pop={'china':143 , 'india':136 , 'usa':32, 'pakistan':21}
print(count_pop)
info=input("Do you like to enter a country:")
country=input("Enter a country name:")
if country in count_pop:
    print("Country already exists")
else:
    population=input("Enter the country population:")
    count_pop[country]=population
print(count_pop)
remove=input("Enter a country to remove:")
if remove in count_pop:
    count_pop.pop(remove)
else:
    print("Does not  exists")
print(count_pop)
query=input("Enter your query:")
if query in count_pop:
    print(count_pop[query])
else:
    print("Country you requested doesnot exists")
print(count_pop)

#=============================================================================
#You are given following list of stocks and their prices in last 3 days,

#Stock	Prices
#info	[600,630,620]
#ril	[1430,1490,1567]
#tl	[234,180,160]
#Write a program that asks user for operation. Value of operations could be,
#print: When user enters print it should print following,
#info ==> [600, 630, 620] ==> avg:  616.67
#ril ==> [1430, 1490, 1567] ==> avg:  1495.67
#mtl ==> [234, 180, 160] ==> avg:  191.33
#add: When user enters 'add', it asks for stock ticker and price.
#If stock already exist in your list (like info, ril etc) then it will append the price to the list.
#Otherwise it will create new entry in your dictionary.
#For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

stockvalues={'info':[600,630,620] , 'ril':[1430,1490,1567],'tl':[234,180,160]}
info=[600,630,620]
ril=[1430,1490,1567]
tl=[234,180,160]
while True:
    operation = input("Enter an operation (print, exit): ").strip().lower()
    
#The .strip() method in Python removes leading and trailing spaces (or specified characters) from a string.It does not remove spaces between words.
#The .lower() method converts all characters in a string to lowercase.


    if operation == "print":
        print("Your info is:",info)
        for i in range(len(info)):
            avg=(info[i]+info[i]+info[i])/3
        print("Your average is:" , avg)
        print("Your ril stocks are:",ril)
        for i in range(len(ril)):
            avg=(ril[i]+ril[i]+ril[i])/3
        print("Your average is:" , avg)
        print("Your tl stocks are:",tl)
        for i in range(len(tl)):
            avg=(tl[i]+tl[i]+tl[i])/3   
        print("Your average is:" , avg)
        break
    
    else:
        print("Invalid operation. Try again!")


stock = input("Enter your new stock: ")
price = list(map(int, input("Enter the price of your stock (space-separated): ").split()))  

stockvalues.update({stock: price})

print(stockvalues)


#Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and
#returns area, circumference and diameter. You should get these values in your main program by calling
#circle_calc function and then print them Solution

import math

def circle_calc(radius):
    area = math.pi * radius ** 2
    diameter = 2 * radius
    circumference = math.pi * diameter
    return area, diameter, circumference  
r = float(input("Enter the radius: "))
area, diameter, circumference = circle_calc(r)

print("Area:",area)
print("Diameter:",diameter)
print("Circumference:" , circumference)


#=======================================DATASTRUCTURES=============================
#=====================ARRAYS===================================
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
#======================================================
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
#========================================================================
arr = list(map(int, input("Enter your array: ").split()))
arr = list(set(arr))  # Remove duplicates
print("Array after removing duplicates:", arr)
#========================================================
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


#Given a sorted array, find the first and last position 

arr=[2,3,4,5,6]
print(arr[0])
print(arr[-1])


#palindrome
num=input("Enter your value:")
num[::-1]
#print(int(num))
print(str(num))

#count no of digits
num=int(input("Enter your number:"))
count=0
while num!=0:
    num//=10
    count+=1
print(count)


#Reverse a string using a loop
s=input("Enter your string:")
rev=s[::-1]
if s==s[::-1]:
    print("It is a palindrome:",rev)
else:
    print("Not a palindrome:",rev)

    














