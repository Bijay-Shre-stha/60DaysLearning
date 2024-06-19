## **Data Types**

- Data types in NumPy are specified using the `dtype` object.
- Below is a list of all data types in NumPy and the characters used to represent them.
  - `i` - integer
  - `b` - boolean
  - `u` - unsigned integer
  - `f` - float
  - `c` - complex float
  - `m` - timedelta
  - `M` - datetime
  - `O` - object
  - `S` - string
  - `U` - unicode string
  - `V` - fixed chunk of memory for other type ( void )

## **Copy vs View**

- **Copy**: A copy of the original array is created in a different memory location.
- **View**: A view of the original array is created, i.e., the same memory location is used for the new array.
- Copy  owns the data and any changes made to the copy won't affect the original array.
- View does not own the data and any changes made to the view will affect the original array.
- To check if an array is a copy or a view, use the `base` attribute. If the array is a view, the `base` attribute will return the original array.

## **Array Shape & Reshape**

- The `shape` of an array is the number of elements in each dimension.
- The `shape` attribute returns a tuple representing the shape of the array.
- `ndmin` attribute returns the number of dimensions of the array.

- The `reshape()` function is used to change the shape of an array.
- The new shape should be compatible with the original shape.
- If the new shape is not compatible, a copy of the original array will be created.
- Unknown dimensions can be passed as `-1` in the `reshape()` function, and NumPy will calculate the dimension based on the number of elements.
- Flattening an array means converting a multidimensional array into a 1D array.

## **Summary**

- **Data Types**: Data types in NumPy are specified using the `dtype` object.
- **Copy vs View**: A copy of the original array is created in a different memory location, while a view of the original array is created using the same memory location.
- **Array Shape & Reshape**: The `shape` of an array is the number of elements in each dimension. The `reshape()` function is used to change the shape of an array.
