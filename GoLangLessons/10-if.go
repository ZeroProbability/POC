package main

import "fmt"

func greet(formal bool, name string) {
    if formal {
        fmt.Println("hello Mr " + name)
    } else {
        fmt.Println("Hey " + name)
    }
}

func main() {
    greet(true, "Anbu")
    greet(false, "Anbu")
}
