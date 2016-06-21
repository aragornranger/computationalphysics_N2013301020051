import calc as ca

test = ca.nuclei(1000,10,1)
test.exact(10)
test.euler(10)
ca.plt.plot(test.t,test.nu,label = "euler",color = "blue")
ca.plt.plot(test.t,test.base,label = "exact",color = "black")
test.rk(10)
ca.plt.plot(test.t,test.nu,label = "r-k",color = "red")
test.emm(10)
ca.plt.plot(test.t,test.nu,label = "mid-point",color = "green")

ca.plt.legend(loc = "upper right")
ca.plt.show()
