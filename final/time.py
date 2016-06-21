import calc as ca
import time as ti

# euler;rk;emm;exact

test = ca.nuclei(10000,100,0.01)
test.exact(1000)

rs = []
tim = []

start = ti.clock()
test.euler(1000)
end = ti.clock()
tot = 0
for j in range(len(test.nu)):
    tot += (test.base[j] - test.nu[j]) * (test.base[j] - test.nu[j])
tot = tot / float(len(test.nu))
rs.append(tot)
tim.append(end - start)
    
start = ti.clock()
test.rk(1000)
end = ti.clock()
tot = 0
for j in range(len(test.nu)):
    tot += (test.base[j] - test.nu[j]) * (test.base[j] - test.nu[j])
tot = tot / float(len(test.nu))
rs.append(tot)
tim.append(end - start)

start = ti.clock()
test.emm(1000)
end = ti.clock()
tot = 0
for j in range(len(test.nu)):
    tot += (test.base[j] - test.nu[j]) * (test.base[j] - test.nu[j])
tot = tot / float(len(test.nu))
rs.append(tot)
tim.append(end - start)

ca.plt.scatter(tim[0],rs[0],marker = "o",label = "euler")
ca.plt.scatter(tim[1],rs[1],marker = "s",label = "runge-kutta")
ca.plt.scatter(tim[2],rs[2],marker = "*",label = "emm")
ca.plt.legend(loc = "upper right")
ca.plt.show()

    
