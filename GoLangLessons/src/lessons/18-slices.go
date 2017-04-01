package main

import "fmt"

func main() {
    var squares []int = make([]int, 10)
    var cubes []int = make([]int, 10)

    fmt.Println(squares)
    fmt.Println(len(squares))
    for i:= 0; i< len(squares); i++ {
        squares[i] = (i+1) * (i+1)
        cubes[i] = (i+1) * (i+1) * (i+1)
    }
    fmt.Println(squares)

    appended:= append(squares, cubes...)

    fmt.Println(appended)

    deleted:= append(appended[:10], appended[11:]...)

    fmt.Println(deleted)
}
