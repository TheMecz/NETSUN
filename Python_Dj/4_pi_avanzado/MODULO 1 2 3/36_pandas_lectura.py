import pandas as pd

#lee archivo csv

df = pd.read_csv(
    "/home/mecz/Cursos/Netzun/Python_Dj/4_pi_avanzado/36_CONTRATACIONDIRECTA.csv",
    encoding='latin1',
    delimiter=';')

#muestra la primera tabla

print(df.head())
print(df)