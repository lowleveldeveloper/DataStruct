#Exceptions
'''
import error
index error
name error
syntax error
type error
value error
'''

#exception handling
'''
try:                        #익셉션일어날때 트라이 중지, 익셉션 작동
    n1=7
    n2=0
    print(n1/n2)
    print("done calculation")
except ZeroDivisionError:   #에러 없으면 익셉션 작동 안함
    print("An error occurred")
    print("due to zero division")
'''
'''
try:
    var=10
    print(var+"hello")
    print(var/2)
    
except ZeroDivisionError:
    print("Division by zero")
    
except (ValueError,TypeError):
    print("Error occurred")
'''
'''
try:
    word = 'spam'
    print(word/0)
except:                      #모든 에러 잡음.
    print('An error occurred')
'''

#Finally
'''
try:
    print("hi")
    print(1/0)
except ZeroDivisionError:
    print("divided by zero")
finally:
    print("This code will run no matter what")
'''

#Rising exceptions
'''
print(1)
raise ValueError
print(2)
'''
'''
name="123"
raise NameError("Invalid name")
'''
'''
try:
    num = 5/0
except:
    print("An error occurred")
    raise
'''

#Assertions
'''
print(1)
assert 2+2==4
print(2)
assert 1+1==3
print(3)
'''
'''
temp= -10                      ####
assert (temp >= 0), "colder than absoute zero" #try-except와 같이 작동

'''


#opening files
'''
file=open("textname.txt","w")
file.close()
'''
'''
file = open("textname.txt")
con = file.read()               #()안에 숫자쓰면 바이트단위로 읽음
print(con)
file.close()
'''

'''
file = open("textname.txt","r")
print(file.readlines())
file.close()
'''
'''
file=open("textname.txt","r")#1라인 엔터 2라인
for line in file:
    print(line)
file.close()
'''

#writing files
'''
file= open("textname.txt","w") #초기화후 라이팅
file.write("mintickingarea")
file.close()
file=open("textname.txt")
print(file.read())
file.close()
'''
'''
msg = "hello world"
file = open("textname.txt","w")
amount_written = file.write(msg)  #filewrite를 저장해 글자 수 출력
print(amount_written)
file.close()
'''

#working with files
'''
try:                        #매번 번거로우므로 try문 사용
    f = open("textname.txt")
    print(f.read())
finally:
    f.close()
'''
'''
with open("textname.txt") as f:       ####
    print(f.read())
'''
