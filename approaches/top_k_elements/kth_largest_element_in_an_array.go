package top_k_elements

import "container/heap"

// https://leetcode.com/problems/kth-largest-element-in-an-array/

func findKthLargest(nums []int, k int) int {
	temp := highHeap(nums)
	h := &temp
	heap.Init(h)

	if k == 1 {
		return (*h)[0]
	}

	for i := 1; i < k; i++ {
		heap.Remove(h, 0)
	}

	return (*h)[0]
}

// highHeap implements the heap interface
type highHeap []int

func (h highHeap) Len() int {
	return len(h)
}
func (h highHeap) Less(i, j int) bool {
	// h[i] > h[j] such that h[0] == max(h...)
	return h[i] > h[j]
}
func (h highHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *highHeap) Push(x interface{}) {
	// Push uses *h because
	// Push increases the length of h
	*h = append(*h, x.(int))
}

func (h *highHeap) Pop() interface{} {
	// Pop uses *h because
	// Pop reduces the length of h
	res := (*h)[len(*h)-1]
	*h = (*h)[0 : len(*h)-1]
	return res
}
