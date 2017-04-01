package main

import "fmt"

// go functions can have multiple return values
func func1(v int) (string, int) {
    fmt.Println("v => ", v)
    return "string value", 3
}

// variable names can also be used for return types
func greet(name, greet string) (greeting, alternate string) {
    greeting = greet + " " + name
    alternate = "Hey " + name
    return
}


func main() {
    var x, y = func1(100)
    fmt.Println("returned values => ", x, "&", y)

    var g1, g2 = greet("Anbu", "Hello")
    fmt.Println(g1)
    fmt.Println(g2)
}
