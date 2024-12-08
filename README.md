# House_Price_Prediction
#House Price Prediction using Linear Regression.  This project uses a linear regression model to predict house prices based on various features. The model is trained on a dataset of house characteristics and their corresponding prices, and its performance is evaluated using common refression metrics.

## Problem Statement
The goal of this project is to build a machine learning model that can accurately predict the price of a house given its features. Accurate house price prediction is valuable for real estate agents, buyers, and sellers. This project aims to create a model that can provide reasonably accurate predictions. This can be used to help buyers and sellers determine a fair price for a property, or to help real estate agents value properties they are trying to sell or buy.

## Dataset
The dataset used in this project is stored in a SQL Server database named 'House_DB'. The table within the database , named house_data, contains the following xolumns:
* 'house_id' (INT, primary Key, Auto-incrementing): Unique identifier for each house.
* 'bedrooms' (INT): Number of bedrooms.
* 'bathrooms' (INT): Number of bathrooms.
* 'square_footage (INT): Total square footage of the house.
* 'lot_size' (DECIMAL): Size of the lot in acres.
* 'location' (VARCHAR): Location of the house (categorical).
* 'year_built' (INT): Year the house was built.
* 'price' (DECIMAL): Sale price of the house (target variable).

## Evaluation Metric
The model's performance is evaluated using the following metrics:
* **Mean Squared Error (MSE):** Measures the average squared difference between the predicted and actual house prices. A lower MSE indicates better model accuracy.
* **R-squared (R2):** Represents the proportion of variance in the target variable (house price) that is predictable from the features. A higher R2 indicates a better fit (closer to 1).

## Project Steps
1. **Database Connection:** The project starts by establishing a connection to the SQL Server database using the 'pyodbc' library. The connection details are stored securely in the Python script.
2. **Data Retrieval:** A SQL query is executed to fetch the relevant data from the 'house_data' table. The data is then loaded into Pandas DataFrame for processing.
3. **Data Preprocessing:** The data is cleaned and preprocessed as needed. This includes handling missing values (filled with the mean for numeric columns), and possibly transforming variables (e.g. using scaling or one-hot encoding).
4. **Model Training:** A linear regression model is trained using the preprocessed data. The data is split into training and testing sets to evaluate the model's performance on unseen data. The 'Scikit-learn' library is used for model training.
5. **Model Evaluation:** The trained model is evaluated using MSE and R2. The model coefficients are also printed to show the relationship between features and predicted price.
6. **Prediction:** The trained model can then be used to predict house prices based on new input features.

## Technologies used
* Python
* 'pyodbc'
* 'pandas'
* 'scikit-learn'
* SQL Server
 
