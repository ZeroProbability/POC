package main

import (
    "fmt"
    "time"
)

func main() {
    done := make(chan bool)
    go func() {
        fmt.Println("Line 1")
        time.Sleep(3 * time.Second)
        fmt.Println("Line 2")
        done <- true
    }()
    fmt.Println("Begin ==---------------- ")
    <-done
    fmt.Println("end   ==---------------- ")
}
