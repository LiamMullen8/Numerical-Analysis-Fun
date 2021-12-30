import multiprocessing

import matplotlib.pyplot as plt
import time
from multiprocessing import Process


def collatz(Map, i, N):
	#Z+ positive integers only :) double check just to be sure ^^
	if N <= 0:
		raise Exception("Z+ positive integers only :)")

	# total O(n) lookup => each dict is O(1), iter thru list of dicts
	for s in range(1, i):
		if N in Map[s]:
			# X[i].append(0)
			return

	# add N to dict, dict maintains order
	(Map[i])[N] = None
	print(Map)
	# base case 1 => infinite cycle begins
	if N == 1:
		return 1

	# even
	elif not(N % 2):
		return collatz(Map, i, N // 2)

	# odd
	else:
		return collatz(Map, i, 3 * N + 1)

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

# Split input between desired number of processes
def split_process(Map, start, stop):
	for i in range(start, stop):
		collatz(Map, i, i)
	print(Map)


if __name__ == "__main__":

	L = int(input("Enter Range of Test Values: "))
	if L <= 0:
		raise Exception("Z+ positive integers only :)")

	# global so graph() and collatz() can access
	X = [{} for _ in range(L)]

	manager = multiprocessing.Manager()
	x = manager.list(X)

	# for i in range(0,L):
	# 	X.append({})
	t1 = Process(target=split_process, args=(x, 1, L//4))
	t2 = Process(target=split_process, args=(x, L//4, L//2))
	t3 = Process(target=split_process, args=(x, L//2, (3*L)//4))
	t4 = Process(target=split_process, args=(x, (3*L)//4, L))

	q1 = time.monotonic()
	t1.start()
	t2.start()
	t3.start()
	t4.start()

	t1.join()
	t2.join()
	t3.join()
	t4.join()
	q2 = time.monotonic()

	print(f"Multi-Processing Time for Collatz up to {L}: ~{q2-q1} seconds")

	# q1 = time.monotonic()
	# for i in range(1, L):
	# 	collatz(i, i)
	# q2 = time.monotonic()

	# print(f"Single thread Time for Collatz up to {L}: ~{q2 - q1} seconds")
	# q2 = time.thread_time()
	# print(f"Multi-thread Time for Collatz up to {L}: ~{q2} seconds")


	# # finding collapsing odds
	# q3 = time.perf_counter()
	# print(f"Collapsing Odds within Range {L}: {collapsing_odds(L)} seconds")
	# q4 = time.perf_counter()
	# print(f"Time for checking odds up to {L}: {q4-q3} seconds")
	#
	# plt.figure()
	print(x)
	for i in x:
		print(i)
	# 	plt.plot(i.keys())
	#
	# plt.xlabel("time step (n)")
	# plt.ylabel("output f(n)")
	# plt.title("3N+1")
	# plt.show()
