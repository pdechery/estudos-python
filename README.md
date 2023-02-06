# Python Helper

## Parallelism and Concurrency

Python can have multiple threads but only one will be executed each time. 

That happens because of the Global Lock Interpreter, created to prevent data issues between threads (Race Condition)

When doing I/O-intensive work, using threads can make the script run faster because the GIL will be released for this type of work (not to others)

Using threads doesn't mean using multiple processors (parallelism). To do that, multiprocessing package can be used.

The asyncio package allows concurrency in a single-thread, using coroutines.

## Generator functions

Generator functions are a special kind of function that returns an iterator.

They use "yeld" instead of "return" and it's possible to use them in a for loop, for example.

Since they don't load everything into memory at once, but instead only when iterated over, they can be named "lazy iterators".

Generators are useful when dealing with large datasets, that will be return on demand (each item a time).

## Wheels and Package distribution

Wheels are the Python standard for distributing packages. 

Wheels allow faster installation, because they avoid the "building stage" phase while downloading packages.

They are a special files (.whl), compressed (zip) and with names that provides information about installation.

The opposite of a Wheel is the source distribution, or sdist. Those are built on the user machine.

setup.py script can be used to create Wheels or Source Distributions.

## Context Managers

Context Managers are objects that implement `__enter__` and `__exit__` special methods.

They're used in situations where you need a "setup" and "teardown" events while acting on some resource.

They're used mostly in situations where you need to release memory after some processing. Ex. Working with files.

You must use the `with` statement to work with Context Managers.

## Iterators

- Iterators are objects that can be iterated over.

- Python obtains iterators from iterables. (see `iter()` built-in function)

- "Iterable" is any object which returns an Iterator.

Iterators interface consists of two methods: `__next__` and `__iter__`.

Python can iterate over any sequence that implements the `__iter__` special method. (or `__getitem__`)

Iterators can be created by using `iter()` built-in function.

## Variable Scope

Python has Local and Global scope, among others (see below)

Local refers to the code block (ex: function) where the variable was declared

Global refers to the whole module (top-level scope). Can be looked using `dir()`

"LEGB" is the rule by which Python resolves names.

- Local = code block scope
- Enclosing = nested functions (Python can have functions inside other functions)
- Global = module scope
- Built-in = automatically loaded by Python once script is runned. Contains all built-in names.

"global" statament can be used to change global names inside local scope

## Dunder methods

Special methods that user double underscores around their names (that's where "dunder" name comes from, Double UNDERscore) and interact with the Python interpreter, defining built-in functions and operators behaviour.

Example:

`__len__` method in a class defines behaviour of `len()` built-in function in an instance from that class.

`__add__` method in a class defines behaviour of the + operator in an instance from that class.

To know available dunder methods on a specific object one can do:

```
>>> x = 2
>>> help(x)

>>> z = {'nome':'Pierre','sobrenome':'Dechery'}
>>> help(z)
```

Those methods are not supposed to be called directly. One should use the high-level built-in functions or operators instead.

When one uses a Dunder method to leverage some operator in Python that's called Operator Overloading.

## Unpacking with asterisk

* and ** can be used on a function signature to enable that function to receive arguments that aren't part of its original signature.

* is for position arguments, who'll be made available as a tuple, and ** is for keyword arguments, who will be made availabe as dict inside the function.

Example:

```
# function signature
def multiple_arguments(a, *mul, **any):
	pass


# function call
multiple_arguments(12, 'hello', 'world', 14, test='ok')
```
## Dictionaries

Dictionaries (dict) are derived from Mapping superclass.

dict keys must be hashable (they can be anything that's hashable)

An object is hashable when it has a "hash" value that does not change during its lifetime.

To obtain a hash, the `__hash__` is used.

Hashes must be comparable to any other objects throught the "==" operator.

Not all objects are hashable. Only those who are immutable (ex. str, bytes, int).

Lists aren't immutable, so they aren't hashable.

## Equality vs identity

To compare raw values the "==" operator must be used, while to compare identity the "is" keyword should be used.

"is" compares identities, and each object has a unique identity unless it is a reference (or alias) to another one.

Example:

a = 2
b = a ("b" is now reference to "a", that means they are the same object)
c = 2 ("c" have the same value as "a" but it's not a reference to it)

## Function parameters by reference or value

Function parameters are aliases of their arguments. That means they reference the same object.

When it comes to change those arguments inside a function, results may differ depending whether the parameter is mutable or not.

Lists, for example will reflect changes outside the function, but not integers.

https://realpython.com/python-pass-by-reference/#replicating-pass-by-reference-with-python

## Functions as first-class citizens

Languages who have functions are "first-class" citizens are those where functions can be:

- Created at runtime
- Passed as an argument to other functions
- Returned as the result of a function
- Used as values for variables or dict keys
- Nested inside other functions

## Private methods

"private" attribute is one that shouldn't be shared with any class instance.

Python doesn't offer a mechanism to create private methods, but offers the "name mangling" mechanism.

If you name your attrite with two leading underscores it will have it's name transformed, so it won't be possible for a subclass to use it.

To create a private method on Python there's also a convention to use a single underscore before it's name.

The interpreter doesn't do nothing when this happens but the convention will help developers to be aware that that method shouldn't be called on a class instance.

## Duck Typing

"If it behaves like a Duck so it is a Duck"

In Python any object can act like any other from any Type if it has the needed methods.

Python doesn't look for Types when inspecting an object. It looks for methods.

The FrenchDeck class can act like an iterable and a dict, because it implements the needed methods.

It doesn't need to inherit from any dict or iterable interface to be recognized and work as a dict or iterable.






	



