## **Array Iterating**

- Iterating means going through elements one by one. As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
- If we iterate on a 1-D array it will go through each element one by one.
- If we iterate on a 2-D array it will go through each row.
- If we iterate on a 3-D array it will go through each 2-D array.
- If we iterate on a n-D array it will go through n-1th dimension one by one.
- `nditer()` is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration, lets see how it works.

## **Array Join**

- Joining means putting contents of two or more arrays in a single array.
- `Concatenate()` function is used to join arrays along an existing axis.
- `Stack()` function is used to join the sequence of same shaped arrays along a new axis.
- `Axis` parameter is used in both the functions, default is 0
- `hstack()` function is used to stack arrays in sequence horizontally (column wise).
- `vstack()` function is used to stack arrays in sequence vertically (row wise).
- `dstack()` function is used to stack arrays in sequence depth wise (along third axis).

## **Array Split**

- Splitting is reverse operation of Joining.
- `array_split()` is equivalent to `split()` function but it splits an array into multiple sub-arrays.
- `hsplit()` function is used to split an array into multiple sub-arrays horizontally (column-wise).
- `vsplit()` function is used to split an array into multiple sub-arrays vertically (row-wise).
- `dsplit()` function is used to split an array into multiple sub-arrays depth wise (along third axis).

## **Summary**

- We can iterate on an array using basic for loop of python.
- `nditer()` is a helping function that can be used from very basic to very advanced iterations.
- `Concatenate()` function is used to join arrays along an existing axis.
- `Stack()` function is used to join the sequence of same shaped arrays along a new axis.
- `Axis` parameter is used in both the functions, default is 0
- `hstack()` function is used to stack arrays in sequence horizontally (column wise).
- `vstack()` function is used to stack arrays in sequence vertically (row wise).
- `dstack()` function is used to stack arrays in sequence depth wise (along third axis).
- `array_split()` is equivalent to `split()` function but it splits an array into multiple sub-arrays.
- `hsplit()` function is used to split an array into multiple sub-arrays horizontally (column-wise).
- `vsplit()` function is used to split an array into multiple sub-arrays vertically (row-wise).
- `dsplit()` function is used to split an array into multiple sub-arrays depth wise (along third axis).

