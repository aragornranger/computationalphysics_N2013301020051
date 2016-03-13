cap =[['  *  ',' * * ','*****','*   *','*   *'],
    ['**** ','*   *','**** ','*   *','**** '],
    [' ****','*    ','*    ','*    ',' ****'],
    ['***  ','*  * ','*   *','*  * ','***  '],
    ['*****','*    ','*****','*    ','*****'],
    ['*****','*    ','**** ','*    ','*    '],
    [' *** ','*    ','*  **','*   *',' *** '],
    ['*   *','*   *','*****','*   *','*   *'],
    [' *** ','  *  ','  *  ','  *  ',' *** '],
    [' *** ','  *  ','  *  ','  *  ',' *   '],
    ['*   *','*  * ','***  ','*  * ','*   *'],
    ['*    ','*    ','*    ','*    ','*****'],
    ['*     *','**   **','* * * *','*  *  *','*  *  *'],
    ['*   *','**  *','* * *','*  **','*   *'],
    [' *** ','*   *','*   *','*   *',' *** '],
    ['***  ','*  * ','***  ','*    ','*    '],
    [' ***  ','*   * ','*   * ','*  ** ',' *** *'],
    ['***  ','*   *','***  ','* *  ','*   *'],
    [' ****','*    ',' *** ','    *','**** '],
    ['*****','  *  ','  *  ','  *  ','  *  '],
    ['*   *','*   *','*   *','*   *',' *** '],
    ['*   *','*   *','*   *',' * * ','  *  '],
    ['*  *  *','*  *  *','* * * *','**   **','*     *'],
    ['*   *',' * * ','  *  ',' * * ','*   *'],
    ['*   *',' * * ','  *  ','  *  ','  *  '],
    ['*****','   * ','  *  ',' *   ','*****'],]
 
#initialization

legal = 0

while legal == 0:

    legal = 1
    letters = raw_input("The letters you want to print:\n")
    #input the letters you want to diplay
    letters = letters.upper()
    #can only display captial letters

    for i in letters:
        if (ord(i) != ord(' ')) and (not (ord('A') <= ord(i) <= ord('Z')) and not(ord('a') <= ord(i) <= ord('z'))):
            legal = 0
            print('Error!Only letters and spaces can be displayed.')
            break;
    #check if all chars input are letters or spaces

output = ['','','','','']


for i in letters:
    for j in range(5):
        if i == ' ':
            output[j] += '      '
            continue
        output[j] +=  cap[ord(i) - ord('A')][j] +  ' '

for i in range(5):
    print output[i]

