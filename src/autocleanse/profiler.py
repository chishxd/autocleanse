import pandas as pd

def profile_dataframe(df: pd.DataFrame):
    """
    Profiles the input DataFrame and returns key data statistics.

    This includes:
        - Column names and their data types
        - Percentage of missing values in each column
        - Descriptive statistics for numerical columns
        - Count of categorical columns

    Args:
        df (pd.DataFrame): The input Pandas DataFrame.

    Returns:
        STDOUT (str): Output is shown to terminal.

    Raises:
        Nothing
    """

    print("--- Profiling Data ---")
    print("First 5 rows in the DataFrame: ")
    print(df.head())
    print(f"Shape of Dataframe(rows, columns):{df.shape}\n") #Prints rows and columns in a Dataframe
    print("Name Of Each Column:")
    for column in df.columns: #Uses For loop to go through each column in the:Python Index of all columns in the dataframe and print them
        print(column)
    print()

    print("Data Type of Each Column:")
    print(df.dtypes) #dtypes() returns datatype of each column in the dataframe.
    print()

    print("Percentage of missing Values:")
    null_percentages = (df.isnull().sum() / len(df)) * 100
    #.isnull() returns bool values if a value is null or not and .sum() sums up all True values. Then a percentage of the null values in each column is calculated.
    print(f"{null_percentages.round(2)}")
    print()

    print("Description of Numerical Columns: ")
    #.describe() function calculates Count, Mean, standard derivation, quartiles, min and max values of each column
    #Basically It is a summary of all the important data needed about the data.
    print(df.describe())
    print()

    print("Count of Unique Values in Categorical Columns: ")
    #Categorical Column means the columns which have limited values, like Male and Female are the only two values in Sex Column of the Dataframe, hence it is a Categorical Column.

    #.nunique() is used to calculate total number of unique values in a column, which has less than 5% of unique value.
    for column in df.columns:
        if df[column].nunique()/len(df) * 100 < 5 :
            print(f"{column} : {df[column].nunique()}") 
    print()
    print("--- End Of Profiling ---")