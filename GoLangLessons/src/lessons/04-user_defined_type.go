package main

import "fmt"

// Defining a new user defined type
// Go doesn't have classes, 'struct' is used in its place
// Anything that's capitalized is visible outside the current source
type Salutation struct {
    name string
    greeting string
}

func main() {
    // initalize the values in the user defined type
    var v = Salutation{"Anbu", "Hello"}

    fmt.Println("User defined type's value => ", v)
    fmt.Println("Printing individual values => ", v.greeting, v.name)

    // while initalizing variable names could also be used for defining the user defined data type
    v = Salutation{greeting: "Hello", name: "Arun"}
    fmt.Println("Printing individual values => ", v.greeting, v.name)

    // initalize the values later
    var n = Salutation{}
    fmt.Println("Initalizing later => " , n)
    n.name = "Bob"
    fmt.Println("Initalizing later => " , n)
    n.greeting = "Hello"
    fmt.Println("Initalizing later => " , n)

}
