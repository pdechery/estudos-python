# Python Helper 

## Inspecting objects

**vars()**

Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute

Sobre o __dict__:

	(Não confundir com a função built-in dict(), que serve para criar dicionaŕios)

	A dictionary or other mapping object used to store an object’s (writable) attributes.

**help()**

Invoke the built-in help system. (This function is intended for interactive use.) If no argument is given, the interactive help system starts on the interpreter console. If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed on the console. If the argument is any other kind of object, a help page on the object is generated.

**dir()**

Without arguments, return the list of names in the current local scope. 
With an argument, attempt to return a list of valid attributes for that object.

**type()**

Retorna tipo do objeto

**repr()**

Return a string containing a printable representation of an object. 

## Definitions

**module**

An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing.

**namespace**

The place where a variable is stored. Namespaces are implemented as dictionaries. There are the local, global and built-in namespaces as well as nested namespaces in objects (in methods).

## __main__

`__main__` is the name of the environment where top-level code is run.

“Top-level code” is the first user-specified Python module that starts running. It’s “top-level” because it imports all other modules that the program needs. Sometimes “top-level code” is called an entry point to the application.


