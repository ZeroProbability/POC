package main

import "fmt"

func main() {
    var prefixMap map[string]string
    prefixMap = make(map[string]string)

    prefixMap["Bob"] = "Mr"
    prefixMap["Joe"] = "Dr"
    prefixMap["Mary"] = "Mrs"

    fmt.Println("Before update.... ")
    for k, v := range prefixMap {
        fmt.Println(v, k)
    }

    prefixMap["Mary"] = "Dr"
    fmt.Println("After update...")
    for k, v := range prefixMap {
        fmt.Println(v, k)
    }

    fmt.Println("After delete...")
    delete(prefixMap, "Joe")
    for k, v := range prefixMap {
        fmt.Println(v, k)
    }

    if _, exists := prefixMap["Bob"]; exists {
        fmt.Println("There is a Bob")
    } else {
        fmt.Println("There is a no Bob")
    }
}
