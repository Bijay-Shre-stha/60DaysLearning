## **Cleaning Data**

- Data cleaning means fixing bad data in your data set.
- Bad data could be:
  - Empty cells
  - Data in wrong format
  - Wrong data
  - Duplicates
- Pandas provides methods for cleaning data.

## **Cleaning Empty Cells**

- Pandas treats `None` and `NaN` as missing values.
- To deal with missing values, we can use the `fillna()` method.
- The `fillna()` method is useful for filling missing values with a specific value.
- `dropna()` method is used to remove rows with missing values.
- `dropna(inplace = True)` will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.
- `fillna( value = 130, inplace = True)` will replace all NULL values with 130 in the original DataFrame.
- `replace()` method is used to replace a specified value with another value.
  - mean() method returns the mean value for the requested axis.
  - median() method returns the median value for the requested axis.
  - mode() method returns the mode value for the requested axis.

## **Cleaning Wrong Format**

- To fix wrong format, we can use the `astype()` method.
- The `astype()` method is used to change data types of columns.
- The data types are important because there are certain operations that can only be performed on certain data types.
- The data types are important because there are certain operations that can only be performed on certain data types.
- The `to_datetime()` method is used to convert a column to datetime.
- The `to_numeric()` method is used to convert a column to numeric.

## **Cleaning Wrong Data**

- When you have incorrect data, you can use the `replace()` method to replace the wrong data with something else.
- The `replace()` method is a useful method for replacing values in a DataFrame.
- The `replace()` method is a useful method for replacing values in a DataFrame.

## **Cleaning Duplicates**

- Duplicate rows are rows that have been registered more than one time.
- By taking a look at our test data set, we can assume that row 11 and 12 are duplicates.
- To discover duplicates, we can use the `duplicated()` method.
- The `duplicated()` method returns a Boolean values for each row.
- The `drop_duplicates()` method is used to remove duplicates.
- The `drop_duplicates()` method returns a new DataFrame without the duplicates.

## **Summary**

- Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset.
- Pandas provides methods for cleaning data.
- The `fillna()` method is useful for filling missing values with a specific value.
- The `dropna()` method is used to remove rows with missing values.
- The `astype()` method is used to change data types of columns.
- The `replace()` method is a useful method for replacing values in a DataFrame.
- The `duplicated()` method returns a Boolean values for each row.
- The `drop_duplicates()` method is used to remove duplicates.