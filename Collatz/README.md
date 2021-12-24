# Collatz Conjecture #

- proposed by Lothar Collatz (1910-1990)
```
Rules: 
if N is odd,  F(N) = 3*N + 1
if N is even, F(N) = N / 2 
```

By following these two simple rules/arithmetic operations, it is conjectured that every natural number will collapse down to 1.

In other words, you can pick any integer from 1 to infinity and the sequence will always reach 1.
* Upon reaching 1, the sequence will be caught in an infinite loop of 4-2-1.

Though there are no counter-exmaples thus far, no proof to this conjecture exists yet.
Also, no closed form solution to determine how many terms it will take until converging to 1.

This project aims to explore this famous conjecture and find a way to reduce the search space of potential counter examples.
e.g. 

## Ideas/Approaches ##
* investigate the rate of convergence of the sequence
* if N is odd, F(N)=3*N+1. Now if this new value is a power of two, we know the sequence will directly converge to 1 and there is no need to continue.
  * This is useful for large inputs as it eliminates redundant computing.

### If a value appears twice in the sequence, this would show a counter example to the conjecture as it would show a cycle within the sequence that doesn't include 1. ###
### If the sequence increases without bound the conjecture will be false. ###
#### There are no examples of either of these case thus far. ####

The only way to approach a power of 2 is by having an odd number from below and performing 3*n + 1. otherwise the sequence would have performed n/2 on an even number that is greater. Since the number in question is a power of 2, the previous even term would have been, too.

the odd numbers that will collapse immediately take the form:  N = 2m+1    F(N) = 3*N+1 = 2^k   =>    N = (2^k - 1)/3

```
Best Case:
Powers of two will collapse the fastest as the sequence will be strictly decreasing through division of 2 - This would take O(logn) time to converge.

Worst Case:
It is hard to determine the worst case for this convergence of this sequence as it gives rise to very unpredictable behavior.
```
