import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('student_performance.csv')
#print(df.head())

# Pie chart: Pass vs Fail
result_count = df["Result"].value_counts()
print(result_count.index)


plt.figure(figsize=(6, 6))

plt.pie(
    result_count,
    labels=result_count.index,
    autopct="%5.1f%%",
    startangle=90
)

plt.title("Pass vs Fail Percentage")
plt.show()
