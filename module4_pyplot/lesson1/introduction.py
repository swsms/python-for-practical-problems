import matplotlib.pyplot as plot
import math

fig = plot.figure()

plot.axis([0, 10, -1.5, 1.5])
plot.xlabel('x')
plot.ylabel('sin(x)')

xs = []
sin_vals = []

x = 0.0
while x < 10.0:
    sin_vals.append(math.sin(x))
    xs.append(x)
    x += 0.01

plot.plot(xs, sin_vals)

fig.savefig('./module4_pyplot/lesson1/sin.png')
