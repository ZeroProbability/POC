package main

import "fmt"

func main() {
    /* python to generate numbers -- 
        print ', '.join([str(i) for i in range(21)])
    */
    i := []int { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20 }
    sum := 0
    for _, v := range i {
        sum += v
    }
    fmt.Println("Sum was => ", sum)
}
