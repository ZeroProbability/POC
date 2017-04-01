package main

import "fmt"

func main() {
    sum := 0
    i := 1
    for i < 21 {
        sum += i
        i += 1
    }
    fmt.Println("Sum was => ", sum)
}
