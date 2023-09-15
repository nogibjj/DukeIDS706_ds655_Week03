#   Importing Packages
import polars as pl
import seaborn as sns
import plotly.express as px

DataSource_Link = "https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/Iris_Data.csv"
df_s = pl.read_csv(DataSource_Link)
#Plot a scatterplot of sepal length vs sepal width



slen = df_s.select(pl.col('sepal_length')).to_numpy().ravel()
swid = df_s.select(pl.col('sepal_width')).to_numpy().ravel()
hue  = df_s.select(pl.col('species')).to_numpy().ravel()
sns.scatterplot(x=slen, y=swid, hue=hue, data = df_s)

sns.show()
