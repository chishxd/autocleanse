import pandas as pd
from autocleanse.profiler import get_true_numerical_data

def test_get_true_numerical_columns_identifies_and_excludes_ids():
    """
    Verifies that the function returns only true numerical columns,
    excluding non-numeric and high-cardinality ID-like columns.
    """
    # ARRANGE
    test_data = {
        'ID': [101, 102, 103, 104, 105, 106],             # Should be excluded (unique values)
        'Age': [25, 30, 35, 40, 35, 40],                # Should be included
        'Category': ['A', 'B', 'A', 'C', 'B','A'],       # Should be excluded (non-numeric)
        'Status_Code': [200, 404, 200, 500, 501, 400]     # Should be included (numeric, reasonable cardinality)
    }
    df = pd.DataFrame(test_data)

    # ACT
    result = get_true_numerical_data(df)

    # ASSERT
    expected = ['Age', 'Status_Code']
    assert set(result) == set(expected)
    print(result)