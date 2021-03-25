import pandas as pd
from pathlib import Path 
from datetime import datetime, date, timedelta

# Read in CSV file and create a dataframe object

csvpath = Path("C:/Users/jakel_lv9e09w/Desktop/uw-fintech-spring-21/Activities/03-Python-Pandas/3-Monday-3_1_21/09-Stu_Multi_Indexing/Resources/goog_google_finance.csv")
goog_df = pd.read_csv(csvpath, parse_dates=True, index_col="Date", infer_datetime_format=True)
goog_df.head() 

print("The google dataframe we imported.")
print(goog_df)

# Clean up the dataframe

goog_df.isnull().mean() * 100

goog_df = goog_df.dropna()

goog_df = goog_df.drop_duplicates()

print("Do we have any nulls in the dataframe now?")

print(goog_df.isnull().sum())


# Grouping the dataframe by two indexes year and month

goog_df = goog_df.groupby([goog_df.index.year, goog_df.index.month])

print("Our dataframw is now grouped by year and month.")
print(goog_df)

# Slice data for closing price based on May 2019 data

goog_slice = goog_df.iloc[2019, 5]
print(goog_slice)