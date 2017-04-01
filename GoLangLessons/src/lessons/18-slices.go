package main

import "fmt"

func main() {
    // Create a slice with total capacity 3
    var s []int = make([]int, 3, 5)

    fmt.Println(s)
    fmt.Println(s.(type))
}
