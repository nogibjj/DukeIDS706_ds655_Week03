#  IDS 706 Week 2 assignment - Creating a function to show descriptive statistics for a dataframe
# Convert this pandas code to corresponding polars code

import polars as pl

def PolarsDesc(df):
  return df.describe()

def PandasDesc(df):
  return df.describe()

