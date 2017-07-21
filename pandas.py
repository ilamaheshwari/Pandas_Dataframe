import pandas as pd

dataset=pd.read_csv("training_titanic.csv")
a=dataset["Survived"].value_counts()
print(a)
print dataset["Survived"].value_counts(normalize="true")
print dataset["Sex"].value_counts(a[1])
print dataset["Sex"].value_counts(a[0])