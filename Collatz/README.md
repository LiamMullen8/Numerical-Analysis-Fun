# Collatz Conjecture #

- proposed by Lothar Collatz (1910-1990)
```
Rules: 
if N is odd,  F(N+1) = 3*F(N) + 1
if N is even, F(N+1) = F(N) / 2 
```

By following these two simple rules/arithmetic operations, it is conjectured that every natural number will collapse down to 1.
In other words, you can pick any integer from 1 to infinity and eventually arrive at 1.

Upon reaching 1, the sequence will be caught in an infinite loop of 4-2-1.

There is no closed form solution as to how many terms it will take until reaching 1 and there is no proof to this conjecture.




* Powers of two will collapse the fastest as there are only reductions through division of 2 - This would take O(logn)  time.
