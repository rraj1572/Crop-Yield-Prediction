import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
url = './data.py'
data = pd.read_csv(url)
data = data.head(1000)

# Drop unnecessary columns
data = data.drop(['State_Name', 'District_Name', 'Crop_Year', 'Season', 'Crop'], axis=1)

# Calculate Yield by dividing Production by Area
data['Yield'] = data['Production'] / data['Area']

# Remove missing values
data = data.dropna()

# Split the data into features and target variable
X = data[['Area', 'Production']]
y = data['Yield']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(X_train, y_train)

# Evaluate the model
y_pred = rf_regressor.predict(X_test)
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
print('R-squared:', r2_score(y_test, y_pred))

pickle.dump(rf_regressor, open('model.pkl', 'wb'))
