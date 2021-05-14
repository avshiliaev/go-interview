package concurrency

import (
	"fmt"
	"time"
)

func ScanLineExample() {
	go count("sheep")
	go count("fish")

	fmt.Scanln()
}

func count(thing string) {
	for i := 1; i <= 30; i++ {
		fmt.Println(i, thing)
		time.Sleep(time.Millisecond * 500)
	}
}
