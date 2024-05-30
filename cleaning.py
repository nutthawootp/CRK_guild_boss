# -*- coding: utf-8 -*-

# """
# This script provides a collection of functions to clean and style dataframes. It includes functions for renaming columns, correcting data types, estimating trophies, removing unnecessary rows, 
# and adding rank change information. The main function `clean_data` applies these functions to a dataframe. Additionally, it includes functions for styling dataframes, renaming guild names, 
# and adding extra guild information. The script can be run as a standalone module to clean a specific file, `MolochTHbackup.xlsx`.
# """

# %% [markdown]
# # Environment preparation
#

# %% [markdown]
# ## import library
#

# %%
import pandas as pd
# Ignore warning
import warnings
warnings.filterwarnings('ignore')
from Preprocessing import *

# %% [markdown]
# ## Load data from rank table in Excel file
#

# %%
file_path = r"data\MolochTHbackup.xlsx"
print(f"\nLoading data from Excel file. {file_path!r}")
df_raw = pd.read_excel(file_path, sheet_name=6, header=1, usecols=range(1, 8))
# df_raw

# %%
# df_raw.info()

# %% [markdown]
# ## Clean data

# %%
def print_processing_status(iteration, total):
    """
    Print the processing status in the console.
    """
    # Calculate the percentage of progress
    percentage = (iteration / float(total)) * 100
    # Print the processing status
    print(f"Processing... {percentage:.2f}%", end="\r")


def clean_data_and_print_status(dataframe, num_rows):
    """
    Clean the dataframe and print the processing status.
    """
    data = clean_data(dataframe)
    
    print("Processing... ", end="\n\n")
    
    for i, row in enumerate(dataframe.itertuples(index=False)):
        print_processing_status(i, num_rows)
        
    save_path = r"data\CRK_guild_boss.csv"
    data.to_csv(save_path, index=False)
    print(f"Processed datasets were saved to {save_path!r}\n")

    save_path = r"data\CRK_guild_boss.pkl"
    # print(f"Pre-processed datasets were saved to {save_path!r}\n")
    data.to_pickle(save_path)
    
    print("Completed...!!", end="\n\n")
    return data



if __name__ == "__main__":
    print()
    data = clean_data_and_print_status(df_raw, len(df_raw))

# %% [markdown]
# # Save processed data in .csv format
#

# # %%
# print(f"{data.shape=}")
# print(data.info())
# %%
