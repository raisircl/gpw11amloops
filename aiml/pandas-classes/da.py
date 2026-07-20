import pandas as pd

df=pd.read_csv('student_performance.csv')

print(df.head())
print(f"Number of students {len(df)}")

print("Rows and Columns:")
print(df.shape)

print("Average Marks:")
print(df["FinalMarks"].mean())

print("Average Attendance:")
print(df["Attendance"].mean())


print("Count pass and fail students")
print(df["Result"].value_counts())

print("Count male and female students")
print(df["Gender"].value_counts())

print("Count students by course")
print(df["Course"].value_counts())


print("Percentage of Pass and Fail students")
result_percent = df["Result"].value_counts(
    normalize=True
) * 100

print(result_percent)

print("Average marks by course")
course_avg = df.groupby("Course")["FinalMarks"].mean()

print(course_avg)


print("Course-wise summary report")
course_summary = df.groupby("Course")["FinalMarks"].agg([
    "count",
    "mean",
    "max",
    "min"
])

print(course_summary)


print("Analyze marks and attendance together")
summary = df.groupby("Course").agg({
    "FinalMarks": ["mean", "max", "min"],
    "Attendance": ["mean", "min"],
    "StudentID": "count"
})

print(summary)


print("Course and Result wise count")
course_result = df.groupby([
    "Course",
    "Result"
])["StudentID"].count()

print(course_result)


print("Convert groupby result into normal table")
course_result = df.groupby([
    "Course",
    "Result"
])["StudentID"].count().reset_index()

print(course_result)


print("Pivot table: Course vs Result")
pivot = pd.pivot_table(
    df,
    values="StudentID",
    index="Course",
    columns="Result",
    aggfunc="count",
    fill_value=0
)

print(pivot)


print("Course with highest average marks")
course_avg = df.groupby("Course")["FinalMarks"].mean()

top_course = course_avg.idxmax()
top_average = course_avg.max()

print("Top Course:", top_course)
print("Average Marks:", top_average)


print("Create pass percentage by course")
pass_data = df[df["Result"] == "Pass"]

total_by_course = df.groupby("Course")["StudentID"].count()
pass_by_course = pass_data.groupby("Course")["StudentID"].count()

pass_percent = (pass_by_course / total_by_course) * 100

print(pass_percent)
