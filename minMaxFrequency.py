import random

def max_num(x):
    max = x[0]
    for i in x:
        if i > max:
            max = i
    return max


def min_num(x):
    min = x[0]
    for i in x:
        if i < min:
            min = i
    return min


def frequency_num(x):
    count_list=[]
    for i in x:
        count_list.append(x.count(i))
    frequency = max(count_list)
    num=[]
    for i in x:
        if x.count(i) == frequency and i not in num:
            num.append(i)
    return num, frequency


def frequency_num2(x):
    count_dict={}
    for i in x:
        count_dict[i] = x.count(i)
    max_frequency = max(count_dict.values())
    for key, value in count_dict.items():
        if max_frequency == value:
            print(f"max_frequency_number : {key} --> {value} times generated")
    return count_dict


### main ###
input_num = int(input("랜덤 숫자 생성 개수 입력:"))
x=[]
for i in range(input_num):
    a = random.randint(0,20)
    x.append(a)

print("max_num:{}".format(max_num(x)))
print("min_num:{}".format(min_num(x)))
print("x:{}".format(x))

print("max_frequency:{}".format(frequency_num(x)))
print("(number,frequency):{}".format(frequency_num2(x)))
