# Exercise 1: Create a function with variable length of arguments
# print all arguments...
def func1():
    #Your code

func1(20, 40, 60)
func1(80, 100)


# with variable length of arguments, sum all arguments & return total sum...
def sum1(*nums):
    a = 0
    for i in nums
        a+=i
    return a

sum1(20, 30, 40)
sum1(10,20)


# Exercise 2: Return multiple values from a function
def calculation(a, b):
   return a+b,a-b,a*b,a/b


# get result in tuple format
res = calculation(40, 10)
print(res)


#Exercise 3: Create a function with default argument
def show_employee(name="Shin", salary=10000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")
show_employee()

#Exercise 4: Create an inner function to calculate the addition
# outer function
def outer_fun(a, b, c):

    # inner function
    def add(a, b):
        return a + b

    def sub(a, b):
        return ????

    # call inner function from outer function
    # return a+b-c
    return ????

result = outer_fun(5, 10, 5)
print(result)


#Exercise 5: Create a recursive function  3 + 2 + 1 --> 6
def addition(num):
    if num:
        return num + addition(num -1)
    else:
        return 0


res = addition(3)
print(res)

def factorial(n):
    if n == 1:
        return 1
    elif n > 1:
        return n*factorial(n-1)

res = factorial(5)
print(res)

#Exercise 6: Generate a Python list of all the even numbers between 4 to 30
# expected output : [4,6,8,10,12,14,16,18,20,22,24,26,28]

def genEvenNum(from, to):
    resultList = []
    #Your Code

    return resultList


genEvenNum(4, 30)
