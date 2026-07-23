import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
print("Current working directory:", os.getcwd())

os.chdir("student_eda_project")  # Change to the parent directory
print("Current working directory:", os.getcwd())

sns.set_theme(style="whitegrid")

print("Libraries imported successfully")
df = pd.read_csv("dataset/student_performance.csv")


print(df.head())
print(df.shape)
