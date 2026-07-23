import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

#print(df.head())
#print(df.info())
sns.set_theme(style="darkgrid")

# Other useful styles:
# darkgrid
# whitegrid
# dark
# white
# ticks
plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="Course",
    hue="Result",
    palette="Set2"
)

plt.title("Pass vs Fail Count")
plt.xlabel("Course")
plt.ylabel("Number of Students")
plt.show()

plt.savefig("pass_fail_count.png", dpi=300)
