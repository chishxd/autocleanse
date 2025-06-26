import pandas as pd

def load_csv(data : str) -> pd.DataFrame:
    """Loads a CSV file into a Pandas DataFrame.

    Parameters
    ----------
    data : str
        The file path to the CSV file.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the loaded data. Returns None if the file
        is not found.

    Raises
    ------
    FileNotFoundError
        If the file path does not exist.
    """
    try:
        df = pd.read_csv(data) #read_csv() method is used to load and read the contents in a CSV file
        return df
    except FileNotFoundError: #We handle the FileNotFoundError so that the program won't crash.
        print("File Not Found!")
        return None
    