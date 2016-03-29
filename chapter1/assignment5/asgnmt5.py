from pylab import *

v = []
t = []

v.append(input("Input the initial speed:"))
a = input("Input a:")
b = input("Input b:")
step = input("Input the step for the calculation:")
time = input("Input the total time:")
t.append(0)
#initialization

for i in range(int(time / step)):
    tmpv = v[i] + (a - b * v[i]) * step
    v.append(tmpv)
    t.append(t[i] + step)
#calculation

plot(t, v, color = "blue", label = "v")

ymax = max(v)
legend(loc = 'upper right')
xticks(np.linspace(0,time,10))
yticks(np.linspace(0,ymax * 1.1,8))
xlabel('Time(s)')
ylabel('Speed of the parachute(m/s)')
title('Frictional force problem')
ylim = (0,ymax * 1.1)
xlim = (0,time)
grid()


show()
