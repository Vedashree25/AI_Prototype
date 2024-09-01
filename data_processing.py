import pandas as pd
import os

def process_file(file_path: str) -> pd.DataFrame:
    # Normalize the path to avoid issues with backslashes
    file_path = os.path.normpath(file_path)
    file_path = os.path.join('C:', 'Desktop', 'AI_Prototype', 'Global_Superstore2.csv')
    print(repr(file_path))  # Shows the raw string

    
    if file_path.endswith("C:\Desktop\AI_Prototype\Global_Superstore2.csv"):
        df = pd.read_csv(file_path)
      
    elif file_path.endswith("C:\Desktop\AI_Prototype\iris.json"):
        df = pd.read_json(file_path)
        
    elif file_path.endswith("C:\Desktop\AI_Prototype\marketingexcel.xlsx"):
        df = pd.read_excel(file_path)
    
    else:
        raise ValueError("Unsupported file format")
    
    return df

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def clean_and_preprocess_data(data: pd.DataFrame):
    imputer = SimpleImputer(strategy='mean')
    data_imputed = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
    
    scaler = StandardScaler()
    data_scaled = pd.DataFrame(scaler.fit_transform(data_imputed), columns=data.columns)
    
    return data_scaled
    
if __name__ == "__main__":
file_path = 'C:\Desktop\AI_Prototype\Global_Superstore2.csv'  
data = load_data(file_path)
cleaned_data = clean_and_preprocess_data(data)

print(cleaned_data.head())








