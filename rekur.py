n = int(input())
"""
def fib(n):
    if n in (1,2):
        return 1
    return fib(n - 1) + fib(n - 2)
print(fib(n))
"""
    #1 1 2 3 5 8 13 21 34
"""
def fact(n):
    if n == 1 or n == 0:
        return 1
    return fact(n - 1) * n
        
print(fact(n))
"""

"""
def sum(n):
    if n == 1:
        return 1
    return sum(n - 1) + n
print(sum(n))
"""


'''
def koroche(n):
    if n == 0:
        return True
    if n < 0:
        return False
    return koroche (n - 3) or koroche (n - 5)
print(koroche(n))
'''