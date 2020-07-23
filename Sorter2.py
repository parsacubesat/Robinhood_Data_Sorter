import pandas as pd
import os



all_df_list = []
cwd = os.path.abspath('')
files = os.listdir(cwd)

for file in files:
    if file.endswith ('.csv'):
        all_df_list.append(pd.read_csv(file))


appended_df = pd.concat(all_df_list)

appended_df.to_excel("Sorted_Stocks.xlsx", index=False)
