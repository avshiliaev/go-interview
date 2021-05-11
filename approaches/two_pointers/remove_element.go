package two_pointers

// https://leetcode.com/problems/remove-element/

func removeElement(nums []int, val int) int {
	// j points to the last position that is not val
	// i points to the first position with a value of val
	i, j := 0, len(nums)-1
	for {
		for i < len(nums) && nums[i] != val {
			i++
		}

		for j >= 0 && nums[j] == val {
			j--
		}

		if i >= j {
			break
		}

		nums[i], nums[j] = nums[j], nums[i]
	}

	return i
}
