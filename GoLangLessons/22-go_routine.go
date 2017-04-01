package main

import (
    "fmt"
    "time"
)

func main() {
    go func() {
        fmt.Println("Line 1")
        time.Sleep(3 * time.Second)
        fmt.Println("Line 2")
    }()
    fmt.Println("Begin ==---------------- ")
    time.Sleep(6 * time.Second)
    fmt.Println("end   ==---------------- ")
}
