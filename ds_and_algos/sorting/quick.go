package sorting

func QuickSort(items []int) {
	if len(items) > 1 {
		pivotIndex := len(items) / 2
		var smallerItems []int
		var largerItems []int

		for i := range items {
			val := items[i]
			if i != pivotIndex {
				if val < items[pivotIndex] {
					smallerItems = append(smallerItems, val)
				} else {
					largerItems = append(largerItems, val)
				}
			}
		}

		QuickSort(smallerItems)
		QuickSort(largerItems)

		var merged = append(append(append([]int{}, smallerItems...), []int{items[pivotIndex]}...), largerItems...)
		//merged := MergeLists(smaller\_items, items[pivot\_index], larger\_items)

		for j := 0; j < len(items); j++ {
			items[j] = merged[j]
		}

	}

}
