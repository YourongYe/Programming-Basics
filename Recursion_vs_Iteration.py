
import time

def fib_recursive(n):
    print(n,end=' ')
    if n <= 1:
	    return 0
    if n == 2:
	    return 1
    return fib_recursive(n-1)+fib_recursive(n-2)

def fib_recursive_memo(n,dic):
    print(n,end=' ')
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
print("fib_recursive result:",fib_recursive(10))
time_end=time.time()
print("fib_recursive time:",time_end-time_start)

time_start=time.time()
dic = {}
print("fib_recursive_memo result:",fib_recursive_memo(10,dic))
time_end=time.time()
print("fib_recursive_memo time:",time_end-time_start)

time_start=time.time()
print("fib_iteration result:",fib_iteration(10))
time_end=time.time()
print("fib_iteration time:",time_end-time_start)


###############################################
# Simple recursive vs iteration
###############################################
def loop_recur(n):
  if n == 0:
    return

  loop_recur(n-1)
  print(n)

def loop_iter(n):
  for i in range(1,n+1):
    print(i)

loop_recur(10)
loop_iter(10)



