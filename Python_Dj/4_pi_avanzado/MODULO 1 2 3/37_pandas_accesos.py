import pandas as pd

# lee el archivo CSV
df = pd.read_csv(
    "/home/mecz/Cursos/Netzun/Python_Dj/4_pi_avanzado/36_CONTRATACIONDIRECTA.csv",
    encoding='latin1',
    delimiter=';')

# Acceso por posición de filas

print(df[0:3])

# Acceso por columnas

print(df[["CODIGOENTIDAD","RUC_ENTIDAD", "CATEGORIA"]])