#Author	:	Bhavya Singh
#Date	:	23-May-2020
#Name	:	Binary Number to Decimal Number


#PROBLEM:

Given a Binary Number B, Print its decimal equivalent.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follow. Each test case contains a single Binary number B. 

Output:
For each testcase, in a new line, print each Decimal number in new line.

Constraints:
1 <= T <= 100
1 <= Digits in Binary <= 16

Example:
Input:
2
10001000
101100
Output:
136
44

#CODE

T = int( input() )
for i in range( T ):
    B = int(input(), 2)
    print( B )