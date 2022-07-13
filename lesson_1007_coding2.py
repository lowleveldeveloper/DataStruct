# Exercise 1: Create a function with variable length of arguments
# print all arguments...
def func1(a, b, *args):
    #Your code
    for i in args:
        print(i)

func1(20, 40, 60, 80, 100)
#func1(80, 100)

# with variable length of arguments, sum all arguments & return total sum...
def sum1(*args):
    # Your code
    a = 0
    for i in args:
        a += i
    return a

print("total sum:", sum1(20, 30, 40))
print("total sum:", sum1(20, 30, 40, 50, 60))


### input????
a = 1
b = 2
c = -8

# ( a * x^2 ) + ( b * x ) + c = 0
r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
### output???
print('해는', r1, '또는', r2)
# return r1, r2
#####
def get_Root2Deq(a,b,c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return r1, r2

a = 1
b = 2
c = -8
root1, root2 = get_Root2Deq(a,b,c)
print('해는', root1, '또는', root2)

# Exercise 2: Return multiple values from a function
def calculation(a, b):
    #Your Code : 사칙연산 수행(a+b, a-b, a*b, a/b) 후 결과 리턴
    #return multiple values separated by comma
    return a+b, a-b, a*b, a/b

# get result in tuple format
#res = calculation(40, 10)
add, sub, multi, div = calculation(40, 10)
print(add, sub, multi, div)

res = calculation(40, 10)
print(res)
print(res[0])
