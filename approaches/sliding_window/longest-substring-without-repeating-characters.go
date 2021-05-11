package sliding_window

// https://leetcode.com/problems/longest-substring-without-repeating-characters/

func lengthOfLongestSubstring(s string) int {
	// location[s[i]] == j means.
	// i-th string in s, last occurrence in s at location j, so, no s[i] in s[j+1:i]
	// location[s[i]] == -1 means: // first occurrence of s[i] in s
	location := [256]int{} // Only 256 long because it is assumed that the input string is only ASCII characters
	for i := range location {
		location[i] = -1 // First set all characters not seen
	}

	maxLen, left := 0, 0

	for i := 0; i < len(s); i++ {
		// means that s[i] has been repeated in s[left:i+1]
		// and s[i] was last seen in location[s[i]]
		if location[s[i]] >= left {
			left = location[s[i]] + 1 // Remove the s[i] character and the part before it in s[left:i+1]
		} else if i+1-left > maxLen {
			// fmt.Println(s[left:i+1])
			maxLen = i + 1 - left
		}
		location[s[i]] = i
	}

	return maxLen
}
