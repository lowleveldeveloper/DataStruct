import matplotlib.pyplot as plt

a=int(input("x range: "))

x = range(0,a)
y = [1/2**v for v in x]
plt.plot(x, y)
plt.show()
