import pandas as pd
import pathlib as Path

csv_path = ("C:\Users\jakel_lv9e09w\Bootcamp\3-2\stock_data.csv")

stock_dataframe = pd.read_csv(csv_path)  #this code still fails even if you have the csv file in the same directory as your program. wtf?????

stock_dataframe.head()
