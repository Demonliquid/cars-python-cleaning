# VIENE DE CHILE INSCRIPCIONES Y VOLANTE

# %% IMPORTAR LIBRERIAS
import os
import pandas as pd
import numpy as np
import datetime


# %% CARGA DE DATOS
inscripciones = pd.read_csv(r"D:\Basededatos\Limpioparaentregar\chileinscripciones.csv")
volanteomaleta = pd.read_csv(r"D:\Basededatos\Limpioparaentregar\datosVM.csv")


# %% PREPARACION DE UNION
inscripciones.rename(columns={"PPU": "PATENTE", "TIPO VEHICULO": "SEGMENTO.1", "AÑO FABRICACION": "AÑO", "MODELO": "MODELO / VERSION"}, inplace=True)


# %% UNION
chile = pd.concat([inscripciones, volanteomaleta], ignore_index=True)
inscripciones = None
volanteomaleta = volanteomaleta[["PATENTE", "NUMERO MOTOR"]]


# %% PATENTES DUPLICADAS
chile.drop_duplicates(subset="PATENTE", inplace=True)

# %%
chile = chile.merge(volanteomaleta, on="PATENTE", how="left")
volanteomaleta = None

# %% PATENTES DUPLICADAS
chile.drop_duplicates(subset="PATENTE", inplace=True)


# %%
condicion = chile["NUMERO MOTOR_x"].isna() & chile["NUMERO MOTOR_y"].notna()
chile.loc[condicion, "NUMERO MOTOR_x"] = chile["NUMERO MOTOR_y"]

chile.rename(columns={"NUMERO MOTOR_x": "NUMERO MOTOR"}, inplace=True)
chile = chile[["PATENTE", "SEGMENTO.1","MARCA","MODELO / VERSION", "AÑO", "RUT", "NUMERO MOTOR"]]


# %% ASEGURAR QUE CADA ELEMENTO TENGA PATENTE
condicion = chile["PATENTE"].notna()
chile = chile[condicion]


# %% CAMPOS GENERALES
chile["MERCADO"] = "CHILE"
chile["CANTIDAD"] = 1


# %% ELEMENTOS SIN DATOS COMO BLANKS
condicion = chile["MARCA"] == "Sin Datos"
chile.loc[condicion, "MARCA"] = None
condicion = chile["MODELO / VERSION"] == "Sin Datos"
chile.loc[condicion, "MODELO / VERSION"] = None
condicion = chile["SEGMENTO.1"] == "Sin Datos"
chile.loc[condicion, "SEGMENTO.1"] = None
condicion = chile["MODELO / VERSION"] == "NO REGISTRA"
chile.loc[condicion, "MODELO / VERSION"] = None


# %% ELEMENTOS UNIFORMES
chile["MARCA"] = chile["MARCA"].str.upper()
chile["MODELO / VERSION"] = chile["MODELO / VERSION"].str.upper()
chile["SEGMENTO.1"] = chile["SEGMENTO.1"].str.upper()

chile["MARCA"] = chile["MARCA"].str.strip()
chile["MODELO / VERSION"] = chile["MODELO / VERSION"].str.strip()
chile["SEGMENTO.1"] = chile["SEGMENTO.1"].str.strip()

# %% CORREGIR AÑO
chile["AÑO"] = chile["AÑO"].astype("float").map('{:.0f}'.format)


# %% AGREGAR MOTOR
chile["MOTOR"] = chile["MODELO / VERSION"].str.extract(r'(\d\.\d)', expand=False).str.strip()
chile["MOTOR"].replace(r'', None)


# %% AGREGAR MODELO
new = chile["MODELO / VERSION"].str.split(" ", n = 1, expand = True)
chile["MODELO"] = new[0] 


# %% SIGUE EN CHILE 1 y 2.py
chile[:4719797].to_csv(r'D:\Basededatos\Limpioparaentregar\chile1.csv', index=False)
chile[4719797:].to_csv(r'D:\Basededatos\Limpioparaentregar\chile2.csv', index=False)

# %%
