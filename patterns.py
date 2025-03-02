print("Pattern One")

def pattern_one(n):
    for i in range(n):
        for j in range(n):
            print(" * ", end= "")
        print("")

pattern_one(5)

# PatternOneEnd
print("Pattern Two")
def pattern_two(n):
    for i in range(n + 1):
        for j in range(i):
            print("*", end= "")
        print("")
pattern_two(5)

print("Pattern Three")
def pattern_three(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(j + 1, end= " ")
        print("")
pattern_three(5)

print("Pattern Four")
def pattern_four(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end="")
        print("")

pattern_four(5)


print("Pattern Five")
def pattern_five(n):
    for i in range(1, n + 1):
        for j in range(n- i + 1):
            print("*", end= "")
        print("")
pattern_five(5)

print("Pattern Six")
def pattern_six(n):
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            print(j + 1, end="  ")
        print("")

pattern_six(5)


print("Pattern Seven")
def pattern_seven(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" S ", end= "")
        for j in range(2 * i - 1):
            print(" * ", end = "")
        for j in range(n - i):
            print(" S ", end= "")
        print("")
pattern_seven(5)

print("Pattern Eight")

def pattern_eight(n):
    for i in range(1, n + 1):
        for j in range(i - 1):
            print(" S ", end="")
        for j in range(2 * n - 2 * i + 1):
            print(" * ", end= "")
        for j in range(i - 1):
            print(" S ", end="")
        print("")
pattern_eight(5)


print("Pattern Nine")
def pattern_nine(n):
    pattern_seven(n)
    pattern_eight(n)

pattern_nine(5)


print("Pattern Eleven")
def pattern_eleven(n):
    start = 1
    for i in range(n):
        if i%2 ==0:
            start = 1
        else:
            start = 0
        for j in range(i + 1):
            print(start, end = " ")
            start = 1 - start
        print()

pattern_eleven(5)


print("Pattern Twelve")
def pattern_twelve(n):
    for i in range(1, n):
        for j in range(i):
            print(j, end = " ")
        for j in range(2*n - 2*i - 2):
            print(" ", end = " ")
        for j in range(i, 0 , -1):
            print( j , end= " ")
        print()
pattern_twelve(5)

print("Pattern Thirteen")
def pattern_thirteen(n):
    start = 1
    for i in range (1,n + 1):
        for j in range(i):
            print(start, end = "  ")
            start = start + 1
        print()
pattern_thirteen(5)




def pattern_three(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end = " ")
        print("")

pattern_three(5)

print("Pattern Fourteen")
def pattern_fourteen(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(65+ j), end= "")
        print("")
pattern_fourteen(5)


print("Pattern Fifteen")
def pattern_fifteen(n):
    for i in range(1 , n + 1):
        for j in range(0 , n - i + 1):
            print(chr(65 + j), end = "")
        print()
pattern_fifteen(5)


print(" Pattern Sixteen")
def pattern_sixteen(n):
    for i in range(1, n):
        for j in range(i + 1):
            print(chr(65 + i), end=" ")
        print()
pattern_sixteen(5)

print(" Pattern Seventeen")
def pattern_seventeen(n):
    for i in range(1, n):
        for j in range(n - 1 - i):
            print("*", end= " ")
        #     Middle
        for j in range(i):
            print(chr(65 + j ), end = " ")
        #     After middle
        for j in range(i - 1, 0, -1):
            print(chr(65 + j - 1 ), end=" ")
        for j in range(n - 1 - i):
            print("*", end=" ")
        print()
pattern_seventeen(5)


print(" Pattern Eighteen")

def pattern_eighteen(n):
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            print(chr(65 + n - j), end= " ")
        print()
pattern_eighteen(5)


print("Pattern Nineteen")

def pattern_nineteen(n):
    for i in range(n):
        for j in range(n - i):
            print(" * ", end= " ")
        for j in range(2 * i):
            print(" S ", end= " ")
        for j in range(n - i):
            print(" * ", end= " ")
        print("")
pattern_nineteen(5)

def pattern_nineteen_b(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(" * ", end=" ")
        for j in range(2 * (n - i)):
            print(" S ", end= " ")
        for j in range(i):
            print(" * ", end=" ")
        print("")

pattern_nineteen_b(5)

print(" Pattern TwentyOne")

def pattern_twentyone(n):
    for i in range(n):
        for j in range(n):
            if i == 0  or i == n-1 or j == 0 or j == n-1:
                print(" * ", end="")
            else:
                print(" S ", end= "")
        print("")

pattern_twentyone(5)

print(" Pattern TwentyTwo")
def pattern_twentytwo(n):
    for i in range(2 * n - 1):
        for j in range (2 * n - 1):
            top = i
            left = j
            right = (2 * n - 2) - j
            bottom = (2 * n -2) - i
            print(n- min(min(top, bottom), min(left,right)), end = "  ")
        print("")

pattern_twentytwo(4)
