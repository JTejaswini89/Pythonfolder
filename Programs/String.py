"""" Create a function that takes a string as input and capitalizes a letter if its ASCII code
 is even and returns its lower case version if its ASCII code is odd.
 Examples
 ascii_capitalize("to be or not to be!") 
➞ "To Be oR NoT To Be!"
 ascii_capitalize("THE LITTLE MERMAID") 
➞ "THe LiTTLe meRmaiD"
 ascii_capitalize("Oh what a beautiful morning.") 
➞ "oH wHaT a BeauTiFuL
 moRNiNg."""
def asciicode(string):
    for i in string:
        if ord(i)%2==0:
            print(i.upper(),end="")
        else:
            print(i.lower(),end="")
        
string="to be or not to be"
print(asciicode(string))

def asciicode(string):
    result=""
    for i in string:
        if ord(i)%2==0:
            result+=i.upper()
        else:
            result+=i.lower()
    return result
        
string="to be or not to be"
print(asciicode(string))

"""Write a function, that replaces all vowels in a string with a specified vowel.
 Examples
 vow_replace("apples and bananas", "u") 
vow_replace("cheese casserole", "o") 
➞ "upplus und bununus"
 ➞ "chooso cossorolo"
 vow_replace("stuffed jalapeno poppers", "e") 
➞ "steffed jelepene peppers"
 Notes
 All words will be lowercase. Y is not considered a vowel"""


def vow_replace(string,vowel):
    vowels="aeiou"
    result=""
    for i in string:
        if i in vowels:
            result+=vowel
        else:
            result+=i
    return result
string="apples and bananas"
vowel="u"
#string=input("Enter a string")
#vowel=input("Enter a vowel:")
print(vow_replace(string,vowel))


"""" Write a function that creates a dictionary with each (key, value) pair being the (lower
 case, upper case) versions of a letter, respectively.
 Examples
 mapping(["p", "s"]) 
➞ { "p": "P", "s": "S" }
 mapping(["a", "b", "c"]) 
➞ { "a": "A", "b": "B", "c": "C" }
 mapping(["a", "v", "y", "z"]) 
➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
 Notes
 All of the letters in the input list will always be lowercase."""

def mapping(letters):
    result={}
    for i in letters:
        result[i]=i.upper()
    return result
#letters=input("Enter you list").split()
letters=["p","s"]
print(mapping(letters))


""" Write a function that converts a dictionary into a list of keys-values tuples.
 Examples
 dict_to_list({
 "D": 1,
 "B": 2
 "C": 3
 }) 
➞ [("B", 2), ("C", 3), ("D", 1)]
 dict_to_list({
 "likes": 2,
 "dislikes": 3,
 "followers": 10
 }) 
➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]
 Return the elements in the list in alphabetical order."""



def dict_to_list(input_dict):
    sorted_dict=sorted(input_dict.items())
    result=[(key,values) for key,values in sorted_dict]
    return result
input_dict={
 "D": 1,
 "B": 2,
 "C": 3
 }
"""input_dict = {}
n = int(input("Enter the number of key-value pairs: "))

for _ in range(n):
key, value = input("Enter key and value separated by space: ").split()
input_dict[key] = value  # Stores values as strings"""

print("Dictionary:", dict_to_list(input_dict))



"""" Create a function that takes three integer arguments (a, b, c) and returns the amount
 of integers which are of equal value.
 Examples
 equal(3, 4, 3) 
➞ 2
 equal(1, 1, 1) 
➞ 3
 equal(3, 4, 1) 
➞ 0
 Notes
 Your function must return 0, 2 or 3"""

def intarg(a,b,c):
    if a==b==c:
        return 3
    elif a==b or b==c or a==c:
        return 2
    else:
        return 0
#a,b,c=input("enter three numbers with space after each number:").split()
a,b,c=3,4,3
print(intarg(a,b,c))


""" Create a function that validates whether three given integers form a Pythagorean
 triplet. The sum of the squares of the two smallest integers must equal the square of
 the largest number to be validated.
 Examples
 is_triplet(3, 4, 5) 
3² + 4² = 25
 5² = 25
 ➞ True
 is_triplet(13, 5, 12) 
➞ True
 5² + 12² = 169
 13² = 169
 is_triplet(1, 2, 3) 
➞ False
 1² + 2² = 5
 3² = 9
 Notes
 Numbers may not be given in a sorted order"""

def is_triplet(a,b,c):
    sorted_num=sorted([a,b,c])
    return sorted_num[0]**2 + sorted_num[1]**2 ==sorted_num[2]**2
a,b,c=3,4,5
print(is_triplet(a,b,c))


"""Create a function that takes a list of strings and return a list, sorted from shortest to
 longest.
 Examples
 sort_by_length(["Google", "Apple", "Microsoft"]) 
➞ ["Apple", "Google", "Microsoft"]
 sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]) 
➞ ["Raphael",
 "Leonardo", "Donatello", "Michelangelo"]
 sort_by_length(["Turing", "Einstein", "Jung"]) 
➞ ["Jung", "Turing", "Einstein"]
 Notes
 All test cases contain lists with strings of different lengths, so you won't have to dea"""

def sort_by_length(lst):
    return sorted(lst,key=len)
#lst=list(map(str,input("Enter your company:").split())) accepts only string data type
lst=input("enter company names:").split()#accepts any type of data and sortes that based on size(33,444,2)-->(2,33,444)
print(sort_by_length(lst))
































































