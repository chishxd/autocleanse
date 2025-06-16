import pandas as pd

def load_csv(data : str) -> pd.DataFrame:
    try:
        df = pd.read_csv(data)
        return df
    except FileNotFoundError:
        print("File Not Found!")
        return None

# [DONE]Shape: Total rows and columns.

# [DONE]Column Names: A list of all columns.

# [DONE]Data Types: The type of each column (e.g., int64, float64, object).

# [DONE]Missing Values: The count or percentage of null/NaN values for each column.

# [DONE] Descriptive Statistics: For numerical columns: count, mean, standard deviation, min, max, and quartiles.

# [DONE]Unique Values: For categorical columns: the count of unique values.

def profile_data(df : pd.DataFrame):
    print("--Profiling Data--")

    print(f"Shape of Dataframe:{df.shape}\n")
    print("Name Of Each Column:")
    for column in df.columns:
        print(column)
    print()

    print("Data Type of Each Column:")
    print(df.dtypes)
    print()

    print("Percentage of missing Values:")
    null_percentages = (df.isnull().sum() / len(df)) * 100
    print(f"{null_percentages.round(2)}")
    print()

    print("Description of Numerical Columns: ")
    print(df.describe())
    print()

    print("Count of Unique Values in Categorical Columns: ")
    for column in df.columns:
        if df[column].nunique()/len(df) * 100 < 5 :
            print(f"{column} : {df[column].nunique()}")
    print()

if __name__ == "__main__":
        df = load_csv("data/train.csv")
        if df is not None:
            profile_data(df)
        else:
            print("Could not load File properly")