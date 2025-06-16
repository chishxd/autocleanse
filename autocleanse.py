import pandas as pd

def load_csv(data : str) -> pd.DataFrame:
    '''
    This funtion is going to be used to load any CSV file
    Args: 
        data : A string of file location to your CSV file.
    Returns:
        pd.DataFrame : A Dataframe created after oarsing CSV file
    Raises:
        FileNotFoundError : When file location is incorrrect or if file does not exist.
    '''
    try:
        df = pd.read_csv(data) #read_csv() method is used to load and read the contents in a CSV file
        return df
    except FileNotFoundError: #We handle the FileNotFoundError so that the program won't crash.
        print("File Not Found!")
        return None


def profile_data(df : pd.DataFrame) -> None:
    '''
    Profiles the data and returns Name of each column, data type of each column, Percentage of missing values, Statistical description of Numerical Columns, Count of Categorical columns

    Args:
        df(pd.DataFrame) : The Panda Dataframes.

    Returns:
        Output With all the data [TODO: A CSV/JSON file with all the data for API working]
    
    Raises:
        Nothing
    '''
    print("--Profiling Data--")

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

#this part of the code let's us to check code in a seperate part when we are working in a modular ecosystem.
#When this code is imported into other program, the code won't directly run, but only desired functions will run.
if __name__ == "__main__":
        df = load_csv("data/train.csv")
        if df is not None:
            profile_data(df)
        else:
            print("Could not load File properly")