'''
When a function calls itself, it is called recursion. 
Recursion is a programming technique that allows a function to solve a 
problem by breaking it down into smaller subproblems of the same type. 
Each recursive call should bring the function closer to a base case, 
which is a condition that stops the recursion.
'''
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n - 1) # recursive call

x=factorial(5) # Output: 120  
print(x)
