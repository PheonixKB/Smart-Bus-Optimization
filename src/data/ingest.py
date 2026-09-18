"""
Data ingestion and cleaning module for Smart Bus Optimization.
"""

import pandas as pd
import os

def ingest_raw_data(raw_data_path: str = "data/raw", cleaned_data_path: str = "data/cleaned"):
    """
    Ingest raw CSV files, perform basic cleaning, and save to cleaned directory.
    
    Args:
        raw_data_path (str): Path to the directory containing raw CSV files.
        cleaned_data_path (str): Path to the directory where cleaned CSV files will be saved.
    """
    # Ensure the cleaned data directory exists
    os.makedirs(cleaned_data_path, exist_ok=True)
    
    # List of expected raw files
    raw_files = [
        "bmtc_route_stop_sequence.csv",
        "bmtc_routes_clean.csv",
        "bmtc_stops_clean.csv"
    ]
    
    for file_name in raw_files:
        raw_file_path = os.path.join(raw_data_path, file_name)
        cleaned_file_path = os.path.join(cleaned_data_path, file_name)
        
        # Check if the raw file exists
        if not os.path.exists(raw_file_path):
            print(f"Warning: Raw file {raw_file_path} not found. Skipping.")
            continue
        
        # Read the CSV file
        df = pd.read_csv(raw_file_path)
        
        # Basic cleaning steps
        # 1. Drop rows that are completely empty
        df.dropna(how='all', inplace=True)
        
        # 2. Strip whitespace from string columns
        for col in df.select_dtypes(include=['object']):
            df[col] = df[col].str.strip()
        
        # 3. Reset index
        df.reset_index(drop=True, inplace=True)
        
        # Save the cleaned data
        df.to_csv(cleaned_file_path, index=False)
        print(f"Cleaned {file_name} and saved to {cleaned_file_path}")

if __name__ == "__main__":
    ingest_raw_data()