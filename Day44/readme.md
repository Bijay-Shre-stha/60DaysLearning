# **Project: Titanic - Machine Learning from Disaster**

## **Description**

In this project, we'll work on the Titanic dataset from Kaggle to predict the survival of passengers based on various features. We'll explore the dataset, clean and preprocess it, and then build a machine learning model to predict whether a passenger survived or not. This project will help you get familiar with the basics of machine learning, classification algorithms, and data preprocessing techniques.

## **Topics**

- Data Analysis
- Data Preprocessing
- Machine Learning
- Classification

## **Skills**

- Data Analysis
- Python
- Machine Learning
- Classification

## **Dataset**

The dataset for this project can be downloaded from the following link:

- [Titanic Dataset](https://www.kaggle.com/c/titanic/data)

## Data Dicitonary

- PassengerId: A column added by Kaggle to identify each row and make submissions easier
- Survived: Whether the passenger survived or not and the value we are predicting (0=No, 1=Yes)
- Pclass: The class of the ticket the passenger purchased (1=1st, 2=2nd, 3=3rd)
- sibsp: The number of siblings or spouses the passenger had aboard the Titanic
- Parch: The number of parents or children the passenger had aboard the Titanic
- Ticket: The passenger’s ticket number
- Fare: The fare the passenger paid
- Cabin: The passenger’s cabin number
- Embarked: The port where the passenger embarked (C=Cherbourg, Q=Queenstown, S=Southampton)

## Models Evaluated

Several machine learning models were evaluated for their accuracy in predicting survival. The following models were tested:

1. **Support Vector Classifier (SVC)**: Achieved the highest accuracy of 83.5%. This model is likely the best starting point for further analysis, but be aware of its computational complexity and lower interpretability.

2. **KNeighbors Classifier**: Achieved an accuracy of 82.6%. This model is simpler and easy to understand, making it a good choice if interpretability is a priority.

3. **Logistic Regression**: Achieved an accuracy of 81.26%. This model is robust and interpretable, often used as a strong baseline model in classification tasks.

4. **Gradient Boosting Classifier**: Achieved an accuracy of 81.25%. This model handles complex data well and is commonly used in many winning Kaggle competitions.

5. **Random Forest Classifier**: Achieved an accuracy of 80.7%. This ensemble method reduces overfitting compared to single decision trees and provides a good balance between performance and interpretability.

6. **Decision Tree Classifier**: Achieved an accuracy of 79.58%. This model is highly interpretable but prone to overfitting.

7. **Gaussian Naive Bayes**: Achieved an accuracy of 78.78%. This model is simple and fast but makes strong assumptions about the data.


## **Summary**

In this project, we'll work on the Titanic dataset from Kaggle to predict the survival of passengers based on various features. We'll explore the dataset, clean and preprocess it, and then build a machine learning model to predict whether a passenger survived or not. This project will help you get familiar with the basics of machine learning, classification algorithms, and data preprocessing techniques.

## **References**

- [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic)
- [Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/overview)
