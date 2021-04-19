package concurrency

import "sync"

func WaitGroupExample() {

	var wg sync.WaitGroup
	wg.Add(1)

	go func() {
		count("sheep")
		wg.Done()
	}()

	wg.Wait()

}
