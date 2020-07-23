import pandas as pd
import os


all_df_list = []
cwd = os.path.abspath('')
files = os.listdir(cwd)

for file in files:
    if file.endswith ('.xlsx'):
        all_df_list.append(pd.read_excel(file))



# Merge all the dataframes in all_df_list
# Pandas will automatically append based on similar column names
appended_df = pd.concat(all_df_list)
appended_df.insert(0, "Ticker", file, True)

# Write the appended dataframe to an excel file
# Add index=False parameter to not include row numbers
appended_df.to_excel("Sorted_Stocks.xlsx", index=False)