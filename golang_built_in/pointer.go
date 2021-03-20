package golang_built_in

import "fmt"

func main() {
	a := 42
	fmt.Println(a) // Value, type int
	fmt.Println(&a) // Address (with ampersand), type *int (Pointer to an int)

	b := &a
	fmt.Println(b) // Address, type *int (Pointer to an int)
	fmt.Println(*b) // Dereference operator, becomes an int

	*b = 43 // Dereference and assign
	fmt.Println(a) // a is not 43

}
