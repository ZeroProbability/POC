package main

import "fmt"

type Student struct {
    isMale bool
    Name string
}

func (s Student) Greeting() string {
    var greet string
    greet = "Miss"
    if s.isMale {
        greet = "Mr"
    }
    return "Hello "+ greet + " "+ s.Name
}

func main() {
    s1 := Student { true, "Anbu" }
    fmt.Println(s1.Greeting())
    s2 := Student { false, "Mary" }
    fmt.Println(s2.Greeting())
}
