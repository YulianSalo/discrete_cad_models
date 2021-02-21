import pandas as pd
import sys

data_file = input("Select your data file: ")
df = pd.read_csv(data_file)
print(df)