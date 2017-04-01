package main

import (
    "fmt"
    "time"
)

func main() {
    done := make(chan bool, 2)
    go func() {
        fmt.Println("Line 1")
        done <- true; time.Sleep(100 * time.Millisecond)
        fmt.Println("Line 2")
        done <- true; time.Sleep(100 * time.Millisecond)
        fmt.Println("Line 3")
        done <- true; time.Sleep(100 * time.Millisecond)
        fmt.Println("Line 4")
        close(done)
        time.Sleep(3 * time.Second)
    }()
    fmt.Println("Begin ==---------------- ")
    var counter int = 1
    for _ = range done {
        fmt.Println("Done", counter, "times")
        counter++
    }
    fmt.Println("end ==---------------- ")
}
