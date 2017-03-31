package main

import "fmt"

func somefunc(otherfunc func(string)) {
    otherfunc("blah")
}

func main() {
    func test(s string) {
        fmt.Println("value = ", s)
    }
    somefunc(test)
}
