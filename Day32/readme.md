## **ufunc Intro**

- **ufunc** stands for "Universal Functions" in NumPy.
- They are the functions that operate element by element on whole arrays.
- They are fast vectorized wrappers for simple functions that take one or more scalar values and produce one or more scalar results.
- unfuncs also take additional arguments, like:
  - `out`: to specify where the result should be stored.
  - `where`: to specify conditions when the operation should be performed.
  - `dtype`: to specify the data type of the returned array.

### **Why a ufunc**

- **ufuncs** are used to implement vectorization in NumPy, which is way faster than iterating over elements.
- They are flexible and can be customized for specific applications.
- They are implemented in compiled C code, making them fast.

### **What is Vectorization?**

- Vectorization is the process of converting a scalar operation into a vector operation.
- It is faster as it pushes more of the computational load into the compiled layer.

## **Creating a ufunc**

- We can create our own **ufunc** using the `frompyfunc()` method.
- The frompyfunc() method takes the following arguments:
  - `function` - the name of the function.
  - `inputs` - the number of input arguments (arrays).
  - `outputs` - the number of output arrays.

## **Simple Arithmetic Using ufunc**

- We can perform simple arithmetic operations using **ufunc**.
- For example, we can add two arrays element-wise using the `add()` function.
- Other arithmetic functions include `subtract()`, `multiply()`, `divide()`, `power()`, etc.
- These functions can also be used with scalar values.

## **Summary**

- **ufunc** stands for "Universal Functions" in NumPy.
- They operate element by element on whole arrays.
- They are fast vectorized wrappers for simple functions.
- **ufuncs** are used to implement vectorization in NumPy, making operations faster.
- We can create our own **ufunc** using the `frompyfunc()` method.
- Simple arithmetic operations can be performed using **ufunc** functions like `add()`, `subtract()`, `multiply()`, etc.
