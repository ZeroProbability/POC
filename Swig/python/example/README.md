# Steps

## Building a Python module on Unix:

    swig -python example.i
    gcc -fPIC -c example.c example_wrap.c -I/usr/include/python2.7
    gcc -shared example.o example_wrap.o -o _example.so

## Usage:

    >>> import example
    >>> example.fact(5)
    120
