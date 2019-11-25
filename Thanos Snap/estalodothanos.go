package main

import (
    "fmt"
    "math/rand"
    "time"
)

func main() {
    
    rand.Seed(time.Now().UnixNano())
    var destiny int = rand.Intn(2)

    if destiny == 0 {
        fmt.Println("You were spared by Thanos.")
    } else {
        fmt.Println("You were slain by Thanos, for the good of the Universe.")
    }
}