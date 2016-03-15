#Assignment 3
##Code
[stringdisplay.py](https://github.com/aragornranger/computationalphysics_N2013301020051/blob/master/assignment3/stringdisplay.py)

##Description
I used a list `cap` to store the pattern for each letter. Through finding the difference between the ASCII number of a particular letter and A, the pattern can be visited. And to print the letters I used another list `output`. To print letters in multiple lines, I initialized `output` with 
```python
output = [[' ' for i in range(5)] for j in line]
```
Variable `line` indicates how many lines I needed to print all letters out, and `rang(5)` suggests that all patterns are five lines in height.
Then after connecting all letters together in `output`,  it can be printed correctly with simply a `for` statement.

##Example

![](https://raw.githubusercontent.com/aragornranger/computationalphysics_N2013301020051/master/pictures/EXP_ASMT3.png)



> Written with [StackEdit](https://stackedit.io/).
