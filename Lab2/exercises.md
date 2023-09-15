# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.


    I think `pop()` and `popitem()` in dict docs are not that precisly because they are also return the value of the popped items. And I also think `reserved(d)` should clarify that it returns an iterator.

    As for list, `pop()` also returns the valuse of the popped item. 


2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

    Dict is a mapping objects that maps hashable values to arbitrary objects.
    
    List is sequence type and is more like array in other languages.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

    Yes, a list allows for random access.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

    Pro: It is very flexible to store any data type in one container so that it can improve the efficiency of developers.
    
    Con: Working with any data type can potentially lead to some type-related errors that cannot be found till runtime, which makes debug harder.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

    I think most of functions are well named.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

    I think there is no functions that have more than 3 arguments.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

    `**kwargs` means that the function can accept a variable number of keyword.
    `**` indicates that it should be treated as a dictionary. `kwargs` stands for `keyword arguments`.

    Pros: 

        1. It is very flexible for a function because it allows us to pass any number of keyword arguments to the function
        2. It can make functions much more expansible.

    Cons:

        1. It makes debug much harder.
        2. We need to put extra effort to check the validation of the arguments

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

    1. Setting the arguments to `None` allows users to ommit those arguments when they are calling these methods if they don't have specific values to set. It makes functions more flexible.
    2. Arguments can be set to anything besides `None`.
    3. default values can represent commonly used settings or parameters for functions, they can make functions much more readable and usable.

