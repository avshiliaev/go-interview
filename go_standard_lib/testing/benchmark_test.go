package testing

import "testing"

var number = 8

func BenchmarkRecursive(b *testing.B) {
	for i:=0; i < b.N; i++ {
		recursive(number)
	}
}

func BenchmarkIterative(b *testing.B) {
	for i:=0; i < b.N; i++ {
		iterative(number)
	}
}
