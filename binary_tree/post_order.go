package binary_tree

func postOrderTraversal(root *TreeNode) []int {
	var stack []*TreeNode
	var res []int

	cur := root
	for cur != nil {
		if cur.Left == nil && cur.Right == nil {
			res = append(res, cur.Val)
			if len(stack) == 0 {
				break
			}
			cur = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
		} else {
			left, right := cur.Left, cur.Right
			cur.Left, cur.Right = nil, nil
			stack = append(stack, cur)

			if left != nil {
				cur = left
				if right != nil {
					stack = append(stack, right)
				}
			} else { // left == nil
				cur = right
			}
		}
	}

	return res
}
