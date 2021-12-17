import matplotlib.pyplot as plt

X=[[] for i in range(10)]

def collatz(i, N):
	if(N==0):
		return
	X[i].append(N)
	if(N==1):
		return 1
	elif not(N % 2):
		return collatz(i, N//2)
	else:
		return collatz(i, 3*N + 1)


for i in range(1, 10):
	collatz(i, i)

plt.figure()
for i in range(1, len(X)):
	print(X[i])
	plt.plot(X[i])

plt.show()
