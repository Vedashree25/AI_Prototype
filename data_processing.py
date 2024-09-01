import pandas as pd

def process_file(file_path: str) -> pd.DataFrame:
    # Use raw strings to handle backslashes correctly
    if file_path.endswith(r'C:\Desktop\AI_Prototype\Iris.csv'):
        df = pd.read_csv(file_path)
      
    elif file_path.endswith(r'C:\Desktop\AI_Prototype\global.json'):
        df = pd.read_json(file_path)
        
    elif file_path.endswith(r'C:\Desktop\AI_Prototype\Sample - Superstore.xls'):
        df = pd.read_excel(file_path)
    
    else:
        raise ValueError("Unsupported file format")
    
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Example cleaning: fill missing values
    df = df.ffill()
    return df

# Example usage
file_path = r'C:\Desktop\AI_Prototype\Iris.csv'
df = process_file(file_path)
cleaned_df = clean_data(df)
print(cleaned_df.head())
