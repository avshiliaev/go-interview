package bitwise

import "fmt"

// Examples https://yourbasic.org/golang/bitwise-operator-cheat-sheet/
func Examples() {
	var a uint = 60 /* 60 = 0011 1100 */
	var b uint = 13 /* 13 = 0000 1101 */
	var c uint = 0

	// Binary AND Operator copies a bit to the result if it exists in both operands.
	/*
			0011 1100 (60)
		  & 0000 1101 (13)
		  =	0000 1100 (12)
	*/
	c = a & b
	fmt.Printf("Line 1 - Value of c is %d\n", c)

	// Binary OR Operator copies a bit if it exists in either operand.
	/*
			0011 1100 (60)
		  | 0000 1101 (13)
		  =	0011 1101 (61)
	*/
	c = a | b
	fmt.Printf("Line 2 - Value of c is %d\n", c)

	// Binary XOR Operator copies the bit if it is set in one operand but not both.
	/*
			0011 1100 (60)
		  ^ 0000 1101 (13)
		  =	0011 0001 (49)
	*/
	c = a ^ b
	fmt.Printf("Line 3 - Value of c is %d\n", c)

	// Binary Left Shift Operator. The left operands value is moved left by the number of bits specified by the right
	// operand.
	/*
			0011 1100 << 2 (60)
		  =	1111 0000 (240)
	*/
	c = a << 2
	fmt.Printf("Line 4 - Value of c is %d\n", c)

	// Binary Right Shift Operator. The left operands value is moved right by the number of bits specified by the right
	// operand.
	/*
			0011 1100 >> 2 (60)
		  =	0000 1111 (15)
	*/
	c = a >> 2
	fmt.Printf("Line 5 - Value of c is %d\n", c)
}

func ToggleSwitchNTimes() {
	x := 0
	cycles := 10

	for i:=0; i<=cycles; i++ {
		x ^= 1
		fmt.Println(x)
	}

	fmt.Println("Switch is: ", x&1==1)
}
