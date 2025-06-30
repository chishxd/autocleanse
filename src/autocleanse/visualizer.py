import os
from autocleanse.profiler import get_true_numerical_data
import matplotlib.pyplot as plt
import pandas as pd
import seaborn


def visualize(df: pd.DataFrame):
    #Listing Only important columns from the Data. This Function omits Columns which are supposed to be identifiers or Indices
    true_numerics = get_true_numerical_data(df)
    print(true_numerics)


    os.makedirs("../results", exist_ok=True) #Make a Directory to store all Histogram images

    #Loop through each column in Dataframe
    for col in true_numerics:
        #Create a New Canvas for plot
        plt.figure(figsize=(10, 6))
        #Plot the data
        seaborn.histplot(data= df[col].dropna(), kde=True, bins=30)
        #Give Title to chart, Labels to X and Y axes
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        #Build a filepath for each plots image
        output_path = f"../results/{col}_histogram.png"
        #Save the image
        plt.savefig(output_path)
        #Close the plot(optional, but nice practice)
        plt.close()
        print(f"Saved {col}_historgram.png")
    print("Operation Completed Successfully")