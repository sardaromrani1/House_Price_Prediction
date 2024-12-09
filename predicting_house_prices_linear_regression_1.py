import pyodbc
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# --- Database Connection ---
server = 'DESKTOP-M079PML\SQLEXPRESS01'
database = 'House_DB'
username = 'sardar'
password = '12345'
 
# Connection string for SQL Server Authenication
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"

def fetch_house_data(conn):
    cursor = conn.cursor()
    query = "SELECT bedrooms, bathrooms, square_footage, lot_size, year_built, price FROM dbo.house_data;"
    cursor.execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame.from_records(rows, columns=['bedrooms', 'bathrooms', 'square_footage', 'lot_size', 'year_built', 'price'])
    cursor.close()
    return df

# --- Linear Regression with Prediction ---
try:
    conn = pyodbc.connect(connection_string)
    house_data = fetch_house_data(conn)

    # --- Data preprocessing ---
    X = house_data.drop('price', axis=1)
    y = house_data['price']

    # One-hot encode categorical features if needed ( if you have categorical features )
    # Example: if you have a 'location' column
    # X = pd.get_dummies(X, columns=['location'], drop_first=True)

    # Handle missing values (if any)
    X.fillna(X.mean(numeric_only=True), inplace=True)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # --- Make predictions ---
    # Example: predict the price for a new house
    new_house = pd.DataFrame({'bedrooms':[3], 'bathrooms':[2], 'square_footage':[1800], 'lot_size':[0.25], 'year_built':[2015]})
    predicted_price = model.predict(new_house)
    print(f"Predicted price for the new house: ${predicted_price[0] :.2f}")

    # Evaluate the model ( on the test set )
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")

except pyodbc.Error as ex:
    print(f"Database error: {ex}")
except Exception as e:
    print(f"An error occured: {e}")
finally:
    if conn:
        conn.close() 