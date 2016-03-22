from pylab import *

na = []
nb = []
t = []

na.append(input("Input the initial number of nuclei type A:"))
nb.append(input("Input the initial number of nuclei type B:"))
taua = input("Input the time constant of nuclei type A:")
taub = input("Input the time constant of nuclei type B:")
step = input("Input the step for the calculation:")
time = input("Input the total time:")
t.append(0)
#initialization

for i in range(int(time / step)):
    tmpa = na[i] - na[i] / taua * step
    tmpb = nb[i] + (na[i] / taua - nb[i] / taub) * step
    na.append(tmpa)
    nb.append(tmpb)
    t.append(t[i] + step)
#calculation

plot(t, na, color = "blue", label = "A")
plot(t, nb, color = "red", label = "B")

ymax = max(max(na),max(nb))
legend(loc = 'upper right')
xticks(np.linspace(0,time,10))
yticks(np.linspace(0,ymax * 1.1,8))
xlabel('Time(s)')
ylabel('Number of nuclei')
title('Radioactive decay problem involving two types of nuclei')
ylim = (0,ymax * 1.1)
xlim = (0,time)
grid()


show()
