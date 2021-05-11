package dfs

// https://leetcode.com/problems/validate-binary-search-tree/

// TreeNode Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isValidBST(root *TreeNode) bool {
	// Minimum and maximum values for Go int types
	MIN, MAX := -1<<63, 1<<63-1

	return recur(MIN, MAX, root)
}

// Recursively, check if root.Val is in the (min, max) range.
func recur(min, max int, root *TreeNode) bool {
	if root == nil {
		return true
	}

	return min < root.Val && root.Val < max &&
		recur(min, root.Val, root.Left) &&
		recur(root.Val, max, root.Right)
}
