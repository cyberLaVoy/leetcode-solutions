// sortArrayByParity sorts an array of integers by parity, where even numbers come before odd numbers.
func sortArrayByParity(nums []int) []int {
	// Create a new slice with the same length as the input slice
	// to store the sorted numbers by parity.
	paritySortedSlice := make([]int, len(nums))
	// Initialize the index for the next empty position in the slice.
	currEmptyArrayIndex := 0
	// Iterate over the input slice to find even numbers and place them in the sorted slice.
	for i := 0; i < len(nums); i++ {
		if nums[i]%2 == 0 {
			// Place the even number in the sorted slice at the current empty position.
			paritySortedSlice[currEmptyArrayIndex] = nums[i]
			// Move to the next empty position in the sorted slice.
			currEmptyArrayIndex++
		}
	}
	// Iterate over the input slice again to find odd numbers and place them in the sorted slice.
	for i := 0; i < len(nums); i++ {
		if nums[i]%2 == 1 {
			// Place the odd number in the sorted slice at the current empty position.
			paritySortedSlice[currEmptyArrayIndex] = nums[i]
			// Move to the next empty position in the sorted slice.
			currEmptyArrayIndex++
		}
	}
	// Return the sorted slice by parity.
	return paritySortedSlice
}