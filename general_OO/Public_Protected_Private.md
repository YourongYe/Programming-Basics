# Public
can be accessed by objects, class method, friend method, and inherited class method (只有public能被实例访问)

# Protected
can be accessed by class method, friend method and inherited class method

# Private
can be accessed by class method, friend method (not commonly used)

# Why we should use Private
private data members are generally considered good because they provide **encapsulation**.

Providing getters and setters for them breaks that encapsulation, but it's still better than public data members because there's only once access point to that data.

You'll notice this during **debugging**. If it's private, you know you can only modify the variable inside the class. **If it's public, you'll have to search the whole code-base for where it might be modified.**

As much as possible, ban getters/setters and make properties private. This follows the principle of **information hiding** - you shouldn't care about what properties a class has. It should be **self-contained**. Of course, in practice this isn't feasible, and if it is, a design that follows this will be more cluttered and harder to maintain than one that doesn't.

**self-contained:** 所有需要完成的动作（eg.修改变量的值）都应该用class里提供的func来完成
