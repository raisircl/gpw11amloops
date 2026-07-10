import pandas as pd
df=pd.read_csv('student_performance.csv')
print("First 5 Records:")
print(df.head())

print("Last 5 Records:")
print(df.tail())

print("Rows and Columns:")
print(df.shape)

print("Column Names:")
print(df.columns)

print("Dataset Information:")
print(df.info())

print("Basic Statistics:")
print(df.describe())
