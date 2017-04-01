package main

import "fmt"

// You can declare constants like this
const (
    PI = 3.14
    LANG = "GO"
)

// integer constants with incrementing values can be delcared like this
const (
    A = iota
    B = iota
    C = iota
)

// if we do not define the value, the previous value is copied 
const (
    D = iota
    E
    F
)

func main() {
    fmt.Println(PI)
    fmt.Println(LANG)

    fmt.Println(A, B, C)
    fmt.Println(D, E, F)
}
