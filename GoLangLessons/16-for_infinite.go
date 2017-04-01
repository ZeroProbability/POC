package main

import "fmt"

func main() {
    sum := 0
    i := 1
    for {
        sum += i
        i += 1
        if i > 20 {
            break
        }
    }
    fmt.Println("Sum was => ", sum)
}
