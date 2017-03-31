package main

import "fmt"

func variadic(n... int) {
    fmt.Println(n)
    fmt.Println("length of arguments =", len(n))
}

func main() {
    variadic(1)
    variadic(1, 2, 3, 4)
}
