import time

def fib_recursive(n):
    if n <= 1:
	    return 0
    if n == 2:
	    return 1
    return fib_recursive(n-1)+fib_recursive(n-2)

def fib_recursive_memo(n,dic):
    if n <= 1:
	    return 0
    if n == 2:
	    return 1

    if n not in dic:
      dic[n] = fib_recursive_memo(n-1,dic)+fib_recursive_memo(n-2,dic)
    return dic[n]

def fib_iteration(n):
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
print(fib_recursive(30))
time_end=time.time()
print("fib_recursive time:",time_end-time_start)

time_start=time.time()
dic = {}
print(fib_recursive_memo(30,dic))
time_end=time.time()
print("fib_recursive_memo time:",time_end-time_start)

time_start=time.time()
print(fib_iteration(30))
time_end=time.time()
print("fib_iteration time:",time_end-time_start)
