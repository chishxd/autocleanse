import clarion
from autocleanse.cleaner import handle_missing_data
from autocleanse.profiler import profile_dataframe, get_true_numerical_data
from autocleanse.utils import load_csv
from autocleanse.visualizer import visualize
from autocleanse.transformer import transform_features

def main():
    df = load_csv("data/train.csv") #Change file name to your dataset, I have provided train.csv in data/
    # df = clarion.load_from_s3("admin", "password", "http://127.0.0.1:9000", "train.csv")
    if df is not None:
        true_cols = get_true_numerical_data(df)
        new_df = handle_missing_data(df)
        model = transform_features(new_df)
        # profile_dataframe(new_df)
        visualize(new_df)
        print(model)

        
    else:
        print("Could not load File properly")

#this part of the code let's us to check code in a seperate part when we are working in a modular ecosystem.
#When this code is imported into other program, the code won't directly run, but only desired functions will run.
if __name__ == "__main__":
        main()