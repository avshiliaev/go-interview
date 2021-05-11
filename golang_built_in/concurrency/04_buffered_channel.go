package concurrency

import "fmt"

func BufferedChannelExample() {

	// If the channel is not buffered, we cannot send and receive in the sage go routine.
	c := make(chan string, 2)
	c <- "hello"
	c <- "world"

	msg := <-c
	fmt.Println(msg)

}
