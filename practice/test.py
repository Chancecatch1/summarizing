import pandas as pd

# Set the file path to the xlsx file
file_path = 'Youjin.xlsx'

# Read the xlsx file and create a DataFrame object
df = pd.read_excel(file_path)

# Set the index to the first column
df = df.set_index(df.columns[0])

# Convert the DataFrame to a dictionary
data_dict = df.to_dict()

# Print the dictionary
print(data_dict)

for key in data_dict:
    print(key)


df_2 = data_dict['Unnamed: 1']

for key_2 in df_2:
    print(key_2)