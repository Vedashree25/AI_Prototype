import pandas as pd

def load_data(file_path: str):
    file_path = r'C:\Desktop\AI_Prototype\Iris.csv'

    if file_path.endswith(r'C:\Desktop\AI_Prototype\Iris.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith(r'C:\Desktop\AI_Prototype\global.json'):
        return pd.read_json(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel('Sample - Superstore.xls')
    else:
        raise ValueError("Unsupported file format")

def clean_data(df: pd.DataFrame):
    # Example cleaning: fill missing values
    df = df.ffill()
    return df
