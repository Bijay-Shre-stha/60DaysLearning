## **ufunc Rounding Decimals**

### Rounding Decimals

- Rounding means reducing the number of digits in a number to make it simpler and easier to work with.

- NumPy provides ufuncs to round decimal numbers.
- The `around()` function rounds the elements of an array to the nearest integer.
- The `floor()` function rounds the elements of an array to the nearest integer towards zero.
- The `ceil()` function rounds the elements of an array to the nearest integer towards infinity.
- The `trunc()` function rounds the elements of an array towards zero.
- The `fix()` function rounds the elements of an array towards zero.

## **ufunc Logs**

- NumPy provides ufuncs to perform logarithmic functions.
- The `log()` function returns the natural logarithm of the elements of the array.
- The `log2()` function returns the base 2 logarithm of the elements of the array.
- The `log10()` function returns the base 10 logarithm of the elements of the array.

### Note

`NumPy does not provide any function to take log at any base, so we can use the frompyfunc()* function along with inbuilt function **math.log()** with two input parameters and one output parameter to take log at any base.
`

## **ufunc Summations**

- NumPy provides ufuncs to perform summations.
- The `sum()` function sums the elements of an array.
- The `cumsum()` function returns the cumulative sum of the elements along a given axis.
- The `prod()` function returns the product of the elements of the array.
- The `cumprod()` function returns the cumulative product of the elements along a given axis.

## **Summary**

- NumPy provides ufuncs to round decimal numbers.
- NumPy provides ufuncs to perform logarithmic functions.
- NumPy provides ufuncs to perform summations.
