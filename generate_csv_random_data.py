import pandas as pd
import random

# Create a list of data
data = []
for i in range(50):
    name = random.choice(["Apple", "Banana", "Chocolate Bar", "Candy", "Chips", "Yogurt", "Milk"])  
    barcode = random.randint(10000, 99999)  
    calories = random.randint(50, 500)
    fat = random.uniform(0, 30) 
    sugar = random.randint(0, 60)
    classification = random.choice(["Healthy", "Unhealthy"]) 
    data.append([name, barcode, calories, fat, sugar, classification])

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=["name", "barcode", "calories", "fat", "sugar", "classification"])

# Save the DataFrame to a CSV file
df.to_csv("food_data.csv", index=False) 

# run python generate_csv_random_data.py ####### for generate csv file
