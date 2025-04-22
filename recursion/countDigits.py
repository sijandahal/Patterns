def countDigits(i):
    if (i >= 1):
        countDigits(i - 1)
        print(i)
        
countDigits(3)
# This print all the functuons first and then the pritn(i) is executed after the condition is not met, so 1,2,3


    

def countDigitsfromBack(i):
    if (i >= 1):
        print(i)
        countDigitsfromBack(i - 1)

countDigitsfromBack(3)

# This prints all the values first, so output is (3) then the condition is run and output is (2) then the condition is run and output is 1 then the condition is run. then again check when the n = 0 so that is false so it breaks out of the loop


# Printing the name N times,
def printName(i):
    for i in range(1,i+1):
        print("Sijan")

printName(5)


# Printing the name n times using the recursion

def PrintNameUsingRecursion(i):
    if (i <= 1 ):
        PrintNameUsingRecursion(i)
        print("Sijan")

PrintNameUsingRecursion(5)

# SumofFirstNNumbers

def SumofFirstNNumbers(i):
    sum = 0
    for i in range(1,i + 1):
        sum += i
    print(sum)

SumofFirstNNumbers(5)

def SumofFirstNNumbersUsingRecursion(i):
    sum = 0
    if i == 0:
       return 0
    return i + SumofFirstNNumbersUsingRecursion(i - 1)
# print(sum)
SumofFirstNNumbersUsingRecursion(5)


# Print 1 to N using recursion
def PrintOnetoN(i):
    if (i >=1):
        PrintOnetoN(i -1)
        print(i)

PrintOnetoN(7)

	
# Print N to 1 using recursion
def PrintNtoOne(i):
    if (i>=1):
        print(i)
        PrintNtoOne(i - 1)

PrintNtoOne(7)


# Factorial of N numbers using recustion

def Factorial(n):
    if n == 0:
        return 1
    return n * Factorial(n - 1)

print(Factorial(2))

# Reverse an array

# Using BuiltIn function
def usingBuiltInReverseMethod(i):
    new_array = []
    for element in reversed(i):
        print("Reverse an array")
        print(element)
        new_array.append(element)
    print(new_array)
    
usingBuiltInReverseMethod([1,2,3,4])


# Using reverse in the loop itself
def ReverseAnArray(i):
    new_array = []
    for element in range((len(i) -1), -1, -1):
        print(i[element])
        new_array.append(i[element])
    print(new_array)

ReverseAnArray([1,2,3])


# Using a Two Pointer Approach

def ReverseAnArrayUsingTwoPointer(i):
    start = 0
    end = len(i) - 1

    while (start < end):
        i[start], i[end] = i[end], i[start]
        start = start + 1
        end = end - 1
    print (i)
    return True

ReverseAnArrayUsingTwoPointer([5,4,3,2,1])

# Time Complexity - o(1)

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.



def palindrome(i):
    new_phrase = ""
    for letter in i.lower():
        if letter.isalnum():
            new_phrase += letter
        print(new_phrase)
    start = 0
    end = len(new_phrase) - 1
    while start < end:

        if (new_phrase[start] != new_phrase[end]):
            return False
        start = start + 1
        end = end - 1
    return True

print(palindrome("A man, a plan, a canal: Panama"))


def palindromeusingSlice(i):
    if i == i[::-1]:
        return True
    else:
        return False

print(palindromeusingSlice("rar"))


# Fibonacci Number

