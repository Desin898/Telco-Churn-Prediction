import pandas as pd
import os

# Define the file name
filename = 'WA_Fn-UseC_-Telco-Customer-Churn.csv'

# Check if file exists to avoid frustration
if os.path.exists(filename):
    # Load the data
    df = pd.read_csv(filename)

    # Success message
    print(f"SUCCESS! Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")
    print("\nHere are the first 5 rows:")
    print(df.head())
else:
    print(f"ERROR: Could not find {filename}. Did you paste it into the project folder?")