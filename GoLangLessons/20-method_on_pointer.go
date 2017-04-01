package main

import "fmt"

type Numbers struct {
    n1 int
    n2 int
}

func (n *Numbers) swap() {
    tmp := n.n1
    n.n1 = n.n2
    n.n2 = tmp
}

func main() {
    var n Numbers
    n = Numbers { 1, 2 }
    fmt.Println("Before swap...", n)
    n.swap()
    fmt.Println("After swap...", n)
}
