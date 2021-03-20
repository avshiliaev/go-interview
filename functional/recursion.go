package functional

import (
	"fmt"
)

func factorial() {
	fmt.Println(4 * 3 * 2 * 1)

	r := recursive(4)
	fmt.Println(r)

	i := iterative(4)
	fmt.Println(i)
}

func recursive(n int) int {
	if n == 0 {
		return 1
	}
	return n * recursive(n-1)
}

func iterative(n int) int {
	total := 1
	for ; n > 0; n-- {
		total *= n
	}
	return total
}
