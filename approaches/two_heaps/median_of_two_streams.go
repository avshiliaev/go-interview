package two_heaps

import "container/heap"

// https://leetcode.com/problems/find-median-from-data-stream/

// MedianFinder to find Median
type MedianFinder struct {
	// nums are divided equally between left and right by number. left.Len() >= right.Len()
	left  *maxHeap
	right *minHeap
}

// Constructor initialize your data structure here.
func Constructor() MedianFinder {
	left := new(maxHeap)
	heap.Init(left)
	right := new(minHeap)
	heap.Init(right)

	return MedianFinder{
		left:  left,
		right: right,
	}
}

// AddNum Add a number to MedianFinder
func (mf *MedianFinder) AddNum(n int) {
	if mf.left.Len() == mf.right.Len() {
		heap.Push(mf.left, n)
	} else {
		heap.Push(mf.right, n)
	}

	if mf.right.Len() > 0 && mf.left.intHeap[0] > mf.right.intHeap[0] {
		mf.left.intHeap[0], mf.right.intHeap[0] = mf.right.intHeap[0], mf.left.intHeap[0]
		heap.Fix(mf.left, 0)
		heap.Fix(mf.right, 0)
	}
}

// FindMedian gives Median
func (mf *MedianFinder) FindMedian() float64 {
	if mf.left.Len() == mf.right.Len() {
		return float64(mf.left.intHeap[0]+mf.right.intHeap[0]) / 2
	}
	return float64(mf.left.intHeap[0])
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */

// maxHeap.intHeap[0] == max(maxHeap.intHeap)
type maxHeap struct {
	intHeap
}

func (h maxHeap) Less(i, j int) bool {
	return h.intHeap[i] > h.intHeap[j]
}

// minHeap.intHeap[0] == min(minHeap.intHeap)
type minHeap struct {
	intHeap
}

// intHeap implements the heap interface
type intHeap []int

func (h intHeap) Len() int {
	return len(h)
}

func (h intHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h intHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *intHeap) Push(x interface{}) {
	// Push uses *h because
	// Push increases the length of h
	*h = append(*h, x.(int))
}

func (h *intHeap) Pop() interface{} {
	// Pop uses *h because
	// Pop reduces the length of h
	res := (*h)[len(*h)-1]
	*h = (*h)[0 : len(*h)-1]
	return res
}
