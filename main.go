package main

import (
	"fmt"
	bitwise2 "github.com/avshiliaev/interview/golang_built_in/bitwise"
	"runtime"
)

func main() {
	fmt.Println(runtime.GOOS)
	fmt.Println(runtime.GOARCH)
	fmt.Println(runtime.NumCPU())
	fmt.Println(runtime.NumGoroutine())

	fmt.Println("-----------------")

	bitwise2.BitVectorMask()
}
