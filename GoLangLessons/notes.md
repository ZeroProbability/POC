# Notes

## What is GO?

* Go is a Compiled, Garbage-collected, and Concurrent language
* Garbage-collection is latency free, unlike Java.
* It is a systems level language like C. But it is built to make use of modern architecture, especially multi-core.
* It is statically typed, but retains the ease of use like dynamic language.
* It is type-safe and memory-safe. Memory safefy means you can set a pointer or overflowing beyond allocated memory.
* Semicolons are automatically inserted by the compiler at the end of lines.

## What is not there in GO?
* There is no inheritance (Because composition is better). 
* There are no generics (or templates).
* There are no assertions.
* There is no method overloading (thus making compilation process be simple and fast).

## Packages

* In go 'packages' are used to define namespaces. 
* There are many predefined packages in go. They can be found in golang.org/pkg

## GOPATH
* Like Java's CLASSPATH, go has GOPATH. Go will look for source code inside 'src' subdirectory in each of the paths declared in GOPATH. 

## Basic Types

* bool
* string
* int, int8, int16, int32, int64
* uint, uint8, uint16, uint32, uint64, uintptr
* byte (uint8)
* rune (int32), like a char
* float32, float64
* complex64, complex128

Notes: 
Unlike other languages, Go requires you to cast int8 to int16 when int8 value is assigned to variable of type int16.

## Types

* Array
* Slice - like a list
* Struct - collection of other types (no classes)
* Pointer 
* Function
* Interface - interfaces like Java
* Map
* Channel - for communication

## Maps

* Keys have to have equality operator defined
* Maps are reference types
* They are not thread safe

## Arrays

* Arrays are Fixed size. If you want to expand an array, you have to create a new one and copy the contents.
* Array type is size and underlying type. Array of type integer is different from Array of type String.
* You need not initalize it. Example: Interger arrays will have zero valued values by default.
* Arrays are not reference types (Unlike slices or maps)

## Slices

* Arrays are fixed size, they can not be reallocaed or appened.
* Type of a slice is underlying member type (the length is irrelevant - unlike array)
* 'make' is used to initalize the slice. Un-made slices will be nill.
* The underlying data is actually an array. 
* the 'make' takes the underlying array type, initial capacity and total capacity. Example `make([]int, 3, 5)`
* Sub-slices can be got using python-like notation Example: `ss = s[3:5]`
* It is not possible to delete an element from the middle of a slice. If we need to delete an element, use `append(s1, s2)` to append all elements expect that one. Example: To remove 4th element `append(s[:4], s[5:])

## Methods and Interfaces

* Methods in golang can operate on a type or a pointer.

','.join([str(x) for x in range(20)])
