#None
'''
print(None) #None

def some_func():
    print("hi")
var = some_func()
print(var) #None/ 리턴값이 없음
'''

#Dictionaries
'''
ages = {"dave":24,"mary":42}
print(ages["dave"])
'''
'''
bad_dict ={[1,2,3]:"one two three"}#리스트타입(가변형)존재해서 에러남.(just key?)
'''
'''
sq={1:2,2:4,3:"error",4:16}
sq[8]=64
sq[3]=9
print(sq) #error와 16값이 변함/가치만 변함 (키는 어캐 할당?)
'''
'''
n={1:"one",2:"two",3:"three"} #key 존재 여부
print(1 in n)
print(4 not in n)
'''
'''
pairs={1:"apple","orange":[2,3,4],True:False,None:True}#key불변/value가변
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345,"not in dictionary"))   #####
'''

#tuple
'''
words=('spam','eggs')
print(words[0])
words[1]="cheese"   #불변형이라 타입에러뜸.
'''
'''
crazy_tuple="one","two","three"  #괄호없이 생성가능
print(crazy_tuple[0])
'''
'''
#list slices
sq = [1,2,3,4,5,6,7,8,9,10]
print(sq[:6])                   #1~6
print(sq[6:])                   #7~10

print(sq[::2])                  #13579
print(sq[2:8:3])                #36

print(sq[1:-1])                 #2~9
print(sq[::-1])                 #reverse
'''

#List Comprehensions
'''
cubes = [i**3 for i in range(5)]
print(cubes)

evens = [a**2 for a in range(10) if a**2%2 == 0]
print(evens)
'''

#string formatting
'''
nums = [4,5,6]
msg = "Numbers: {0} {1} {2}".format(nums[0],nums[1],nums[2])          
print(msg)


a="{x},{y}".format(x=12,y=5)          ####
print(a)
'''

#useful functions
'''
print(",".join(["spam","egg"]))             ####

print("hello me".replace("me","world"))

print("this is a sentence.".startswith("this"))

print("this is a sentence.".endswith("sentence"))

print("this is a sentence.".upper())

print("AN ALL CAPS SENTENCE".lower())

print("spam,egg,ham".split(","))
'''

'''
print(min(3,5,6,0))
print(max(1,6,7,8,4))
print(abs(-22))
print(abs(22))
print(sum([1,2,3,4,5,6,7,8,9]))   ##리스트만?
'''

'''
nums = [55,44,33,22,11]

if all([i>5 for i in nums]):
    print("all larger than 5")

if any([i%2 == 0 for i in nums]):
    print("at least one is even")

for v in enumerate(nums):          #(index,value) output
    print(v)
'''

#text analyzer
'''
filename = input("enter a filename: ")

with open(filename) as f:           #close 안함?
    text = f.read()
print(text)
'''
'''
def count_char(text,char):               ####
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

filename = input("enter a filename: ")
with open(filename) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100*count_char(text,char)/len(text)
    print("{0}-{1}%".format(char,round(perc,2)))   #round?
'''

