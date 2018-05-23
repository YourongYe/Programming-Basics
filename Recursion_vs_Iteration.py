import time

def fib(n):
    if n <= 1:
	    return 0
    if n == 2:
	    return 1
    return fib(n-1)+fib(n-2)

def fib2(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1

    pre = 0
    current = 1
    
    while n >= 3:
        next = pre+current
        pre = current
        current = next
        n -= 1

    return next
   
time_start=time.time()
print(fib(40))
time_end=time.time()
print(time_end-time_start)

time_start=time.time()
print(fib2(40))
time_end=time.time()
print(time_end-time_start)
