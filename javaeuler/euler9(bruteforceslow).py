#!/opt/homebrew/bin/python3

for i in range(0,1000):
	for j in range(0,1000):
		for k in range(0,1000):
			if i*i + j*j == k*k and i + j + k == 1000:
				print(i*j*k)
				break