package bitwise

import (
	"fmt"
	"math/rand"
)

/*
	Built-in operators
	0011 & 0101   =	0001		Bitwise AND
	0011 | 0101   =	0111		Bitwise OR
	0011 ^ 0101   =	0110		Bitwise XOR
	^0101	      = 1010		Bitwise NOT (same as 1111 ^ 0101)
	0011 &^ 0101  =	0010		Bitclear (AND NOT)
	00110101<<2	  =	11010100	Left shift
	00110101<<100 =	00000000	No upper limit on shift count
	00110101>>2	  =	00001101	Right shift

	1. The binary numbers in the examples are for explanation only. Integer literals in Go must be specified in octal,
		decimal or hexadecimal.
	2. The bitwise operators take both signed and unsigned integers as input. The right-hand side of a shift operator,
		however, must be an unsigned integer.
	3. Shift operators implement arithmetic shifts if the left operand is a signed integer and logical shifts if it is
		an unsigned integer.
*/

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

func CheckParity() {
	for x := 0; x < 100; x++ {
		num := rand.Int()
		if num&1 == 1 {
			fmt.Printf("%d is odd\n", num)
		} else {
			fmt.Printf("%d is even\n", num)
		}
	}
}

func ToggleSwitchNTimes() {
	x := 0
	cycles := 10

	for i := 0; i <= cycles; i++ {
		x ^= 1
		fmt.Println(x)
	}

	fmt.Println("Switch is: ", x&1 == 1)
}

func BitVectorMask() {

	x := 1
	cycles := 10
	for i := 0; i <= cycles; i++ {
		j := rand.Intn(10)
		if j < 5 {
			fmt.Println("shift x by 1")
			x <<= 1
		}
	}

	mask := 1
	for i := 0; i <= 1; i++ {
		fmt.Println("shift mask by 1")
		mask <<= 1
	}

	fmt.Printf("%d == %08b\n", x, x)
	fmt.Printf("%d == %08b\n", mask, mask)

	if x&mask == 0 {
		fmt.Println("Switch is OFF")
	} else {
		fmt.Println("Switch is ON")
	}

}
