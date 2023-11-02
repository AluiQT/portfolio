#!/opt/homebrew/bin/python3

fortnite = False
for i in range(0, 1000):
	for j in range(0, 1000):
		k = 1000 - i - j
		if i*i + j*j == k*k and (i*j*k) != 0:
			print(i * j * k)
			fortnite = True
			break  
	if fortnite == True:
		break
	