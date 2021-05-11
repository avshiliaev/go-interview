package functional

import "fmt"

func closure() {
	a := generator()
	fmt.Println(a())
	fmt.Println(a())
	fmt.Println(a())

	/*
		Output:
		1
		2
		3
	*/
}

func generator() func() int {
	var x int
	return func() int {
		x++
		return x
	}
}
