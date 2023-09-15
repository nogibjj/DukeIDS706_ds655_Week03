#   Importing Packages
import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt

def PolarsPlot(df):
    #   Getting the x-axis and y-axis for the plot
    slen = df.select(pl.col('sepal_length')).to_numpy().ravel()
    swid = df.select(pl.col('sepal_width')).to_numpy().ravel()
    #   Adding colours based on the Species column
    hue  = df.select(pl.col('species')).to_numpy().ravel()
    #   Plotting the Scatter chart
    ax = sns.scatterplot(x=slen, y=swid, hue=hue)
    #   Saving the chart as a png file in the resources folder
    plt.savefig("./Resources/Data_Plot.png")
    print("Successfully saved the plot in Resources folder")



