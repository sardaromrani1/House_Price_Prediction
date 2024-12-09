import csv
import random

# Define the number of rows to generate
num_rows = 1000

# Define column names (matching your table structure)
column_names = ['house_id', 'bedrooms', 'bathrooms', 'square_footage', 'lot_size', 'location', 'year_built', 'price']

# Function to generate random data for each column
def generate_house_data():
    house_id = None # house_id is auto-incrementing so it's not generated here.
    bedrooms = random.randint(1, 6)
    bathrooms = random.randint(1, 4)
    square_footage = random.randint(500, 4000)
    lot_size = round(random.uniform(0.1, 1.0), 2)   # Lot size between 0.1 and 1.0 acres
    location = random.choice(['Springfield', 'Shelbyville', 'Capital City'])    # Example locations
    year_built = random.randint(1950, 2023)
    price = round(random.uniform(100000, 1000000), 2)   # Price between $100,000 and $1,000,000

    return [house_id, bedrooms, bathrooms, square_footage, lot_size, location, year_built, price]


# Generate the CSV data
try:

    with open('house_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(column_names)   # Write header row
        for _ in range(num_rows):
            house_data = generate_house_data()
            writer.writerow(house_data)

    print(f"Generated 'house_data.csv' with {num_rows} rows.")
except Exception as e:
    print(f"An error occurred: {e}")