import matplotlib.pyplot as plt
import time

L = int(input("Enter Range of Test Values: "))
if L <= 0:
	raise Exception("Z+ positive integers only :)")

#global so graph() and collatz() can access
X = [{} for i in range(L)]


def collatz(i, N):
	
	#Z+ positive integers only :) double check just to be sure ^^
	if N <= 0:
		raise Exception("Z+ positive integers only :)")

	# add N to dict, dict maintains order
	(X[i])[N] = None

	# total O(n) lookup => each dict is O(1), iter thru list of dicts
	for s in range(1, i):
		if N in X[s]:
			# X[i].append(0)
			return


	# base case 1 infinite cycle begins
	if N == 1:
		return 1
	
	# even
	elif not(N % 2):
		return collatz(i, N//2)
	
	# odd
	else:
		return collatz(i, 3*N + 1)


## check all odds up to some limit N
def collapsing_odds(N):

	odds = []

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


def run_collatz():

	q1 = time.perf_counter()
	for i in range(1, L):
		collatz(i, i)
	q2 = time.perf_counter()
	print(f"Time for Collatz up to {L}: {q2-q1} seconds")

	# for i in X:
	# 	print(i.keys())

	# plt.figure()
	# for i in X[1:]:
	# 	# print(f"{i[0]}: {i}")
	# 	plt.plot(i)
	#
	# plt.xlabel("time step (n)")
	# plt.ylabel("output f(n)")
	# plt.title("3N+1")
	# plt.show()


	return


if __name__ == "__main__":

	# finding collapsing odds
	q3 = time.perf_counter()
	print(f"Collapsing Odds within Range {L}: {collapsing_odds(L)} seconds")
	q4 = time.perf_counter()
	print(f"Time for checking odds up to {L}: {q4-q3} seconds")

	# collatz up to L
	run_collatz()