package linked_list

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */

type SLinkedList struct {
	size       int
	head, tail *ListNode
}

type ListNode struct {
	Val  int
	Next *ListNode
}

// Constructor initialize your data structure here. */
func Constructor() SLinkedList {
	t := &ListNode{}
	h := &ListNode{Next: t}
	return SLinkedList{
		head: h,
		tail: t,
	}
}

// Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
func (l *SLinkedList) Get(index int) int {
	if index < 0 || l.size <= index {
		return -1
	}
	i, cur := 0, l.head.Next
	for i < index {
		i++
		cur = cur.Next
	}
	return cur.Val
}

// AddAtHead a node of value val before the first element of the linked list. After the insertion,
// the new node will be the first node of the linked list.
func (l *SLinkedList) AddAtHead(val int) {
	nd := &ListNode{Val: val}
	nd.Next = l.head.Next
	l.head.Next = nd
	l.size++
}

// AddAtTail append a node of value val to the last element of the linked list.
func (l *SLinkedList) AddAtTail(val int) {
	l.tail.Val = val
	nd := &ListNode{}
	l.tail.Next = nd
	l.tail = nd
	l.size++
}

// AddAtIndex add a node of value val before the index-th node in the linked list.
// If index equals to the length of linked list, the node will be appended to the end of linked list.
// If index is greater than the length, the node will not be inserted.
func (l *SLinkedList) AddAtIndex(index int, val int) {
	switch {
	case index < 0 || l.size < index:
		return
	case index == 0:
		l.AddAtHead(val)
		return
	case index == l.size:
		l.AddAtTail(val)
		return
	}

	i, cur := -1, l.head
	for i+1 < index {
		i++
		cur = cur.Next
	}

	nd := &ListNode{Val: val}
	nd.Next = cur.Next
	cur.Next = nd

	l.size++
}

// DeleteAtIndex delete the index-th node in the linked list, if the index is valid.
func (l *SLinkedList) DeleteAtIndex(index int) {
	if index < 0 || l.size <= index {
		return
	}

	i, cur := -1, l.head
	for i+1 < index {
		i++
		cur = cur.Next
	}

	cur.Next = cur.Next.Next

	l.size--
}
