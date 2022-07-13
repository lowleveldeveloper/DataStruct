import numpy as np

x=[2,4,6,8]
y=[81,93,91,97]

mx=np.mean(x)
my=np.mean(y)
print("x평균: ",mx)
print("y평균: ", my)

divisor = sum([(mx-i)**2 for i in x])

def top(x,mx,y,my):
    d = 0
    for i in range(len(x)):
        d += (x[i] - mx)*(y[i]-my)

    return d

dividend = top(x,mx,y,my)

print("분모: ",divisor)
print("분자: ",dividend)

a = dividend/divisor
b = my - (mx*a)

print("기울기 a: ",a)
print("y절편 b: ",b)
