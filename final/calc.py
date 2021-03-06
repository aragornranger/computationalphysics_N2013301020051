import numpy as np
import matplotlib.pyplot as plt

class nuclei:
    nu = []
    base = []
    t = []
    step = 0
    n = 0
    tau = 0
    
    def __init__(self,n,tau,step):
        self.nu = []
        self.t = [] 
        self.nu.append(n)
        self.t.append(0)
        self.tau = tau
        self.step = step
        self.n = n
        
    def exact(self,t):
        self.base = []
        self.base.append(self.n)
        for i in range(int(t / self.step)):
            tmp = np.exp(-float(self.step * (i + 1)) / float(self.tau))
            self.base.append(self.nu[0] * tmp)
            
    def euler(self,t):
        self.__init__(self.n,self.tau,self.step)
        for i in range(int(t / self.step)):
            self.nu.append(self.nu[-1] - self.nu[-1] / self.tau * self.step)
            tmp = self.t[-1] + self.step
            self.t.append(tmp)

    def rk(self,t):
        self.__init__(self.n,self.tau,self.step)
        for i in range(int(t / self.step)):
            k1 = -float(self.nu[-1]) / float(self.tau)
            k2 = -(float(self.nu[-1]) + float(self.step) / 2.0 * k1) / float(self.tau)
            k3 = -(float(self.nu[-1]) + float(self.step) / 2.0 * k2) / float(self.tau)
            k4 = -(float(self.nu[-1]) + float(self.step) * k3) / float(self.tau)
            self.nu.append(self.nu[-1] + float(self.step) / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4))
            self.t.append(self.t[-1] + self.step)

    def emm(self,t):
        self.__init__(self.n,self.tau,self.step)
        for i in range(int(t / self.step)):
            tmp = -float(self.nu[-1]) / float(self.tau)
            self.nu.append(self.nu[-1] + self.step * (-float(self.nu[-1] + float(self.step) / 2.0 * tmp) / float(self.tau)))
            self.t.append(self.t[-1] + self.step)        
    
    
