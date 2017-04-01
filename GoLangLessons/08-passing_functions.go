package main

import "fmt"

// optionally add a custom type
type printer func(string) ()

func somefunc(printfunc printer) {
    printfunc("blah")
}

func printit(s string) {
    fmt.Println("value = ", s)
}

func main() {
    somefunc(printit)
}
