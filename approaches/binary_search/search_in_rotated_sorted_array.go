package binary_search

// https://leetcode.com/problems/search-in-rotated-sorted-array/

func search(nums []int, target int) int {
	rotated := indexOfMin(nums) /* Arrays rotated by distance */
	size := len(nums)
	left, right := 0, size-1

	for left <= right {
		mid := (left + right) / 2
		/* nums is rotated, so you need to use rotatedMid to get the value of mid */
		rotatedMid := (rotated + mid) % size
		switch {
		case nums[rotatedMid] < target:
			left = mid + 1
		case target < nums[rotatedMid]:
			right = mid - 1
		default:
			return rotatedMid
		}
	}

	return -1
}

/* nums is an incremental array that has been rotated */
func indexOfMin(nums []int) int {
	size := len(nums)
	left, right := 0, size-1
	for left < right {
		mid := (left + right) / 2
		if nums[right] < nums[mid] {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}
