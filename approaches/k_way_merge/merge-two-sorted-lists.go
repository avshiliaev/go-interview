package k_way_merge

// https://leetcode.com/problems/merge-two-sorted-lists/

// ListNode definition
type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	// One chain is nil, return another chain directly
	if l1 == nil {
		return l2
	}
	if l2 == nil {
		return l1
	}

	// At this point, neither chain is nil, so you can just use l.Val without worrying about panic
	// Between l1 and l2, choose the smaller node as head and set the node
	var head, node *ListNode
	if l1.Val < l2.Val {
		head = l1
		node = l1
		l1 = l1.Next
	} else {
		head = l2
		node = l2
		l2 = l2.Next
	}

	// Loop through the values of l1 and l2, always choosing the smaller value to connect to the node
	for l1 != nil && l2 != nil {
		if l1.Val < l2.Val {
			node.Next = l1
			l1 = l1.Next
		} else {
			node.Next = l2
			l2 = l2.Next
		}

		// With this step, the head is a complete chain
		node = node.Next
	}

	if l1 != nil {
		// Connect the remaining chain of l1
		node.Next = l1
	}

	if l2 != nil {
		// Connect the remaining chain of l2
		node.Next = l2
	}

	return head
}
