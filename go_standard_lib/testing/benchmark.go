package testing

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
