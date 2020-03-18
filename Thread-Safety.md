# Define
An object is thread-safe for reading from multiple threads. For example, given an object A, it is safe to read A from thread 1 and from thread 2 simultaneously.

For example, given an object A, if thread 1 is writing to A, then thread 2 must be prevented from reading from or writing to A.

# Example
- Calling foo(x) on one thread and foo(y) on a second thread concurrently is OK.  
- Calling foo(x_i) on any number of threads concurrently is OK, provided each x_i is different.  
- Calling foo(x) on a specific number of threads concurrently is OK.   
- Calling foo(x) on any number of threads concurrently is OK.   
- Calling foo(x) on one thread and bar(x) on another thread concurrently is OK.   
- Calling foo(x) on one thread and bar(x) on any number of threads concurrently is OK.    

# Thread synchronization 
It is defined as a mechanism which ensures that two or more concurrent processes or threads do not simultaneously execute some particular program segment known as a critical section.   
When one thread starts executing the critical section (a serialized segment of the program) the other thread should wait until   the first thread finishes. If proper synchronization techniques are not applied, it may cause a race condition where the    values of variables may be unpredictable and vary depending on the timings of context switches of the processes or threads.

# Mutex
https://www.geeksforgeeks.org/mutex-lock-for-linux-thread-synchronization/
The most popular way of achieving thread synchronization.  

A Mutex is a lock that we set before using a shared resource and release after using it.  
When the lock is set, no other thread can access the locked region of code.  
So we see that even if thread 2 is scheduled while thread 1 was not done accessing the shared resource and the code is locked by thread 1 using mutexes then thread 2 cannot even access that region of code.  
So this ensures synchronized access of shared resources in the code.  
