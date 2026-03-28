"""
Caching is a technique that stores results of operations so you dont need to recalculate every time you need the same result

Recursion is a technique where a function calls itself in order to solve a problem
Recursion breaks down complex problems into smaller, subproblems
Every recursion has a base case (stops the recursion) and a recursive case (function calls itself)

Memoisation is both caching and recursion combined
Memoisation is the process of storing results of function calls and returning the cached result
This technique eliminates redundant calculations which reduces time complexity significantly

"""

class Solution:
    def factorial(self, n):
        if n == 0 or n == 1: #Base case
            return 1
        
        return n * self.factorial(n-1) #Recursive case

    #Factorial function showing recursion
    
    def fibonacci(self, n):
        fib_cache = {} #Memoisation using a dictionary

        if n in fib_cache:
            return fib_cache[n]
        #Checks if value is already in cache
        
        if n <= 1:
            return n
        #Base case
        
        fib_cache[n] = self.fibonacci(n-1) + self.fibonacci(n-2)
        #Result stored in cache

        return fib_cache[n] #Recursive case with caching
    
    #Fibonacci function showing memoisation

sol1 = Solution()

print(sol1.factorial(5)) #Calls factorial(4) and so on in steps of -1

print(sol1.fibonacci(7)) #Calculates 7th fibonacci number