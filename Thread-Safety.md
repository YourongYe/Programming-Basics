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
