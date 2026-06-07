import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("student_data.csv")

# Display dataset
print("Student Dataset")
print(data)

# Calculate average marks
avg_marks = data["Marks"].mean()
print("\nAverage Marks:", round(avg_marks, 2))

# Calculate average study hours
avg_hours = data["Study_Hours"].mean()
print("Average Study Hours:", round(avg_hours, 2))

# Identify top-performing student
highest_marks = data["Marks"].max()
top_student = data[data["Marks"] == highest_marks]

print("\nTop Performing Student")
print(top_student)

# Analyze correlation between study hours and marks
corr = data["Study_Hours"].corr(data["Marks"])
print("\nCorrelation between Study Hours and Marks:", round(corr, 2))

# Visualize data
plt.scatter(data["Study_Hours"], data["Marks"])

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.grid(True)

plt.show()