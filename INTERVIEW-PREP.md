# Python Interview Helper

## Parallelism and Concurrency

Python can have multiple threads but only one will be executed each time. 

That happens because of the Global Lock Interpreter, created to prevent data issues between threads (Race Condition)

When doing I/O-intensive work, using threads can make the script run faster because the GIL will be released for this type of work (not to others')

Using threads doesn't mean using multiple processors (parallelism). To do that, multiprocessing package can be used.

The asyncio package allows concurrency in a single-thread (using coroutines).

## Generator functions

Generator functions are a special kind of function that returns an iterator.

They use "yeld" instead of "return" and it's possible to use them in a for loop.

Since they don't load everything into memory at once, but instead only when iterated over, they can be named "lazy iterators".

Generators are useful when dealing with large datasets, that will be return on demand (each item a time).

## Wheels and Package distribution

Wheels avoid "building stage" phase while downloading packages.

They are a special files (.whl), compressed (zip) and with names that provides information about installation.

The opposite of a Wheel is the source distribution, or sdist. Those are build on the user machine.

setup.py script can be used to create Wheels or Source Distributions.

## Context Managers

Context Managers are protocols that implement __enter__ and __exit__ special methods

They're used in situations where you need a Setup and Teardown events while acting on some resource.

They're used mostly in situations where you need to release memory after some processing. Ex. Working with files.

You must use the with statement to work with Context Managers.

## Iterators

Any  object that implements the __next__() special method is an 'iterable'.

That means lists and strings, for example.

An iterator is an object that's used for iterating over another one (that's iterable). 

Iterators can be created by using iter() built-in function.

