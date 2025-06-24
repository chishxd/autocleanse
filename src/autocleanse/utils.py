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
    