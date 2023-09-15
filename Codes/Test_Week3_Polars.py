#  IDS 706 Week 3 assignment - testing our template using Polars
 
import polars as pl
from Polars_Description import PolarsDesc
from Polars_Plot import PolarsPlot


def test_Polars():
    #   Reading Source Data from the Github Link
    DataSource_Link = "https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/Iris_Data.csv"
    df_s = pl.read_csv(DataSource_Link)

    # Writing the summary statistics to a file Summary.md in output folder
    with open("./Resources/Summary.md", "w", encoding="utf-8") as f:
        f.write(str(PolarsDesc(df_s)))
        print("Successfuessfully written the Summary.md file in the Resources folder")

    # Pasting the sample graph in the output folder
    PolarsPlot(df_s)

    #   Reading the Reference Data from the Resources Folder
    DataReference_Link = "./Resources/Iris_Data.csv"
    df_r = pl.read_csv(DataReference_Link)

    assert(PolarsDesc(df_r).frame_equal(df_s.describe()))


test_Polars()
