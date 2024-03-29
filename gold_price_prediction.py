import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

"""Data Colllection and Processing"""

gold_data = pd.read_csv('/content/gld_price_data.csv')

gold_data.head()

gold_data.tail()

# number of rows and columns
gold_data.shape

# getting some basic informations about the data
gold_data.info()

# getting the statistical measures of the data
gold_data.describe()

# constructing a heatmap to understand the correlatiom
plt.figure(figsize = (8,8))
corr = gold_data.corr()
sns.heatmap(corr,
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values,
            annot=True,fmt='.2f',linewidths=0.30)
plt.title('Correlation of gold data  Features', y = 1.05, size=15)

#correlation score
print (corr['GLD'].sort_values(ascending=False), '\n')

# checking the distribution of the GLD Price
sns.distplot(gold_data['GLD'],color='green')

#relation with GLD variable
sns.jointplot(x = gold_data['SLV'], y = gold_data['GLD'], color = 'orange')

#relation with GLD variable
sns.jointplot(x = gold_data['SPX'], y = gold_data['GLD'], color = 'purple')

#spliting the feature and target
X = gold_data.drop(['Date','GLD'],axis=1)
Y = gold_data['GLD']
print(X,'\n')
print(Y)

#spliting into training data and Test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=2)

#model training: Random Forest Regressor
regressor = RandomForestRegressor(n_estimators=100)

# training the model
regressor.fit(X_train,Y_train)

"""**Model Evaluation**"""

# prediction on Test Data
test_data_prediction = regressor.predict(X_test)

print(test_data_prediction)

# R squared error
error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared error : ", error_score)

"""**Compare the Actual Values and Predicted Values in a Plot**"""

Y_test = list(Y_test)

plt.plot(Y_test, color='blue', label = 'Actual Value')
plt.plot(test_data_prediction, color='red', label='Predicted Value')
plt.title('Actual Price vs Predicted Price')
plt.xlabel('Number of values')
plt.ylabel('GLD Price')
plt.legend()
plt.show()
