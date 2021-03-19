package data_structures

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
	head, tail *node
}

type node struct {
	val  int
	next *node
}

// Constructor initialize your data structure here. */
func Constructor() SLinkedList {
	t := &node{}
	h := &node{next: t}
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
	i, cur := 0, l.head.next
	for i < index {
		i++
		cur = cur.next
	}
	return cur.val
}

// AddAtHead a node of value val before the first element of the linked list. After the insertion,
// the new node will be the first node of the linked list.
func (l *SLinkedList) AddAtHead(val int) {
	nd := &node{val: val}
	nd.next = l.head.next
	l.head.next = nd
	l.size++
}

// AddAtTail append a node of value val to the last element of the linked list.
func (l *SLinkedList) AddAtTail(val int) {
	l.tail.val = val
	nd := &node{}
	l.tail.next = nd
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
		cur = cur.next
	}

	nd := &node{val: val}
	nd.next = cur.next
	cur.next = nd

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
		cur = cur.next
	}

	cur.next = cur.next.next

	l.size--
}
