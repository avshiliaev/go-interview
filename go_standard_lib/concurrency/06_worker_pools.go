package concurrency

import "fmt"

func WorkerPoolsExample() {
	bufferSize := 100
	jobs := make(chan int, bufferSize)
	results := make(chan int, bufferSize)

	// Multiple concurrent workers. No order guarantee.
	go worker(jobs, results)
	go worker(jobs, results)
	go worker(jobs, results)
	go worker(jobs, results)

	for i := 0; i < bufferSize; i++ {
		jobs <- i
	}
	close(jobs)

	for j := 0; j < bufferSize; j++ {
		fmt.Println(<-results)
	}
}

func worker(jobs <-chan int, results chan<- int) {
	for n := range jobs {
		results <- fib(n)
	}
}

func fib(n int) int {
	if n <= 1 {
		return n
	}
	return fib(n-1) + fib(n-2)
}
