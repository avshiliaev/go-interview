package concurrency

import (
	"fmt"
	"time"
)

// Channels block!
func ChannelsExample() {
	c := make(chan string)
	go countWithChannel("sheep", c)

	//
	/*
		for {
			msg, open := <-c
			if !open {
				break
			}
			fmt.Println(msg)
		}
	*/
	for msg := range c {
		fmt.Println(msg)
	}

}

func countWithChannel(thing string, c chan string) {
	for i := 1; i <= 10; i++ {
		c <- thing
		time.Sleep(time.Millisecond * 500)
	}

	// If not closed, causes deadlock!
	close(c)
}
