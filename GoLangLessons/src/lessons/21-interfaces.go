package main

import "fmt"

type animal struct {
    name string
}

type bird struct {
    name string
}

type movable interface {
    move()
}

func (n animal) move() {
    fmt.Println(n.name, "is running")
}

func (n bird) move() {
    fmt.Println(n.name, "is flying")
}

func main() {
    var t movable
    t = animal { "Dog" }
    t.move()
    t = bird { "Dove" }
    t.move()
}
