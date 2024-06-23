## **Random Permutations**

- Random Permutations means changing the arrangement of elements in a sequence or a group.
- Random Permutations is used to randomly permute a sequence or return a permuted range.
- The `shuffle()` method is used to shuffle the sequence.
- The `permutation()` method is used to return a new array by shuffling the elements of the original array.

## **Seaborn**

- Seaborn is a Python data visualization library based on matplotlib.
- It provides a high-level interface for drawing attractive and informative statistical graphics.
- Seaborn is a library for making statistical graphics in Python.
- It is built on top of matplotlib and closely integrated with pandas data structures.

### **Basic plot using seaborn**

- `sns.histplot()` function is used to draw a histogram of a dataset.

  - `Data`: 1-dimensional array-like.
  - `x, y`: names of variables in data or vector data, optional.
  - `bins`: specifies the number of bins to use when grouping the data.
  - `kde`: whether to plot a gaussian kernel density estimate.
  - `color`: color of the plot elements.
  - `label`: label for the plot.

- `sns.displot()` function is used to draw the univariate set of distributions and plot the histogram with `kde` and `rug`

  - `a`: 1-dimensional array-like.
  - `bins`: specifies the number of bins to use when grouping the data.
  - `kde`: whether to plot a gaussian kernel density estimate.
  - `rug`: whether to draw a rugplot on the support axis.
  - `hist`: whether to draw a histogram.

- `sns.lineplot()` function is used to draw a line plot with possibility of several semantic groupings.

  - `x, y`: names of variables in data or vector data, optional.
  - `hue`: name in data, optional.
  - `style`: name in data, optional.
  - `size`: name in data, optional.
  - `data`: DataFrame, array, or list of arrays, optional.
  - `palette`: palette name, list, or dict, optional.
  - `markers`: boolean, optional.
  - `dashes`: boolean, optional.

- `sns.lmplot()` function is used to draw a scatterplot of two variables with a linear regression model fit.

  - `x, y`: names of variables in data or vector data, optional.
  - `hue`: name in data, optional.
  - `data`: DataFrame, array, or list of arrays, optional.
  - `palette`: palette name, list, or dict, optional.
  - `markers`: boolean, optional.
  - `dashes`: boolean, optional.

- `sns.barplot()` function is used to draw a bar plot.
  
  - `x, y`: names of variables in data or vector data, optional.
  - `hue`: name in data, optional.
  - `data`: DataFrame, array, or list of arrays, optional.
  - `palette`: palette name, list, or dict, optional.
  - `orient`: orientation of the plot (vertical or horizontal).
  - `color`: color of the plot elements.

## **Summary**

- Random Permutations is used to randomly permute a sequence or return a permuted range.
- Seaborn provides a high-level interface for drawing attractive and informative statistical graphics.
- Seaborn is built on top of matplotlib and closely integrated with pandas data structures.
- Seaborn provides a variety of functions to plot different types of graphs.

