import matplotlib.pyplot as plt
import math
import time

L = int(input("Enter Range of Test Values: "))
#global so graph() and collatz() can access
X=[[] for i in range(L)]


def collatz(i, N):
	
	#Z+ positive integers only :)
	if(N <= 0):
		return
	
	for s in range(1,i):
		if N in X[s]:
			X[i].append("REP")
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
	for i in range(1, L):
		collatz(i, i)

	plt.figure()
	for i in X:
		print(i)
		plt.plot(i)

	plt.xlabel("time step (n)")
	plt.ylabel("output f(n)")
	plt.title("3N+1")
	plt.show()
	return


if __name__ == "__main__":
	q1=time.monotonic()
	print(f"Collapsing Odds within Range {L}: {collapsing_odds(L)}")
	q2=time.monotonic()
	print(f"Time for checking odds up to {L}: {q2-q1}")
	graph()
