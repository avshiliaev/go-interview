package data_structures

// Remove the (L - n + 1) th node from the beginning in the list.
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	d, headIsNthFromEnd := getParent(head, n)

	if headIsNthFromEnd {
		return head.Next
	}

	d.Next = d.Next.Next

	return head
}

func getParent(head *ListNode, n int) (parent *ListNode, headIsNthFromEnd bool) {
	parent = head

	for head != nil {
		if n < 0 {
			parent = parent.Next
		}

		n--
		head = head.Next
	}

	headIsNthFromEnd = n == 0

	return
}
