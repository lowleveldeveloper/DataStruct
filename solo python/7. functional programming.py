#Functional Programming
'''
def apply_twice(func,arg):
    return func(func(arg))

def add_five(x):
    return x+5

print(apply_twice(add_five,10))
'''
'''
def pure_function(x,y):       #pure
    temp=x+2*y
    return temp/(2*x+y)


some_list=[]

def impure(arg):              #impure ??
    some_list.append(arg)
'''
'''
#Lambdas
def my_func(f,arg):
    return f(arg)

my_func(lambda x: 2*x*x, 5)          ####what is lambda?
'''
'''
def poly(x):                     #named function
    return x**2+5*x+4
print(poly(-4))

print(lambda x: x**2+5*x+4(-4))  #lambda
'''
'''
d=lambda x:x*2
print(d(7))
'''

#map and filter
'''
def add_five(x):
    return x+5

nums = [11,22,33,44,55]
result=list(map(add_five,nums))    #함수에 리스트갑대입 반복 ***
print(result)


reresult=list(map(lambda x: x+5,nums)) #람다로 간략화
print(reresult)
'''
'''
nums=[11,22,33,44,55]
res=list(filter(lambda x:x%2 == 0,nums)) #식에 맞는거만 추출
print(res)
'''

#generator
'''
def countdown():
    i=5
    while i > 0:
        yield i           #???
        i -= 1

for i in countdown():
    print(i)
'''
'''
def infinite():
    while True:
        yield 7
for i in infinite():
    print(i)
'''
'''
def n(x):
    for i in range(x):
        if i%2 == 0:
            yield i         #대충 생성자는 빠르다
print(list(n(11)))
'''

#decorators
'''
a=input("decorator: ")        #데코함수에 텍스트함수 넣기
def decor(func):
    global a
    def wrap():
        print("====")
        func()
        print("====")
    return wrap
def print_text ():
    global a
    print(a)

decorated = decor(print_text)
decorated()


@decor             #none막줄에 나옴오류/ @통해서 데코가능 ***
def printf ():
    global a
    print(a)
print(printf())
'''

#recursion                ****
'''
def fac(x):
    if x == 1:
        return 1
    else:
        return x*fac(x-1) #......

print(fac(10))
'''
'''
def iseven(x):               #??????
    if x == 0:
        return True
    else:
        return isodd(x-1)
def isodd(x):
    return not iseven(x)

print(isodd(17))
print(iseven(23))
'''

#sets  추가내용 필요
'''
num_set={1,2,3,4,5}
word_set=set(["spam"])
print(3 in num_set) #add/remove특정/pop임의
'''
'''
fir={1,2,3,4,5,6}
sec={4,5,6,7,8,9}

print(fir | sec) #합집합
print(fir & sec) #교집합
print(fir - sec) #차집합
print(sec - fir)
print(fir ^ sec) #합집합-교집합
'''

#itertools
'''
from itertools import count

for i in count(3):
    print(i)
    if i >= 11:
        break
'''
'''
from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))    #accumulate???
print(nums)
print(list(takewhile(lambda x: x<=6,nums)))
'''
'''
from itertools import product,permutations

letters=("a","b")
print(list(product(letters,range(2))))#튜플각요소+범위조합   ****
print(list(permutations(letters)))#튜블요소로 가능한 집합들
'''
