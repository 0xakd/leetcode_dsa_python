# Algorithm: #49 Group Anagram

### Step 1:

Check if the input list is empty.
If it is, return an empty list [].


### Step 2:

Create a function that converts each string into a frequency string.

For example:
"apple" → "a1e1l1p2"

This frequency string represents how many times each character appears in the string after sorting the characters in ascending order.
	•	a → appears 1 time
	•	e → appears 1 time
	•	l → appears 1 time
	•	p → appears 2 times

If two strings have the same frequency string, they are anagrams and should be grouped together.


### Step 3:

Iterate over the list of strings.
For each string, compute its frequency string using the function created in Step 2.

### Step 4:

Group strings that have the same frequency string using a map (dictionary) or list.
Each unique frequency string acts as a key, and its corresponding value is a list of strings that share that frequency.

### Final Output:

Return the grouped anagrams as a list of lists.
