## **Implementation of Sorting Function**

- Without using the built-in `sort()` function, we can implement our own sorting function.
- The function can be implemented using the bubble sort algorithm.
- The bubble sort algorithm compares each pair of adjacent elements and swaps them if they are in the wrong order.
- The process is repeated until no more swaps are needed.

## **Array Search**

- `numpy.where()` function returns the indices of elements in an input array where the given condition is satisfied.
- `numpy.searchsorted()` function returns the indices where the specified value would be inserted to maintain the order of the array.
- Default search is from left to right, but it can be changed to right to left using the `side` parameter.

## **Array Sorting**

- `numpy.sort()` function returns a sorted copy of an input array.
- This method returns a copy of the array, leaving the original array unchanged.

## **Array Filter**

- Getting some elements out of an existing array and creating a new array out of them is called filtering.
- A boolean index list is a list of booleans corresponding to indexes in the array.
- If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

## **Summary**

- We learned how to implement a sorting function, search for elements in an array, sort an array, and filter an array in NumPy.
- These functions are useful for manipulating and analyzing data in NumPy arrays.
