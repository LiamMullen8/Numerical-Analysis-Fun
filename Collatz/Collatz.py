import matplotlib.pyplot as plt
import math
import time

#global so graph() and collatz() can access
X=[[] for i in range(10)]


def collatz(i, N):
	
	#Z+ positive integers only :)
	if(N <= 0):
		return
	
	X[i].append(N)
	
	# base case 1 infinite cycle begins
	if(N==1):
		return 1
	
	# even
	elif not(N % 2):
		return collatz(i, N//2)
	
	# odd
	else:
		return collatz(i, 3*N + 1)


## check all odds up to some limit N
def collapsing_odds(N):
	odds=[]
	for i in range(1, N, 2): 
		
		# INITIAL APPROACH
		# x = 3*i + 1
		# y = math.log(x,2)
		# if y.is_integer():
		# 	odds.append(i)

		# SLIGHTLY REFINED
		# if (math.log(3*i + 1, 2)).is_integer():
		# 	odds.append(i)

		# FAST BITWISE APPROACH :)
		n = 3*i + 1
		if n and not(n & (n-1)):
			odds.append(i)
			print(f"Power of Two: {n}, Collapsing Odd: {i}")

	return odds


def graph():
	for i in range(1, 10):
		collatz(i, i)

	plt.figure()
	for i in range(1, len(X)):
		print(X[i])
		plt.plot(X[i])

	plt.show()


if __name__ == "__main__":
	# graph()
	q1=time.monotonic()
	print(collapsing_odds(1000000))
	q2=time.monotonic()
	print(f"Time for checking odds up to 1 million: {q2-q1}")
