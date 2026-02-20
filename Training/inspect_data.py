import pandas as pd
import os

files = [
    r"data\flood dataset.xlsx",
    r"..\archive (1)\rainfall in india 1901-2015.xlsx"
]

for file_path in files:
    print(f"--- Inspecting {os.path.basename(file_path)} ---")
    try:
        df = pd.read_excel(file_path)
        print(df.head())
        print("\nInfo:")
        print(df.info())
        print("\n")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
