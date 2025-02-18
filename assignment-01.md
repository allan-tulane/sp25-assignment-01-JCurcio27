

# CMPS 2200 Assignment 1

**Name:** Jaedan Curcio


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  
.  
.  $2^{n+1} \in O(2^n)$ is true, as the inequality $2^{n+1}$ is less than or equal to c * $2^n$ (n > n0) holds true for all values
.  where c is greater than or equal to 2, and n0 is greater than or equal to 1, meaning $2^n$ asymptotically dominates $2^{n+1}$.
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  
.  
.  No, as there are no values of c or n0 which make the inequality $2^{2^n}$ is less than or equal to c * $2^n$ (n > n0) hold true,
.  meaning that 2^(2^n) grows too fast, and 2^n cannot asymptotically dominate it.
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  
.  $n^{1.01} \in O(\mathrm{log}^2 n)$ is false, as $n^{1.01}$ grows polynomially, which is faster than $\mathrm{log}^2 n)$,
.  which is polylogarithmic growth. Since $n^{1.01}$ grows faster than $\mathrm{log}^2 n)$, $\mathrm{log}^2 n)$ cannot 
.  be asymptotically dominant, and thus the original question is false.

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
.  As previously discussed, $n^{1.01}$ grows much faster than $\mathrm{log}^2 n)$. This means that no matter how big the value of c is,
.  $n^{1.01}$ will always eventually outweigh $\mathrm{log}^2 n)$, so thus $n^{1.01} \in \Omega(\mathrm{log}^2 n)$ is true.
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  
.  No, $\sqrt{n}$ is not $\in O((\mathrm{log} n)^3)$, as $\sqrt{n}$ grows faster than $(\mathrm{log} n)^3)$, so 
.  O((\mathrm{log} n)^3)$ cannot asymptotically dominate $\sqrt{n}$ (limit n -> infinity of f(n)/g(n) is infinity)
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  Yes, $\sqrt{n}$ is $\in O((\mathrm{log} n)^3)$. As previously states, the limit as n approaches infinity of $\sqrt{n}$ over
.  $(\mathrm{log} n)^3)$ is infinity, ans thus $\sqrt{n}$ is $\in O((\mathrm{log} n)^3)$.


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  
.  This function takes in a value x, and then if x is greater than one, returns the value of the xth number in the fibonacci sequence
.  by recursively calling itself on x-1 and x-2, eventually returning f(x) since f(x) = f(x-1) + f(x-2).
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  
.  
.  The work and span of this implementation are both O(n), as we have to iterate through the entire list in order to produce an answer.
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  The work of this sequential algorithm is O(n), as the algorithm continously creates smaller lists starting at size n, and dividing
.  in half every time. This is theoretically an infinite series which converges to n, meaning the work is O(n). The span is O(log n)
.  as each subproblem can be done independently, so the span becomes the depth of the recursion, which os O(log n).
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  If we parallelize like with sum_list_recursive, the work is W(n) =  2W(n/2) + W(1), as the list is divided by two repeatedly
.  (starting with one list) until a base case is reached, and then the lists are put back together, which takes W(1) time. The span is
.  log2n, because that is the number of recursive calls needed to reach the base case.
.  
.  
.  
.  
.  

