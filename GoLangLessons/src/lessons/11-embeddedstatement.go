package main

import "fmt"

func greet(formal bool, name string) {
    if f := "hello Mr "; formal {
        fmt.Println(f + name)
    } else {
        fmt.Println("hey " + name)
    }
}

func main() {
    greet(true, "Anbu")
    greet(false, "Anbu")
}
