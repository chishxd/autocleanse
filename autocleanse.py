import pandas as pd

def load_csv(data : str) -> pd.DataFrame:
    """
    Loads a CSV file into a Pandas DataFrame.

    Args:
        data (str): File path to the CSV file.

    Returns:
        df (pd.DataFrame): DataFrame parsed from the CSV file.

    Raises:
        FileNotFoundError: If the file path is incorrect or the file does not exist.
    """
    try:
        df = pd.read_csv(data) #read_csv() method is used to load and read the contents in a CSV file
        return df
    except FileNotFoundError: #We handle the FileNotFoundError so that the program won't crash.
        print("File Not Found!")
        return None


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
    for column in df.columns: #Uses For loop to go through each column in the Index of all columns in the dataframe and print them
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

#This is our work of Day 2, We are cleaning DataFrame so that we can train the data without any errors.
def handle_missing_data(df : pd.DataFrame) -> pd.DataFrame:
    '''
    Function to clean the provided data by:
    - Dropping Columns with too many Null values
    - Imputing data in barely any empty values

    Args:
        df (pd.DataFrame): A Panda Dataframe

    Returns:
        df (pd.DataFrame): The cleaned DataFrame with missing values handled and specified columns dropped.
    '''
    nullCols = [] #To store Columns with more than 60% Null Values.
    for column in df.columns:
        if df[column].isnull().sum() / len(df) * 100 > 60.00 : #Same comparision from the profiling_dataframe()
            nullCols.append(column)

        else:
            #Check if the percentage of unique values in the DataFrame is less than 5%, if yes fill the categorical values from modes
            if df[column].nunique()/len(df) * 100 < 5 :
                df[column] = df[column].fillna(df[column].mode().iloc[0]) #use mode when imputing non-numerical and categorical data
            else:
                #Check if the column is numeric, if yes we can use Median to fill null values.
                if pd.api.types.is_numeric_dtype(df[column]):
                    df[column] = df[column].fillna(df[column].median()) #use median when imputing numerical data
                else:
                    df[column] = df[column].fillna('Unknown')
    
    df = df.drop(columns=nullCols) #To delete the columns from listed earlier in the funtion.
    
    return df


#this part of the code let's us to check code in a seperate part when we are working in a modular ecosystem.
#When this code is imported into other program, the code won't directly run, but only desired functions will run.
if __name__ == "__main__":
        df = load_csv("data/train.csv")
        if df is not None:
            profile_dataframe(df)
            new_df = handle_missing_data(df)
            profile_dataframe(new_df)
        else:
            print("Could not load File properly")