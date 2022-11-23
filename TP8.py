import numpy as np
import pandas as pd

titanic = pd.read_csv("data/titanic.txt", sep = ";")

print(titanic)
titanic.info()