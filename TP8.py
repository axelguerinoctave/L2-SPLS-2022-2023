import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("data/titanic.txt", sep = ";")

del titanic["Name"]

titanic["Sex"] = titanic["Sex"].astype("category")
cat_columns = titanic.select_dtypes(["category"]).columns
titanic[cat_columns] = titanic[cat_columns].apply(lambda x: x.cat.codes)

matcorr = titanic.corr()

print(matcorr)
print(titanic)
titanic.info()

titanic["Survived"].value_counts()

survived = titanic[titanic["Survived"] == 1]["Sex"].value_counts()
dead = titanic[titanic["Survived"] == 0]["Sex"].value_counts()
df = pd.DataFrame([survived, dead])
df.index = ["Survived", "Dead"]
df.columns = ["Female", "Male"]

print(df)
df.plot(kind = "bar", stacked = True, figsize = (7, 3))

survived = titanic[titanic["Survived"] == 1]["Pclass"].value_counts()
dead = titanic[titanic["Survived"] == 0]["Pclass"].value_counts()
df = pd.DataFrame([survived, dead])
df.index = ["Survived", "Dead"]

print(df)
df.plot(kind = "bar", stacked = True, figsize = (7, 3))

F1 = titanic.query("Sex == 0 & Pclass == 1")["Survived"].value_counts()
F2 = titanic.query("Sex == 0 & Pclass == 2")["Survived"].value_counts()
F3 = titanic.query("Sex == 0 & Pclass == 3")["Survived"].value_counts()
H1 = titanic.query("Sex == 1 & Pclass == 1")["Survived"].value_counts()
H2 = titanic.query("Sex == 1 & Pclass == 2")["Survived"].value_counts()
H3 = titanic.query("Sex == 1 & Pclass == 3")["Survived"].value_counts()
df = pd.DataFrame([F1, F2, F3, H1, H2, H3])
df.columns = ["Survived", "Dead"]
df.index = ["F1", "F2", "F3", "H1", "H2", "H3"]
print(df)
df.plot(kind = "bar", stacked = True, figsize = (7, 3))

age_limite = 15
enfant = titanic[titanic["Age"] <= age_limite]["Survived"].value_counts()
adulte = titanic[titanic["Age"] > age_limite]["Survived"].value_counts()
df = pd.DataFrame([enfant, adulte])
df.index = ["Enfant", "Adulte"]
df.columns = ["Dead", "Survived"]

print(df)
df.plot(kind = "bar", stacked = True, figsize = (7, 3))

C1 = titanic.query("Age <= 15")["Survived"].value_counts()
C2 = titanic.query("Age > 15 & Age <= 30")["Survived"].value_counts()
C3 = titanic.query("Age > 30 & Age <= 45")["Survived"].value_counts()
C4 = titanic.query("Age > 45 & Age <= 60")["Survived"].value_counts()
C5 = titanic.query("Age > 60")["Survived"].value_counts()
df = pd.DataFrame([C1, C2, C3, C4, C5])
df.columns = ["Dead", "Survived"]
df.index = ["C1", "C2", "C3", "C4", "C5"]
print(df)
df.plot(kind = "bar", stacked = True, figsize = (7, 3))
