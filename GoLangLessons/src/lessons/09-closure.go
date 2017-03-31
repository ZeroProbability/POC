package main

import "fmt"

// optionally add a custom type
type printer func(string) ()


func createprintfunc(prefix, suffix string) printer {
    return func(s string) {
        fmt.Println(prefix + s + suffix)
    }
}

func somefunc(printfunc printer) {
    printfunc("blah")
}

func main() {
    somefunc(createprintfunc("hello ", "!!"))
}
