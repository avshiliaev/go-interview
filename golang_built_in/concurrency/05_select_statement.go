package concurrency

import (
	"fmt"
	"time"
)

func SelectStatementExample() {
	c1 := make(chan string)
	c2 := make(chan string)

	go func() {
		for {
			c1 <- "Every 500ms"
			time.Sleep(time.Millisecond * 500)
		}
	}()

	go func() {
		for {
			c2 <- "Every two seconds"
			time.Sleep(time.Second * 2)
		}
	}()

	for {

		// This way we would be blocked and wait for the slowest routine to post on the channel
		/*
			fmt.Println(<- c1)
			fmt.Println(<- c2)
		*/

		select {
		case msg1 := <-c1:
			fmt.Println(msg1)
		case msg2 := <-c2:
			fmt.Println(msg2)
		}
	}

}
