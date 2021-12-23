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
* if N is odd, F(N)=3*N+1. Now if this new value is a power of two, we know the sequence will directly converge to 1 at the fast rate as 

```
Best Case:
Powers of two will collapse the fastest as the sequence will be strictly decreasing through division of 2 - This would take O(logn) time to converge.
```
