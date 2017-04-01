package main

import (
    "fmt"
    "time"
)

func main() {
    chan1 := make(chan int, 3)
    chan2 := make(chan int, 3)
    go func() {
        time.Sleep(100 * time.Millisecond)
        chan1 <- 44
    }()
    go func() {
        time.Sleep(100 * time.Millisecond)
        chan2 <- 88
    }()
    fmt.Println("Begin ==---------------- ")
    var readFromOne = false
    var readFromTwo = false
    outer: for {
        select {
        case i, ok := <-chan1:
            if ok {
                fmt.Println(i, "from chan1")
                readFromOne = true
            } else {
                fmt.Println("Error reading from one")
            }
        case i, ok := <-chan2:
            if ok {
                fmt.Println(i, "from chan2")
                readFromTwo = true
            } else {
                fmt.Println("Error reading from one")
            }
        default:
            if readFromOne && readFromTwo {
                break outer
            }
            fmt.Println("Nothing to read")
            time.Sleep(10 * time.Millisecond)
        }
    }
    fmt.Println("end ==---------------- ")
}
