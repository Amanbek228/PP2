#ex1
def func(grams):
    ounces = 28.3495231 * grams
    print(ounces)

func(2)

#ex2
def temp(fahren):
    cels=(5/9)*(fahren-32)
    print(cels)
temp(13)

#ex3
def farm(heads, legs):
    rab=(legs-2*heads)//2
    chick=heads-rab
    print("chicken =", chick, "rabbits =", rab)
farm(35, 94)

#ex4
def check_prime(i):
    for x in range(2, i):
        if i == 1:
            return False
        if i % x == 0:
            return False
    return True

list = [1, 3, 4, 5, 8, 12, 11]
def filter_prime(some_list):
    arr=[]
    for i in some_list:
        if check_prime(i) == True:
            arr.append(i)
    return arr
list1 = filter_prime(list)

#ex5
from itertools import permutations
st = input()
list1= list(permutations(st))
for x in list1:
    print(x)

#ex6
str = "abd fre der"
def convert(str):
    li = list(str.split(""))
    print(*li[::-1])
convert(str)

#ex7

def has_33(nums):
    for i in range(len(nums) -1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

has_33([1, 3, 3]) #→ True
has_33([1, 3, 1, 3]) #→ False
has_33([3, 1, 3]) #→ False

#ex8

a = list(map(int, input().split()))

def func(a):
    l = len(a)
    for i in range(l):
        if a[i]==0:
            for j in range(i+1, l):
                if a[j]==0:
                    for x in range(j+1, l):
                         match(a[x]):
                               case 0: return False
                               case 7: return True
    return False
print(func(a))

#ex9

def volume(rad):
    print(4/3 * 3.14 * rad**3)
volume(3)

#ex10
def unique(m):
    ans = []
    for i in m:
        if ans.count(i) == 0: 
            ans.append(i)
    return ans

print(unique(a))

#ex11

def ispalindrom(word):
    copy = word[::-1]
    if copy == word:
        return True
    return False
print(ispalindrom("abbad")) # false
print(ispalindrom("abba")) #true

#ex12
def histogram(arr):
    for i in arr:
        strin = '*'
        print(strin * i)
histogram([3, 4, 2])
 
#ex13
import random
def guess():
    number= random.randint(1, 21)
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.\n")
    count = 0
    for i in range(20):
        count +=1
        x = int(input("Take a guess.\n"))
        if x < number:
            print("Your guess is too low.\n")
        elif x > number:
            print("Your guess is too high.")
        elif x == number:
            print(f"Good job, {name}, You guessed my number in {count} guesses!")
            break
    
guess()