#!/opt/homebrew/bin/python3

import math

n = 1999999
listToN = [True] * (n+1)

for num in range(2,n+1):
	if listToN[num] == True:
		for num2 in range(num * num,n + 1, num):
			listToN[num2] = False 

sumOfPrime = [num for num in range(2, n + 1) if listToN[num] == True]

print(sum(sumOfPrime))