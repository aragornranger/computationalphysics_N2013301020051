cap =[
    ['   *   ','  * *  ',' ***** ',' *   * ',' *   * '],            #A
    [' ****  ',' *   * ',' ****  ',' *   * ',' ****  '],              #B
    ['  **** ',' *     ',' *     ',' *     ','  **** '],              #C
    [' ***   ',' *  *  ',' *   * ',' *  *  ',' ***   '],              #D
    [' ***** ',' *     ',' ***** ',' *     ',' ***** '],              #E
    [' ***** ',' *     ',' ****  ',' *     ',' *     '],              #F
    ['  ***  ',' *     ',' *  ** ',' *   * ','  ***  '],              #G
    [' *   * ',' *   * ',' ***** ',' *   * ',' *   * '],              #H
    ['  ***  ','   *   ','   *   ','   *   ','  ***  '],              #I 
    ['  ***  ','   *   ','   *   ','   *   ','  *    '],              #J
    [' *   * ',' *  *  ',' ***   ',' *  *  ',' *   * '],              #K  
    [' *     ',' *     ',' *     ',' *     ',' ***** '],              #L
    ['*     *','**   **','* * * *','*  *  *','*  *  *'],              #M
    [' *   * ',' **  * ',' * * * ',' *  ** ',' *   * '],              #N
    ['  ***  ',' *   * ',' *   * ',' *   * ','  ***  '],              #O
    [' ****  ',' *   * ',' ****  ',' *     ',' *     '],              #P
    ['  ***  ',' *   * ',' *   * ',' *  ** ','  *** *'],              #Q
    [' ***   ',' *   * ',' ***   ',' * *   ',' *   * '],              #R
    ['  ***  ',' *     ','  ***  ','     * ','  ***  '],              #S
    [' ***** ','   *   ','   *   ','   *   ','   *   '],              #T
    [' *   * ',' *   * ',' *   * ',' *   * ','  ***  '],              #U
    [' *   * ',' *   * ',' *   * ','  * *  ','   *   '],              #V
    ['*  *  *','*  *  *','* * * *','**   **','*     *'],              #W
    [' *   * ','  * *  ','   *   ','  * *  ',' *   * '],              #X
    [' *   * ','  * *  ','   *   ','   *   ','   *   '],              #Y
    [' ***** ','    *  ','   *   ','  *    ',' ***** ']]              #Z
 
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

#a maximum of ten chars are allowed per line
line = len(letters) // 10
if len(letters) % 10 != 0:
    line += 1

output = [['' for i in range(5)] for j in range(line)]


for i in range(len(letters)):
    for j in range(5):
        if letters[i] == ' ':
            output[i // 10][j] += '      '
            continue
        output[i // 10][j] += cap[ord(letters[i]) - ord('A')][j] + ' '

for i in range(line):
    for j in range(5):
        print output[i][j]

