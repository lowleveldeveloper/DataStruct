import collections
import random
import statistics

x = []
randomNum_num = int(input("Enter: "))
val = [randomNum_num]

def rand(x):
    for i in range(randomNum_num):
        randomNum = random.randrange(0,20)
        x.append(randomNum)
    return x

val = rand(x)

print(val)

def many(val):
    count = 0
    for i in range(len(val)):
        for j in range(i):
            if val[i] == val[j]:
                count +=1
                return val[i]

def fre(y):
    answer = []
    getmax = 0
    y1 = set(y)
    for i in y1:
        fe = y.count(i)
        if getmax < fe:
            getmax = fe
            answer = []
            answer.append(i)
        elif getmax == fe:
            answer.append(i)
    answer.sort()
    print(answer)


print("method 1: ", many(val))

print("method 2: ", fre(val))

#### method 3
dict = collections.Counter(val)
print(dict)

freqValue = max(dict.values())

# 이준현 학생 코드 수정본...
def get_key(val):
    f_list = []    # 최빈값을 저장하는 리스트 생성
    for key, value in dict.items():
        if val == value:
            f_list.append(key)

    return f_list  # 최빈값들로 구성된 리스트 리턴...

print("method 3: ", get_key(freqValue))

#### method 4
#print("method 4: ", statistics.mode(val))
#print("method 4: ", statistics..multimode(val))  # from Python 3.8

#### method 5
val.sort()
print(val)
print("method 5: ", max(val, key=val.count))
