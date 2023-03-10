import pandas as pd

# read the excel file into a pandas dataframe
df = pd.read_excel('cardio_train.csv')

# remove duplicates
df.drop_duplicates(inplace=True)

# remove empty rows and columns
df.dropna(how='all', inplace=True)
df.dropna(axis=1, how='all', inplace=True)

# convert string columns to lowercase
df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)

# remove leading/trailing spaces from string columns
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# replace any NaN values with a default value (e.g. "N/A")
df.fillna("N/A", inplace=True)

# write the cleaned data to a new excel file
df.to_excel('cleaned_data.xlsx', index=False)
