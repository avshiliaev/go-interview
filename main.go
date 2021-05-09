package main

import (
	"fmt"
	"github.com/avshiliaev/interview/bitwise"
	"runtime"
)

func main() {
	fmt.Println(runtime.GOOS)
	fmt.Println(runtime.GOARCH)
	fmt.Println(runtime.NumCPU())
	fmt.Println(runtime.NumGoroutine())

	fmt.Println("-----------------")

	bitwise.BitVectorMask()
}
