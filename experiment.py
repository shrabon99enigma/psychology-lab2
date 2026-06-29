import pandas as pd
import random

# Sample Data
names = [
    "Rahim", "Karim", "Hasan", "Sakib", "Nafis",
    "Arafat", "Mim", "Nusrat", "Tania", "Jannat"
]

departments = [
    "CSE", "EEE", "Civil", "Mechanical", "BBA"
]

rows = []

for i in range(1, 101):
    rows.append({
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 30),
        "Department": random.choice(departments),
        "Semester": random.randint(1, 8),
        "CGPA": round(random.uniform(2.50, 4.00), 2),
        "Attendance (%)": random.randint(60, 100),
        "Tuition Fee": random.randint(30000, 80000),
        "Status": random.choice(["Paid", "Pending"]),
        "Email": f"student{i}@example.com"
    })

df = pd.DataFrame(rows)

# Save CSV
df.to_csv("students.csv", index=False)

print("students.csv created successfully!")