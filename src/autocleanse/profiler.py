import pandas as pd

def profile_dataframe(df: pd.DataFrame) -> None:
    """Generate and print a profile report of a pandas DataFrame.

        The report provides a summary of key data characteristics, including column
        names and their data types, the percentage of missing values, descriptive
        statistics for numerical columns, and a count of unique values for
        categorical columns.

        Parameters
        ----------
        df : pd.DataFrame
            The DataFrame to be profiled.

        Returns
        -------
        None
            This function prints its output to stdout and does not return anything.

        Raises
        ------
        TypeError
            If the input `df` is not a pandas DataFrame.
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


#-----------------------------------------------------------------------------------------------------------------------#

def get_true_numerical_data(df: pd.DataFrame, id_threshold: float = 0.95) -> list[str]:
    """
    Lists all the important numerical columns by omitting Unique Key values
    TODO: Add context-based listing

    Parameters
    ----------
        df : pd.DataFrame
            A Panda Dataframe

    Returns
    -------
        true_numerical.columns : list[str]
             List of all Important Numerical Columns
    """
    numerical_cols = df.select_dtypes(include='number')
    cols_to_exclude = [
        col for col in numerical_cols.columns
        if numerical_cols[col].nunique() / len(df) > id_threshold
    ]

    true_numericals = numerical_cols.drop(columns=cols_to_exclude)

    return list(true_numericals.columns)
