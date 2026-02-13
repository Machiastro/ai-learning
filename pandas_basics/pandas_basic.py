import pandas as pd

#load dataset
df = pd.read_csv("students.csv")

print("=== Dataset ===")
print(df)

# info dataset
print("\n=== Info ===")
print(df.info())

#basic statistics
print(df.describe())

# average per subject
print("\n=== Average Scores ===")
print(df[["Math", "English", "Science"]].mean ())

# add new column: Final average
df["Final_Avg"] = df[["Math", "English", "Science"]].mean(axis=1)

print("\n=== With final average ===")
print(df)

# save new file
df.to_csv("students_result.csv", index=False)
print("\nResult saved to students_result.csv")

