import pandas as pd

# lee el archivo CSV
df = pd.read_csv(
    "/home/mecz/Cursos/Netzun/Python_Dj/4_pi_avanzado/36_CONTRATACIONDIRECTA.csv",
    encoding='latin1',
    delimiter=';',
    on_bad_lines='skip'
    )

# Filtrado
filter = df["CATEGORIA"] == "MATERIAL Y EQUIPO MEDICO"
df_equipo_medico = df.where(filter).notna()
print(df_equipo_medico)