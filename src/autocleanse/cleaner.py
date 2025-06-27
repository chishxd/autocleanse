import pandas as pd

df = pd.read_csv("/home/chish/Projects/autocleanse/data/train.csv")

def handle_missing_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handles missing data by imputing or dropping columns.

    Drops:
        - Columns with more than 60% missing values.
        - Columns with ≥95% unique values (likely ID columns).

    Imputes:
        - Low-cardinality categorical: mode
        - Numeric: median
        - Other: 'Unknown'

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame with potential missing values.

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame.
    """
    print("Started Cleaning the Data...")

    drop_cols = []

    # Detect numeric columns
    numerical_cols = df.select_dtypes(include='number')

    # Drop ID-like columns: high cardinality numeric features
    id_like_cols = [
        col for col in numerical_cols.columns
        if df[col].nunique() >= 0.95 * len(df)
    ]
    drop_cols.extend(id_like_cols)

    for column in df.columns:
        missing_ratio = df[column].isnull().sum() / len(df)

        if missing_ratio > 0.6:
            drop_cols.append(column)
        else:
            unique_ratio = df[column].nunique() / len(df)

            if unique_ratio < 0.05:
                df[column] = df[column].fillna(df[column].mode().iloc[0])
            elif pd.api.types.is_numeric_dtype(df[column]):
                df[column] = df[column].fillna(df[column].median())
            else:
                df[column] = df[column].fillna("Unknown")

    df = df.drop(columns=list(set(drop_cols)))

    print("Finished Cleaning the Data!")
    return df



new_df = handle_missing_data(df)
print(new_df.head)