import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris = pd.read_csv("data/iris.data", header=None)
iris.columns = [
    "sepal length", 
    "sepal width", 
    "petal length", 
    "petal width", 
    "class"]

print(iris)
iris.info()
print(iris["class"].value_counts())

fig, axs = plt.subplots(2, 2)
cn = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

sns.boxplot(x = "class", y = "sepal length", data = iris, order = cn, ax = axs[0, 0])
sns.boxplot(x = "class", y = "sepal width", data = iris, order = cn, ax = axs[0, 1])
sns.boxplot(x = "class", y = "petal length", data = iris, order = cn, ax = axs[1, 0])
sns.boxplot(x = "class", y = "petal width", data = iris, order = cn, ax = axs[1, 1])

fig.tight_layout(pad = 1.0)
fig.savefig("img/iris.png")

matcorr = iris.corr()
print(matcorr)

fig, axs = plt.subplots(1, 1)
sns.set()
sns.heatmap(matcorr)
fig.savefig("img/iris_corr.png")