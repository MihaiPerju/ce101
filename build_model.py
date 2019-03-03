# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder,Imputer

# Importing the dataset
dataset = pd.read_csv('./train.csv')


#Find the  column names
# column_numbers = dataset.count()

#Getting all variables and the target variable
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 80].values

#Split the numerical and categorical variables  by type
numerical_types =['int64','float64']
numerical_columns=[]
categorical_columns=[]
categorical_columns_indexes=[]

for index,column in enumerate(dataset.columns):
    if dataset[column].dtype not in numerical_types:
        categorical_columns.append(column)
        categorical_columns_indexes.append(index)
    else:
        numerical_columns.append(column)

#TODO: Take care of missing data

print(X[:,6].fillna('NaN'))

# Encoding categorical data
labelencoder_X = LabelEncoder()
# for index in categorical_columns_indexes:
#     print(index)
#     X[:, index] = labelencoder_X.fit_transform(X[:, index])
#     print(X[:,index])

# onehotencoder = OneHotEncoder(categorical_features = [2])
# X = onehotencoder.fit_transform(X).toarray()

# print(X)

# Splitting the dataset into the Training set and Test set
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""