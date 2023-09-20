#   Importing Packages
import polars as pl
import seaborn as sns
import matplotlib.pyplot as plt
import os
import datetime

def PolarsPlot(df):
    #   Getting the x-axis and y-axis for the plot
    slen = df.select(pl.col('sepal_length')).to_numpy().ravel()
    swid = df.select(pl.col('sepal_width')).to_numpy().ravel()
    #   Adding colours based on the Species column
    hue  = df.select(pl.col('species')).to_numpy().ravel()
    #   Plotting the Scatter chart
    ax = sns.scatterplot(x=slen, y=swid, hue=hue)
    ax.set(xlabel ="Sepal Length", ylabel = "Sepal Width", title ='Distribution of Sepal Length and Sepal Width across different Species \n Generated on - '
        + str(datetime.datetime.now()))
    #   Saving the chart as a png file in the resources folder
    if os.path.isfile("./Resources/Data_Plot.png"):
        os.remove("./Resources/Data_Plot.png")
    plt.savefig("./Resources/Data_Plot.png")
    
    print("Successfully saved the plot in Resources folder")



