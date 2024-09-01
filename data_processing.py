import pandas as pd
import os

def process_file(file_path: str) -> pd.DataFrame:
    # Normalize the path to avoid issues with backslashes
    file_path = os.path.normpath(file_path)
    file_path = os.path.join('C:', 'Desktop', 'AI_Prototype', 'Iris.csv')
    print(repr(file_path))  # Shows the raw string

    
    if file_path.endswith('Iris.csv'):
        df = pd.read_csv(file_path)
      
    elif file_path.endswith('global.json'):
        df = pd.read_json(file_path)
        
    elif file_path.endswith('Sample - Superstore.xlsx'):
        df = pd.read_excel(file_path)
    
    else:
        raise ValueError("Unsupported file format")
    
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Forward fill missing values
    df = df.ffill()
    return df

# Example usage
if __name__ == "__main__":
    # Use raw string to avoid escape sequence issues
    file_path = r'C:\Desktop\AI_Prototype\Iris.csv'
    df = process_file(file_path)
    cleaned_df = clean_data(df)
    print(cleaned_df.head())



