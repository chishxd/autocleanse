import clarion
from src.autocleanse.cleaner import handle_missing_data
from src.autocleanse.profiler import profile_dataframe, get_true_numerical_data
from src.autocleanse.utils import load_csv

def main():
    df = load_csv("data/Synthetic_data.csv") #Change file name to your dataset, I have provided train.csv in data/
    # df = clarion.load_from_s3("admin", "password", "http://127.0.0.1:9000", "train.csv")
    if df is not None:
        true_cols = get_true_numerical_data(df)
        print(true_cols)
        # profile_dataframe(df)
        # new_df = handle_missing_data(df)
        # profile_dataframe(new_df)
    else:
        print("Could not load File properly")

#this part of the code let's us to check code in a seperate part when we are working in a modular ecosystem.
#When this code is imported into other program, the code won't directly run, but only desired functions will run.
if __name__ == "__main__":
        main()