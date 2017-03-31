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

func main() {
    greet("Bob")
    greet("Joe")
    greet("Mary")
    greet("Anbu")
}
