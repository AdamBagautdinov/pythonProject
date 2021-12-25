
#1

def fu(n):
    if n != 0:
        return n *fu(n-1)
    else:
        return 1

def sum(m):
    k = 0
    for i in range(1, m+1):
        k += fu(i-1)**2 / fu(2*i)

#2.
def arifm_(first, second, k):
    d = second - first
    return first + d*(k-1)

#3.
import math as mt
def recursion( x, n, count = 1):
    if count <= n:
        return mt.cos(x + recursion(x,n, count +1))
    else:
        return 0

#4
x = 8**2020 + 4**2017 + 26 - 1

s = ""

while x > 0:
    s += str(x % 2)
    x //= 2

print(s.count("1"))

#5