"""
Student Performance Analysis
Complete data analysis with visualizations
"""

import pandas as pd
import matplotlib.pyplot as plt

# =====================
# STEP 1: LOAD DATA
# =====================
df = pd.read_csv('data/student_performance.csv')
print("Data Loaded Successfully!")
print(df.head())

# =====================
# STEP 2: EXPLORE DATA
# =====================
print("\n--- DATASET INFO ---")
print(df.info())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())
df = df.dropna()

# =====================
# STEP 3: ANALYSIS
# =====================
print("\n--- BASIC STATISTICS ---")
print(f"Total Students: {len(df)}")
print(f"Average Math Score: {df['Math_Score'].mean():.2f}")
print(f"Average Science Score: {df['Science_Score'].mean():.2f}")
print(f"Average English Score: {df['English_Score'].mean():.2f}")
print(f"Average Attendance: {df['Attendance'].mean():.2f}%")
print(f"Top Student: {df.loc[df['Math_Score'].idxmax(), 'Student_Name']}")

# =====================
# STEP 4: VISUALIZATION
# =====================

# Chart 1 - Bar Chart: Average Score per Subject
subjects = ['Math_Score', 'Science_Score', 'English_Score']
averages = [df[s].mean() for s in subjects]

plt.figure(figsize=(8, 5))
plt.bar(['Math', 'Science', 'English'], averages, color=['blue', 'green', 'orange'])
plt.title('Average Score by Subject')
plt.ylabel('Average Score')
plt.xlabel('Subject')
plt.savefig('visualizations/bar_chart.png')
plt.close()
print("\nBar chart saved!")

# Chart 2 - Pie Chart: Grade Distribution
grade_counts = df['Grade'].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%')
plt.title('Grade Distribution')
plt.savefig('visualizations/pie_chart.png')
plt.close()
print("Pie chart saved!")

# =====================
# STEP 5: FINAL REPORT
# =====================
print("\n" + "="*45)
print("   STUDENT PERFORMANCE ANALYSIS REPORT")
print("="*45)
print(f"Total Students Analyzed : {len(df)}")
print(f"Avg Math Score          : {df['Math_Score'].mean():.2f}")
print(f"Avg Science Score       : {df['Science_Score'].mean():.2f}")
print(f"Avg English Score       : {df['English_Score'].mean():.2f}")
print(f"Avg Attendance          : {df['Attendance'].mean():.2f}%")
print(f"Top Student             : {df.loc[df['Math_Score'].idxmax(), 'Student_Name']}")
print("="*45)
print("Charts saved in visualizations/ folder")