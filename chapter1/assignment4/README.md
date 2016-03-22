#Assignment 4
##Problem
I chose problem 1.4 of chapter 1.
##Abstract
In this assignment I wrote a program using the Euler method to solve a radioactive decay problem involving two types of nuclei A and B, where nuclei of type A decay into type B ones. With the program I researched the behavior of the nuclei in various initial conditions.
##Code
-  [assignment4](https://github.com/aragornranger/computationalphysics_N2013301020051/blob/master/chapter1/assignment4/asgmnt4_4.py)
##Calculation
The pattern of the decay processes of two types of nuclei can be described by the following differential equations:
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN_A%7D%7Bdt%7D%20%3D%20-%20%5Cfrac%7BN_A%7D%7B%5Ctau_A%7D)
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN_B%7D%7Bdt%7D%20%3D%20%5Cfrac%7BN_A%7D%7B%5Ctau_A%7D%20-%20%5Cfrac%7BN_B%7D%7B%5Ctau_B%7D)
where ![](http://latex.codecogs.com/gif.latex?\tau_A) and ![](http://latex.codecogs.com/gif.latex?\tau_A) are the decay time constants. Using Tayler expansion we ca obtain:
![](http://latex.codecogs.com/gif.latex?N_A%28t&plus;%5CDelta%20t%29%20%5Capprox%20N_A%28t%29%20-%20%5Cfrac%7BN_A%28t%29%7D%7B%5Ctau%7D%5CDelta%20t)
![](http://latex.codecogs.com/gif.latex?N_B%28t&plus;%5CDelta%20t%29%20%5Capprox%20N_B%28t%29%20&plus;%20%5Cfrac%7BN_A%28t%29%7D%7B%5Ctau%7D%5CDelta%20t%20-%20%5Cfrac%7BN_B%28t%29%7D%7B%5Ctau%7D%5CDelta%20t)
With these two equations, given the initial conditions, it's easy to calculate the number of nuclei at a given time t.
##Result
![](https://raw.githubusercontent.com/aragornranger/computationalphysics_N2013301020051/master/pictures/chapter1/1000%2C1000%2C2%2C2.png)
figure with ![](http://latex.codecogs.com/gif.latex?N_A=N_B=1000), ![](http://latex.codecogs.com/gif.latex?\tau_A=\tau_B=2).
##More discussion
After trying multiple sets of initial conditions I noticed that the number of nuclei of type B would vary in two different ways. Blow are some examples:
![](https://raw.githubusercontent.com/aragornranger/computationalphysics_N2013301020051/master/pictures/chapter1/500%2C1000%2C2%2C2.png)
![](http://latex.codecogs.com/gif.latex?N_A=500,N_B=1000,\tau_A=2,\tau_B=2)
![](https://raw.githubusercontent.com/aragornranger/computationalphysics_N2013301020051/master/pictures/chapter1/1000%2C500%2C2%2Cpoint5.png)
![](http://latex.codecogs.com/gif.latex?N_A=1000,N_B=500,\tau_A=2,\tau_B=0.5)
![](https://raw.githubusercontent.com/aragornranger/computationalphysics_N2013301020051/master/pictures/chapter1/1000%2C500%2C2%2C10.png)
![](http://latex.codecogs.com/gif.latex?N_A=1000,N_B=500,\tau_A=2,\tau_B=10)
When ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BN_A%7D%7BN_B%7D%3E%5Cfrac%7B%5Ctau_A%7D%7B%5Ctau_B%7D), the number of type B nuclei would increase at first and then decrease after it reaches a maximum. When ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BN_A%7D%7BN_B%7D%3C%5Cfrac%7B%5Ctau_A%7D%7B%5Ctau_B%7D), it would go down directly without any increasing process.
##Acknowledgement
I give my thanks to writer of [Matplotlib 教程 | 始终](http://liam0205.me/2014/09/11/matplotlib-tutorial-zh-cn/), which helped me a lot when I learn how to use matplotlib.

> Written with [StackEdit](https://stackedit.io/).