package main

import "fmt"

func main() {
    message := "hello world"
    var greeting *string = &message

    fmt.Println(message, *greeting)
}
