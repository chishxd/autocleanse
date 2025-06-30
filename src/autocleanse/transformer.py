# src/autocleanse/transformer.py

import pandas as pd
from sklearn.preprocessing import StandardScaler

def transform_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Takes a cleaned DataFrame and performs all necessary feature engineering steps.

    Steps:
    1. Extracts titles from the 'Name' column.
    2. Drops irrelevant or redundant columns.
    3. Performs one-hot encoding on categorical features.
    4. Scales all numerical features.

    Returns:
        A fully transformed, model-ready DataFrame.
    """
    # Use .copy() to avoid changing the original DataFrame
    df_transformed = df.copy()

    # --- 1. Extract Titles from Name ---
    df_transformed['Title'] = df_transformed['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
    # Consolidate rare titles (a good practice to add)
    rare_titles = ['Dr', 'Rev', 'Col', 'Major', 'Sir', 'Lady', 'Don', 'Jonkheer']
    df_transformed['Title'] = df_transformed['Title'].replace(rare_titles, 'Rare')
    df_transformed['Title'] = df_transformed['Title'].replace(['Mlle', 'Ms'], 'Miss')
    df_transformed['Title'] = df_transformed['Title'].replace('Mme', 'Mrs')

    # --- 2. Drop Unnecessary Columns ---
    # We drop 'Name' and 'Ticket' because they are too unique and have been processed.
    # We drop 'Cabin' because it has too many missing values (from the cleaner phase).
    # We drop 'PassengerId' as it's an identifier.
    cols_to_drop = ['Name','Ticket', 'PassengerId', 'Cabin']
    existing_cols_to_drop = [col for col in cols_to_drop if col in df_transformed.columns]
    df_transformed = df_transformed.drop(columns=existing_cols_to_drop, axis=1)

    # --- 3. One-Hot Encode Categorical Features ---
    # Identify categorical columns to encode
    # 'Title' is now one of our categorical features
    categorical_cols = df_transformed.select_dtypes(include=['object', 'category']).columns
    df_transformed = pd.get_dummies(df_transformed, columns=categorical_cols, drop_first=True)

    # --- 4. Scale Numerical Features ---
    # Identify numerical columns to scale
    numerical_cols = df_transformed.select_dtypes(include=['int64', 'float64']).columns
    scaler = StandardScaler()
    df_transformed[numerical_cols] = scaler.fit_transform(df_transformed[numerical_cols])

    print("[INFO] Feature engineering complete.")
    return df_transformed