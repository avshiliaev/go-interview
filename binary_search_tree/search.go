package binary_search_tree

func searchBST(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return nil
	}
	switch {
	case root.Val < val:
		return searchBST(root.Right, val)
	case val < root.Val:
		return searchBST(root.Left, val)
	default:
		return root
	}
}
