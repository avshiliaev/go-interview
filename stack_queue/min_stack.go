package stack_queue

type MinStack struct {
	stack []item
}
type item struct {
	min, x int
}

func MinStackConstructor() MinStack {
	return MinStack{}
}

func (ms *MinStack) Push(x int) {
	min := x
	if len(ms.stack) > 0 && ms.GetMin() < x {
		min = ms.GetMin()
	}
	ms.stack = append(ms.stack, item{min: min, x: x})
}

func (ms *MinStack) Pop() {
	ms.stack = ms.stack[:len(ms.stack)-1]
}

func (ms *MinStack) Top() int {
	return ms.stack[len(ms.stack)-1].x
}

func (ms *MinStack) GetMin() int {
	return ms.stack[len(ms.stack)-1].min
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
