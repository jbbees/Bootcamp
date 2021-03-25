# Pandas

Panel Data Structures

Spreadsheets in python


> import pandas as pd                        - brings in pandas library and stores in aliased variable named pd to reference the library

> from pathlib import Paths       


load an enite csv file into a dataframe.

## Dataframe

**this requires you have the file in the current directory** 

dataframe is the table itself.

csv_path = Path("file path")          - store the entire file path into 1 variable

amd_dataframe = pd.read_csv(csv_path) - pandas has built-in read_csv() function to read csv files. 
                                      - pass it the csv_path variable since it has our filepath stored in it.
                                      - this code will create a table/spreadsheet out of the csv file data.

amd_dataframe.head()                  - dataframe will by default display the first 5 rows.

amd_dataframe.head(10)                - dataframe will display the first 10 rows. this has to be last code to display your entire table. 


amd_dataframe.columns = ['column1', 'column2', 'column3', 'column4', column5']
amd_dataframe.head(10)                 - you have to put a .head() call at the very end of your dataframe code. 

list elements become the column names of the table created.

look-up last records in a table

amd_dataframe.tail(10)                  - you have to look up last 10 records in a dataframe table.

display rows of specific columns.

amd_dataframe[['Date', 'Close']].head(2)



