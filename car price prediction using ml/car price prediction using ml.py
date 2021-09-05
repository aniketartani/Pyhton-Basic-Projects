import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn import  metrics


# data collectoin and processing ____________


car_dataset = pd.read_csv('F:\Samarth projects\python projects\car price prediction using ml\car data.csv')


#inspecting first 5 rows of dataset---------
car_dataset.head()
# getting some information about the dataset
car_dataset.info()
# encoding the categorical data "Fuel_Type"coulmn
car_dataset.replace({'Fuel_Type':{'Petrol':0,'Diesel':1,'CNG':2}},inplace=True)

# encoding the categorical data "Seller_Type"coulmn
car_dataset.replace({'Seller_Type':{'Dealer':0,'Individual':1}},inplace=True)

# encoding the categorical data "Transmission"coulmn
car_dataset.replace({'Transmission':{'Manual':0,'Automatic':1}},inplace=True)

#splitting data into Training data and test data
X = car_dataset.drop(['Car_Name','Selling_Price'],axis = 1)

Y = car_dataset['Selling_Price']
#splitting training and test data
X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size=0.1,random_state=1)

#model training.
#Linear Regression loading 

Lin_reg_model = LinearRegression()
Lin_reg_model.fit(X_train,Y_train)

# model Evaluation

#prediction on trasaining data
training_data_prediction = Lin_reg_model.predict(X_train)
error_score = metrics.r2_score(Y_train , training_data_prediction)
print("R squared Error:", error_score)
#visualize the actual prices and predict the prices
plt.scatter(Y_train, training_data_prediction)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual Prices vs Predicted Prices')
plt.show()
testing_data_prediction = Lin_reg_model.predict(X_test)
error_score = metrics.r2_score(Y_test , testing_data_prediction)
print("R squared Error:", error_score)
#visualize the actual prices and predict the prices
plt.scatter(Y_test, testing_data_prediction)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual Prices vs Predicted Prices')
plt.show()