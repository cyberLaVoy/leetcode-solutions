// nextGreatestLetter finds the next lexicographically greatest letter in a sorted array of letters
// given a target letter. If no greater letter is found, it returns the first letter in the array.
func nextGreatestLetter(letters []byte, target byte) byte {
    // Initialize the next greatest letter as the first letter in the array
    nextGreatestLetter := letters[0]
    // Iterate through each letter in the array
    for i := 0; i < len(letters); i++ {
        // If the current letter is greater than the target letter,
        // update the next greatest letter and exit the loop
        if letters[i] > target {
            nextGreatestLetter = letters[i]
            break
        }
    }
    // Return the next greatest letter found
    return nextGreatestLetter
}