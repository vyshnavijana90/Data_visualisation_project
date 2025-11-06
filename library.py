# 📊 Data Visualization using Matplotlib and Seaborn
# 👩‍💻 Created by: Sai Vyshnavi Jana

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# -----------------------------
# 1️⃣ Using Matplotlib
# -----------------------------

# Sample data for Matplotlib
subjects = ['Python', 'Java', 'C++', 'JavaScript']
students = [45, 30, 25, 40]

plt.figure(figsize=(8,5))
plt.bar(subjects, students, color=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Number of Students Enrolled per Subject', fontsize=14)
plt.xlabel('Subjects')
plt.ylabel('Number of Students')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# -----------------------------
# 2️⃣ Using Seaborn
# -----------------------------

# Sample data for Seaborn
data = {
    'Department': ['CSE', 'ECE', 'EEE', 'MECH', 'CIVIL'],
    'Students': [60, 45, 40, 35, 30]
}
df = pd.DataFrame(data)

sns.set(style="whitegrid", palette="coolwarm")

plt.figure(figsize=(8,5))
sns.barplot(x='Department', y='Students', data=df)
plt.title('Number of Students in Each Department', fontsize=14)
plt.xlabel('Department')
plt.ylabel('Number of Students')
plt.show()

# -----------------------------
# 3️⃣ Bonus: Seaborn Scatterplot (Offline Safe)
# -----------------------------

# Custom sample data
scatter_data = {
    'Total_Bill': [20, 34, 45, 15, 28, 52, 38, 47, 31, 26],
    'Tip': [3, 5, 7, 2, 4, 8, 5, 7, 4, 3],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female']
}

df_scatter = pd.DataFrame(scatter_data)

plt.figure(figsize=(8,5))
sns.scatterplot(x='Total_Bill', y='Tip', hue='Gender', data=df_scatter, palette='rainbow', s=100)
plt.title('Tips vs Total Bill (Custom Scatter Plot)', fontsize=14)
plt.xlabel('Total Bill Amount')
plt.ylabel('Tip Amount')
plt.show()

print("✅ Visualization completed successfully by Sai Vyshnavi Jana!")