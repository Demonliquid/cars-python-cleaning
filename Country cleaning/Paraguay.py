# %%
import os
import pandas as pd
import numpy as np
import re
from scripts import versionfinal,versionurgencia,versionespecifico,identificacionmotor,motorseguncilindrada,corregirmarca, progreso, motor, quitardecimal, valores, modelogeneral, especifico, origensegunvin, version, modelogenerico, especifico2, corregirmodelo, segmentacion, cilindrada, traccion, marca


# %% CARGA DE DATOS
# NADA QUE AGREGAR DESDE ORIGEN, SON LOS DATOS QUE HAY
# paraguay
# HAY FILAS CON COLUMNAS MEZCLADAS
paraguay =  pd.read_csv(r"D:\Basededatos\Origen\Paraguay\Bases Unificadas_Paraguay_Limpio.csv")


# %%
paraguay = quitardecimal(paraguay, "Año de fabricacion")


# %% COLUMNAS UTILES
paraguay["MERCADO"] = "PARAGUAY"
paraguay["CANTIDAD"] = 1
paraguay["MOTOR"] = None
paraguay["MODELO"] = None
paraguay["VERSION"] = None
paraguay["MODELO GENERICO"] = None
paraguay["SEGMENTO.1"] = None
paraguay["CARROCERIA"] = None
paraguay["TRACCION"] = None
paraguay["CILINDRADA"] = None

paraguay.rename(columns={
                'Clase de Automotor': 'TIPO_VEHICULO',
                'Marca': 'MARCA',
                'Modelo': 'MODELO/VERSION',
                'País de Fabricación': 'ORIGEN',
                'Año de fabricacion': 'AÑO'},
                inplace=True)


columnasutiles = [
                  "MERCADO",
                  "TIPO_VEHICULO",
                  "MARCA",
                  "MODELO GENERICO",
                  "MODELO",
                  "MODELO/VERSION",
                  "VERSION",
                  "AÑO",
                  "MOTOR",
                  "CANTIDAD",
                  "ORIGEN",
                  "SEGMENTO.1",
                  "CARROCERIA",
                  "TRACCION",
                  "CILINDRADA"
                  ]

paraguay = paraguay[columnasutiles]


# %% TIPO_VEHICULO
paraguay["TIPO_VEHICULO"] = paraguay["TIPO_VEHICULO"].str.upper()
condicion = paraguay["TIPO_VEHICULO"] == "AUTOMOTOR"
paraguay.loc[condicion, "TIPO_VEHICULO"] = "AUTO"
condicion = paraguay["TIPO_VEHICULO"] == "AUTOS ANTIGUOS"
paraguay.loc[condicion, "TIPO_VEHICULO"] = "AUTO"
condicion = None
condicion = paraguay["TIPO_VEHICULO"] == "MOTOS ANTIGUAS"
paraguay.loc[condicion, "TIPO_VEHICULO"] = "MOTOCICLETA"
condicion = None
condicion = paraguay["TIPO_VEHICULO"] == "TRACTOR/MAQUINARIA"
paraguay.loc[condicion, "TIPO_VEHICULO"] = "TRACTOR"
condicion = None


# %% MOTOR DE MODELO/VERSION
paraguay = motor(paraguay)

# %%
paraguay = corregirmarca(paraguay,columnasutiles)

# %% MODELO
paraguay["MODELO/VERSION"] = paraguay["MODELO/VERSION"].astype(str).str.strip()
paraguay = especifico2(paraguay, columnasutiles)
paraguay = versionfinal(paraguay)
paraguay = corregirmodelo(paraguay, columnasutiles)
paraguay = segmentacion(paraguay,columnasutiles)


# %% MODELO GENERICO
paraguay = modelogenerico(paraguay)




# %% CILINDRADA
paraguay = cilindrada(paraguay, columnasutiles)

# %% TRACCION
paraguay = traccion(paraguay)

# %% ARREGLOS ESPECIFICOS
# ALGUNOS VALORES MEZCLADOS
paraguay["ORIGEN"] = paraguay["ORIGEN"].str.upper()
condicion = paraguay["ORIGEN"] != "2018-03-20 00:00:00"
paraguay = paraguay[condicion]
condicion = paraguay["ORIGEN"] != "NO"
paraguay = paraguay[condicion]
condicion = None
condicion = (paraguay["TIPO_VEHICULO"] == "DORADO") | (paraguay["TIPO_VEHICULO"] == "NEGRO/ROJO")
paraguay = paraguay[~condicion]
condicion = None

condicion = paraguay["MODELO/VERSION"].isin(["3 EJES", "Sin Especificar", "Sin especificacion"])
paraguay.loc[condicion,"MODELO/VERSION"] = None

condicion = paraguay["MODELO/VERSION"].notna()
paraguay = paraguay[condicion]


# %%
paraguay.info(null_counts=True)

# %%
condicion = paraguay["AÑO"] == "nan"
paraguay.loc[condicion, "AÑO"] = None


# %% GUARDAR ARCHIVO
paraguay.to_csv(r'D:\Basededatos\Limpioparaunir\paraguay.csv', index=False)


# %%
progreso = progreso(paraguay)
progreso


# %%
condicion = paraguay["MODELO"].isna()
paraguay[condicion]
# %%
valores(paraguay, "AÑO")
# %%
