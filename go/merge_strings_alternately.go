package main

import (
    "fmt"
    "math"
)

// mergeAlternately merges two input strings alternately.
// It takes two strings, word1 and word2, and returns a new string
// with the characters from word1 and word2 merged alternately.
// If one word is longer than the other, the remaining characters
// from the longer word are appended to the end of the merged string.
func mergeAlternately(word1 string, word2 string) string {
	var alternatelyMergedWords string

	// Determine the maximum and minimum lengths of the input words
	maxWordLen := int(math.Max(float64(len(word1)), float64(len(word2))))
	minWordLen := int(math.Min(float64(len(word1)), float64(len(word2))))

	// Merge the characters from word1 and word2 alternately
	for i := 0; i < minWordLen; i++ {
		alternatelyMergedWords += word1[i:i+1]
		alternatelyMergedWords += word2[i:i+1]
	}

	// If one word is longer than the other, append the remaining characters
	if maxWordLen != minWordLen {
		if len(word1) > len(word2) {
			alternatelyMergedWords += word1[minWordLen:maxWordLen]
		} else {
			alternatelyMergedWords += word2[minWordLen:maxWordLen]
		}
	}

	return alternatelyMergedWords
}

func main() {
    fmt.Println( mergeAlternately("abc", "pqrasdf") )
}