## **Project-I: MAGIC Gamma Telescope**

This project involves using data from the MAGIC Gamma Telescope to classify gamma (signal) and hadron (background) events.

### **Data Source**

The data for this project can be downloaded from the UCI Machine Learning Repository: [MAGIC Gamma Telescope Data](https://archive.ics.uci.edu/ml/datasets/MAGIC+Gamma+Telescope)

The data file is named `magic04.data`.

### **Data Description**

The dataset contains the following columns:

1. **fLength**: continuous
2. **fWidth**: continuous
3. **fSize**: continuous
4. **fConc**: continuous
5. **fConc1**: continuous
6. **fAsym**: continuous
7. **fM3Long**: continuous
8. **fM3Trans**: continuous
9. **fAlpha**: continuous
10. **fDist**: continuous
11. **class**: g (gamma, signal), h (hadron, background)

## **Model Classification**

# K-nearest Neighbors (KNN)

K-nearest neighbors (KNN) is a type of supervised learning algorithm used for classification. It classifies data points based on their similarity to other data points.

## Key Concepts

- **K**: K is the number of neighbors to consider when classifying a data point.
- **Distance Metric**: The distance metric is used to measure the similarity between data points.
- **Majority Class**: The majority class is the class that occurs most frequently among the K-nearest neighbors.
- **Euclidean Distance**: Euclidean distance is a common distance metric used in K-nearest neighbors.

![KNN](image.png)
![KNN](image-1.png)