import pandas as pd
df = pd.read_csv("students_performance_dirty_data.csv")
#print(df.head())

# print("Rows and Columns:")
# print(df.shape)

# print("Column Names:")
# print(df.columns)

# print("Dataset Info:")
# print(df.info())

# print("Missing Values:")
# print(df.isnull().sum())

# print("Total Missing Values:")
# print(df.isnull().sum().sum())

# show all the rows with missing values
#missing_values_rows = df[df.isnull().any(axis=1)]
#print("Rows with Missing Values:")
#print(missing_values_rows)
# print(df["Attendance"])

# att_avg=df["Attendance"].mean()
# df["Attendance"]=df["Attendance"].fillna(att_avg)

# print(df["Attendance"])

# print(df["FinalMarks"])

# df["FinalMarks"]=df["FinalMarks"].fillna(df["FinalMarks"].mean())
# print(df)

#clean_df=df.dropna()
#print(df)
#print(clean_df)

# Count duplicate rows
print(df.duplicated().sum())

# Show duplicate rows
duplicates = df[df.duplicated()]

print(duplicates)

without_duplicates = df.drop_duplicates()
print(df)
print(without_duplicates)
