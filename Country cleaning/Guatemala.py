# %%
import os
import pandas as pd
import numpy as np
import datetime
from scripts import versionfinal,versionurgencia,versionespecifico,identificacionmotor,motorseguncilindrada,corregirmarca, progreso, motor, quitardecimal, valores, modelogeneral, especifico, origensegunvin, version, modelogenerico, especifico2, corregirmodelo, segmentacion, cilindrada, traccion, marca


# %% CARGA DE DATOS

# PAIS 
# SE PIERDEN 3 LINEAS, DEJAR O AGREGAR MANUALMENTE
guatemala = pd.read_csv(r"D:\Basededatos\Origen\Guatemala\Guatemala 2020.txt",
                        names= ["ANIO_ALZA", "MES", "NOMBRE_DEPARTAMENTO", "NOMBRE_MUNICIPIO", "MODELO_VEHICULO", "LINEA_VEHICULO", "TIPO_VEHICULO", "USO_VEHICULO", "MARCA_VEHICULO", "CANTIDAD"],
                        quotechar='"',
                        sep="|",
                        error_bad_lines=False,
                        engine='python')


# %% ARGEGA LINEAS PERDIDAS
datosperdidos = pd.DataFrame(
    {"ANIO_ALZA": [1993, 1995, 1994],
    "MES": [8, 5, 11],
    "NOMBRE_DEPARTAMENTO": ["ZACAPA", "GUATEMALA", "GUATEMALA"],
    "NOMBRE_MUNICIPIO": ["ZACAPA", "SAN MIGUEL PETAPA", "GUATEMALA"],
    "MODELO_VEHICULO": [1989, 1995, 1995],
    "LINEA_VEHICULO": [r'"E" 4WD', r'"H100 DLX', r'"H100 DLX'],
    "TIPO_VEHICULO": ["PICK UP", "PANEL", "PANEL"],
    "USO_VEHICULO": ["PARTICULAR", "PARTICULAR", "PARTICULAR"],
    "MARCA_VEHICULO": ["NISSAN", "HYUNDAI", "HYUNDAI"],
    "CANTIDAD": [1, 1, 1]}
    )
guatemala = guatemala.append(datosperdidos)


# %% 49005 autos con MODELO_VEHICULO = '1980 o menor'
guatemala["MODELO_VEHICULO"].replace('1980 o menor', '1980', inplace=True) 


# %% COLUMNAS UTILES
guatemala.rename(columns={
                'TIPO_VEHICULO': 'SEGMENTO.1',
                'MARCA_VEHICULO': 'MARCA',
                'LINEA_VEHICULO': 'MODELO/VERSION',
                'MODELO_VEHICULO': 'AÑO',
                'CANTIDAD': 'FLOTA 2019',
                'NOMBRE_DEPARTAMENTO': 'PROVINCIA',
                'NOMBRE_MUNICIPIO': 'LOCALIDAD'},
                inplace=True)


guatemala["MERCADO"] = "GUATEMALA"
guatemala["MOTOR"] = None
guatemala["MODELO"] = None
guatemala["MODELO GENERICO"] = None
guatemala["VERSION"] = None
guatemala["CILINDRADA"] = None
guatemala["TIPO_VEHICULO"] = None

columnasutiles = [
                  "MERCADO",
                  "TIPO_VEHICULO",
                  "SEGMENTO.1",
                  "MARCA",
                  "MODELO GENERICO",
                  "MODELO",
                  "MODELO/VERSION",
                  "VERSION",
                  "AÑO",
                  "MOTOR",
                  "CILINDRADA",
                  "FLOTA 2019",
                  'PROVINCIA',
                  'LOCALIDAD']

guatemala = guatemala[columnasutiles]


# %%
condicion = guatemala["MODELO/VERSION"] == "."
guatemala.loc[condicion, "MODELO/VERSION"] = None

# %%
condicion = guatemala["MODELO/VERSION"].isin(["SIN LINEA"])
guatemala.loc[condicion, "MODELO/VERSION"] = None

condicion = guatemala["MODELO/VERSION"].notna()
guatemala = guatemala[condicion]
condicion = None

# %%
guatemala = corregirmarca(guatemala, columnasutiles)

# %%
guatemala["MODELO/VERSION"] = guatemala["MODELO/VERSION"].astype(str).str.strip()
guatemala = especifico2(guatemala, columnasutiles)
guatemala = versionfinal(guatemala)
guatemala = corregirmodelo(guatemala, columnasutiles)
guatemala = segmentacion(guatemala,columnasutiles)


# %% MODELO GENERICO
guatemala = modelogenerico(guatemala)

# %%
# %% MOTOR
guatemala = motor(guatemala)

# %%
guatemala = cilindrada(guatemala, columnasutiles)


# %%
guatemala.info(null_counts=True)

# %%
guatemala.to_csv(r'D:\Basededatos\Limpioparaunir\guatemala.csv', index=False)


# %%
