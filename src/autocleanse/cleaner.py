import pandas as pd

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
    print("Started Cleaning the Data...")
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

    print("Finished Cleaning the Data!")
    
    return df