import pandas as pd

#1 download dan load data
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("=== Loaded Titanic Dataset===")
print(df.head()) # tampilkan 5 baris pertama
print("\n=== Missing Values Before ===")
print(df.isnull().sum())

# drop cabin column
df = df.drop(columns=["Cabin"])

# fill missing age with median
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)

# fill missing embarked with most frequent
most_common_embarked = df["Embarked"].mode()[0]
df["Embarked"] = df ["Embarked"].fillna(most_common_embarked)

print("\n=== Missing Values After ===")
print(df.isnull().sum())

#2 info
print("\n=== Info ===")
print(df.info())

#3 statistik dasar
print("\n=== Describe ===")
print(df.describe())

#4 jumlah penumpang selamat (survivor)
survival_counts = df["Survived"]. value_counts()
print("\n=== Survival Count ===")
print(survival_counts)

#5 rata rata umur (average) based on status (survived or nah)
avg_age = df.groupby("Survived")["Age"].mean()
print("\n=== Average Age by Survival ===")
print(avg_age)

#6 Filter: survivor and age>30
adults_survived = df[(df["Survived"] == 1) & (df["Age"] > 30)]
print("\n=== Adults Survived (Age>30) ===")
print(adults_survived.head())

#7 save filter result
adults_survived.to_csv("adults_survived.csv", index=False)
print("\nFiltered data saved to adults_survived.csv")

# Encode categorical data
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

print("\n=== Encoded Data ===")
print(df[["Sex", "Embarked"]].head())


print("\n=== Survival Rate by Gender ===")
gender_survival = df.groupby("Sex")["Survived"].mean()
print(gender_survival)


print("\n=== Survival Rate by Class ===")
class_survival = df.groupby("Pclass")["Survived"].mean()
print(class_survival)


print("\n=== Average Age (Survived vs Not) ===")
age_survival = df.groupby("Survived")["Age"].mean()
print(age_survival)


