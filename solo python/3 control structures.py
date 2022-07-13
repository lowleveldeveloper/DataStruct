'''
num=3
if num == 1:
    print("a")
elif num == 2:  #1아니고 2라면, if-else 축약형
    print("b")
elif num == 3:
    print("c")
else:
    print("s")
'''
'''
if (1==1)and(4>3): #둘다 트루니 true
    print("true")
else:
    print("false")
    
if (1!=1)or(4>3): #둘중 하나가 트루니 true
    print("true")
else:
    print("false")

if (not 1==1) == True: #(not 1==1)은 폴즈다.
    print("true")
else:
    print("false")
'''
'''
grade=88
if (grade >= 70 and grade <=100): #활용
    print("passed")
'''
'''
Str = "hello world"
print(Str[4])
'''
'''
words = ["python","fun"]
index =1
words.insert(index,"is")
print(words)
'''
'''
letters = ['p','q','r']
print(letters.index('r'))#위치 표시/max(list),min,count,remove,reverse
'''
'''
stri = "testing for loops"
count = 0

for x in stri:
    if (x == 't'):
        count += 1

print(count)
'''
'''
num=list(range(10))
print(num)
'''
'''
num=list(range(1,11,2)) #1357
print(num)
'''

