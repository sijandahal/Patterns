# Brute Force Approach

import math


def count(n):
    counter = 0
    if n == 0:
        print(1)
        return
    if n < 0:
        n = n * -1

    while n > 0:
      n =  n // 10
      counter = counter + 1
    print(counter)


count(-1236)
count(12345)
count(0)

# Optimal Approach

def countDigits(n):
    countDigit = int(math.log10(n)+ 1)
    print(countDigit)

countDigits(1111)

# Reverse A number
def reverse(n):
    reversed_number = 0
    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n = n // 10
    return reversed_number

print(reverse(5525))    