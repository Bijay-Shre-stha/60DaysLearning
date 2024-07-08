## **Pandas**

- Pandas is a fast, powerful, flexible and easy to use open source data analysis and data manipulation library built on top of the Python programming language.
- It is a popular library for data analysis and is used in many applications ranging from commercial to academic research.
- Pandas is well suited for many different kinds of data:
  - Tabular data with heterogeneously-typed columns, as in an SQL table or Excel spreadsheet
  - Ordered and unordered (not necessarily fixed-frequency) time series data.
  - Arbitrary matrix data with row and column labels
  - Any other form of observational / statistical data sets. The data actually need not be labeled at all to be placed into a pandas data structure.
- The two primary data structures of pandas are:
  - **Series**: A one-dimensional array-like object containing an array of data and an associated array of data labels, called its index.
  - **DataFrame**: A two-dimensional table of data with rows and columns. It is conceptually a dictionary of Series objects.

## **Pandas: Series**

- A Series is a one-dimensional array-like object containing an array of data and an associated array of data labels, called its index.
- The basic method to create a Series is to call:

   ```python
  s = pd.Series(data, index=index)
  ```

  Here, `data` can be many different things:
  - A Python dict
  - An ndarray
  - A scalar value (like 5)
- The passed index is a list of axis labels. If you pass an index and data, the result will be:

## **Pandas DataFrames**

- A DataFrame is a two-dimensional table of data with rows and columns.
- It is conceptually a dictionary of Series objects.
- The DataFrame has both a row and column index.
- A DataFrame can be created from various data types like:
  - Lists
  - Dicts
  - Series
  - Numpy ndarrays
  - Another DataFrame
- The DataFrame can be created using the following constructor:

## **Summary**

- **Pandas** is a powerful data analysis and data manipulation library built on top of Python.
- **Series** is a one-dimensional array-like object containing an array of data and an associated array of data labels.
- **DataFrame** is a two-dimensional table of data with rows and columns. It is conceptually a dictionary of Series objects.
- A DataFrame can be created from various data types like lists, dicts, Series, Numpy ndarrays, or another DataFrame.
