package topological_sorting

// https://leetcode.com/problems/course-schedule/

func canFinish(numCourses int, prerequisites [][]int) bool {
	// next[i][j] : i -> next[i]... , i is a pre-requisite for next[i]
	next := buildNext(numCourses, prerequisites)
	// pres[i] : **number of pre-requisite courses** for i
	pres := buildPres(next)

	return check(next, pres, numCourses)
}

func buildNext(n int, prereq [][]int) [][]int {
	next := make([][]int, n)

	for _, pair := range prereq {
		next[pair[1]] = append(next[pair[1]], pair[0])
	}

	return next
}

func buildPres(next [][]int) []int {
	pres := make([]int, len(next))

	for _, neighbours := range next {
		for _, n := range neighbours {
			pres[n]++
		}
	}

	return pres
}

func check(next [][]int, pres []int, numCourses int) bool {
	var i, j int

	// The code for the i-th completed course is j
	for i = 0; i < numCourses; i++ {
		// Complete the first course encountered, which does not require a prerequisite
		for j = 0; j < numCourses; j++ {
			if pres[j] == 0 {
				break
			}
		}

		// Every course requires a pre-requisite
		// Loops appear
		if j >= numCourses {
			return false
		}

		// Modify pres[j] to a negative number
		// Avoid reworking
		pres[j] = -1
		// After completing course j
		// For subsequent courses of j, the number of pre-requisite courses can be -1
		for _, c := range next[j] {
			pres[c]--
		}
	}

	return true
}
