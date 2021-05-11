package sorting

const NADA int = -1

func DeepCopy(values []int) []int {
	tmp := make([]int, len(values))
	copy(tmp, values)
	return tmp
}

func MergeSort(items []int) {

	if len(items) > 1 {
		mid := len(items) / 2
		left := DeepCopy(items[0:mid])
		right := DeepCopy(items[mid:])

		MergeSort(left)
		MergeSort(right)

		l := 0
		r := 0

		for i := 0; i < len(items); i++ {

			lValues := NADA
			rValues := NADA

			if l < len(left) {
				lValues = left[l]
			}

			if r < len(right) {
				rValues = right[r]
			}

			if (lValues != NADA && rValues != NADA && lValues < rValues) || rValues == NADA {
				items[i] = lValues
				l += 1
			} else if (lValues != NADA && rValues != NADA && lValues >= rValues) || lValues == NADA {
				items[i] = rValues
				r += 1
			}

		}
	}

}
