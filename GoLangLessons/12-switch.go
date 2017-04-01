package main

import "fmt"

func greet(name string) {
    switch name {
    case "Bob":
        fmt.Println("Hello Mr Bob")
    case "Joe":
        fmt.Println("Hey Joe")
    case "Mary":
        fmt.Println("Hello Mrs Mary")
    default:
        fmt.Println("Hey dude")
    }
}

// switch with fallthrough 
func numtype(n int) {
    switch n {
    case 1:
        fmt.Println(n , " is uno ")
        fallthrough
    default:
        fmt.Println(n , " is a natural number")
    }
}

func main() {
    fmt.Println(" =========== ")
    greet("Bob")
    greet("Joe")
    greet("Mary")
    greet("Anbu")

    fmt.Println(" =========== ")
    numtype(1)
    numtype(2)
}
