import matplotlib.pyplot as plt
xcor=10
ycor=10

x = range(0, 230)
y = [(230-ycor/230-xcor)*(i-230)+230for i in x]
plt.plot(x, y, 'ro')
