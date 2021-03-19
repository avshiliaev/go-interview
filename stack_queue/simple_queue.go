package stack_queue

// CircularQueue
type Queue struct {
	queue []int
}

// Constructor initialize your data structure here. Set the size of the queue to be k.
func QueueConstructor() Queue {
	return Queue{
		queue: make([]int, 0),
	}
}

// EnQueue insert an element into the circular queue. Return true if the operation is successful.
func (m *Queue) EnQueue(value int) bool {
	m.queue = append(m.queue, value)
	return true
}

// DeQueue delete an element from the circular queue. Return true if the operation is successful.
func (m *Queue) DeQueue() bool {
	if len(m.queue) == 0 {
		return false
	}

	m.queue = m.queue[1:]
	return true
}

// Front get the front item from the queue.
func (m *Queue) Front() int {
	if len(m.queue) == 0 {
		return -1
	}

	return m.queue[0]
}

// Rear get the last item from the queue. */
func (m *Queue) Rear() int {
	if len(m.queue) == 0 {
		return -1
	}
	return m.queue[len(m.queue)-1]
}

// IsEmpty checks whether the circular queue is empty or not. */
func (m *Queue) IsEmpty() bool {
	return len(m.queue) == 0
}
