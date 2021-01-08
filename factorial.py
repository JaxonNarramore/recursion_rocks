# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))
# => 120
