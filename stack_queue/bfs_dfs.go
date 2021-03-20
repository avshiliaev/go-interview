package stack_queue

// https://github.com/maximelamure/algorithms/blob/master/datastructure/tree.go

// A Tree is a simple binary tree
type Tree struct {
	root *TNode
}

type TNode struct {
	key   int
	value int
	left  *TNode
	right *TNode
	level int
}

/*
 * int BFS(Node root, Node target) {
		Queue<Node> queue;  // store all nodes which are waiting to be processed
		int step = 0;       // number of steps needed from root to current node
		// initialize
		add root to queue;
		// BFS
		while (queue is not empty) {
			step = step + 1;
			// iterate the nodes which are already in the queue
			int size = queue.size();
			for (int i = 0; i < size; ++i) {
				Node cur = the first node in queue;
				return step if cur is target;
				for (Node next : the neighbors of cur) {
					add next to queue;
				}
				remove the first node from queue;
			}
		}
		return -1;          // there is no path from root to target
	}
*/

// BFS traverses the tree in the level order
func (t *Tree) BFS() <-chan int {
	ch := make(chan int)
	go func() {
		if t.root != nil {
			queue := QueueConstructor()
			queue.EnQueue(t.root)
			for {
				if queue.IsEmpty() {
					break
				}
				n := queue.DeQueue()
				ch <- n.value
				if n.left != nil {
					queue.EnQueue(n.left)
				}
				if n.right != nil {
					queue.EnQueue(n.right)
				}
			}
		}
		close(ch)
	}()

	return ch
}

/*
 * boolean DFS(Node cur, Node target, Set<Node> visited) {
		return true if cur is target;
		for (next : each neighbor of cur) {
			if (next is not in visited) {
				add next to visted;
				return true if DFS(next, target, visited) == true;
			}
		}
		return false;
	}
*/

// DFS traverse the tree in pre-order
func (t *Tree) DFS() <-chan int {
	ch := make(chan int)
	go func() {
		if t.root != nil {
			var stack Stack
			stack.Push(t.root)
			for {
				if stack.IsEmpty() {
					break
				}
				n := stack.Pop()
				ch <- n.value
				if n.right != nil {
					stack.Push(n.right)
				}
				if n.left != nil {
					stack.Push(n.left)
				}
			}
		}
		close(ch)
	}()
	return ch
}
