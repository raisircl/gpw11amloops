import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('student_performance.csv')
print(df.head())

plt.figure(figsize=(8,5))
plt.plot(df['StudentName'],df['FinalMarks'], marker='o', color='b')
plt.xlabel('Student')
plt.ylabel('Marks')
plt.title('Student Final Marks')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
