"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
   
   
   
   """打印三角形"""
line = 5
for i in range(1, line + 1):
    print('* ' * i)
print()

for i in range(1, line + 1):
    print((line - i) * ' ' + '*' * i)
print()

# for i in range(1, line + 1):
#     print(' ' * (line - i) + '* ' * i)
# print()

for i in range(line):
    print(' ' * (line - i) + '*' * (2 * i + 1))
