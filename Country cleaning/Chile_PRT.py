# %%
import os
from numpy.lib.shape_base import expand_dims
import pandas as pd
import numpy as np
import re
from scripts import versionfinal,versionurgencia,versionespecifico,identificacionmotor,motorseguncilindrada,corregirmarca, progreso, motor, quitardecimal, valores, modelogeneral, especifico, origensegunvin, version, modelogenerico, especifico2, corregirmodelo, segmentacion, cilindrada, traccion, marca


# %% CARGA DE DATOS

# chile
# HAY FILAS CON COLUMNAS MEZCLADAS
chile =  pd.read_csv(r"D:\Basededatos\Origen\Chile\PRT\PRT_FINAL.csv")


# %%
chile = quitardecimal(chile, "ANO_FABRICACION")


# %% COLUMNAS UTILES
chile.rename(columns={
                'PPU': 'PATENTE',
                'MODELO': 'MODELO/VERSION',
                'ANO_FABRICACION': 'AÑO',
                'NUM_MOTOR': 'NUMERO MOTOR',
                'NUM_CHASIS': "NUMERO CHASIS / VIN"},
                inplace=True)


chile["MERCADO"] = "CHILE"
chile["CANTIDAD"] = 1
chile["MOTOR"] = None
chile["MODELO"] = None
chile["VERSION"] = None
chile["MODELO GENERICO"] = None
chile["ORIGEN"] = None
chile["TIPO_VEHICULO"] = None
chile["SEGMENTO.1"] = None
chile["CARROCERIA"] = None
chile["TRACCION"] = None
chile["CILINDRADA"] = None


columnasutiles = [
                  "MERCADO",
                  "PATENTE",
                  "MARCA",
                  "MODELO GENERICO",
                  "MODELO",
                  "MODELO/VERSION",
                  "VERSION",
                  "AÑO",
                  "MOTOR",
                  "NUMERO MOTOR",
                  "NUMERO CHASIS / VIN",
                  "VIN",
                  "CANTIDAD",
                  "ORIGEN",
                  "TIPO_VEHICULO",
                  "SEGMENTO.1",
                  "CARROCERIA",
                  "TRACCION",
                  "CILINDRADA"
                  ]

chile = chile[columnasutiles]





# %% MOTOR DE MODELO/VERSION
chile = motor(chile)


# %% MODELO 1
chile["MODELO/VERSION"] = chile["MODELO/VERSION"].str.upper()


condicion = chile["MODELO/VERSION"].notna()
chile = chile[condicion]
condicion = None

# %%
chile = corregirmarca(chile, columnasutiles)

# %% MODELO 2
chile["MODELO/VERSION"] = chile["MODELO/VERSION"].astype(str).str.strip()
chile = especifico2(chile, columnasutiles)
chile = versionfinal(chile)
chile = corregirmodelo(chile, columnasutiles)
chile = segmentacion(chile,columnasutiles)


# QUITAR HECHIZO QUE TIENE MODELO/VERSION ILEGIBLE
condicion1= chile["MARCA"] == "HECHIZO"
condicion2= chile["MODELO"].isna()
chile.loc[condicion1 & condicion2, "MODELO/VERSION"] = None
condicion1 = None
condicion2 = None
condicion = chile["MODELO/VERSION"].notna()
chile = chile[condicion]
condicion = None


# %% MODELO GENERICO
chile = modelogenerico(chile)


# %% ARREGLAR VIN
# TENGO DOS COLUMAS DE VIN
# LOS QUE ESTEN BIEN EN VIN, VAN A NUMERO CHASIS / VIN
sincaracter = chile["VIN"].str.isalnum() == True
cantidad = chile["VIN"].str.len() == 17
letras = chile["VIN"].str.contains(r'Q|O|I|q|o|i|-|\s', regex=True) == False
condicion = sincaracter & cantidad & letras

chile.loc[condicion, "NUMERO CHASIS / VIN"] = chile.loc[condicion, "VIN"]


# %% LIMPIAR NUMERO CHASIS / VIN
sincaracter = chile["NUMERO CHASIS / VIN"].str.isalnum() == True
cantidad = chile["NUMERO CHASIS / VIN"].str.len() == 17
letras = chile["NUMERO CHASIS / VIN"].str.contains(r'Q|O|I|q|o|i|-|\s', regex=True) == False
condicion = sincaracter & cantidad & letras

chile.loc[~condicion, "NUMERO CHASIS / VIN"] = None


# %% ORIGEN SEGUN VIN
chile = origensegunvin(chile)


# %%
chile = cilindrada(chile, columnasutiles)


# %%
chile = traccion(chile)


# %% SACAR EL VIN DE MAS EN COLUMNAS UTILES
chile["IDENTIFICACION MOTOR"] = None
columnasutiles = [
                  "MERCADO",
                  "PATENTE",
                  "MARCA",
                  "MODELO GENERICO",
                  "MODELO",
                  "MODELO/VERSION",
                  "VERSION",
                  "AÑO",
                  "MOTOR",
                  "NUMERO MOTOR",
                  "NUMERO CHASIS / VIN",
                  "CANTIDAD",
                  "ORIGEN",
                  "TIPO_VEHICULO",
                  "SEGMENTO.1",
                  "CARROCERIA",
                  "TRACCION",
                  "CILINDRADA",
                  "IDENTIFICACION MOTOR"
                  ]


chile = chile[columnasutiles]


# %%
condicion = chile["NUMERO MOTOR"] == "HECHIZO"
chile.loc[condicion] = None
condicion = None

errores = [0,
           "S/N",
           "0",
           "NO REGISTRA",
           "SN",
           "-",
           "N/R",
           "SIN NUMERO",
           "NO TIENE",
           "S/M",
           ".",
           "NOREGISTRA",
           "NR",
           "SINNUMERO",
           "S-N",
           "S/N",
           "SM",
           "NO REG",
           "NO REGISTRA",
           "SIN",
           "S.N",
           "S",
           "NO  REGISTRA",
           "NOTIENE",
           "s/n",
           "#NAME?",
           "--",
           "SIN MOTOR",
           "sin registro",
           "no registra",
           "S/n"          
           ]
condicion = chile["NUMERO MOTOR"].isin(errores) 
chile.loc[condicion, "NUMERO MOTOR"] = None
errores = None

# %%
chile = quitardecimal(chile, "AÑO")
chile = quitardecimal(chile, "CANTIDAD")
chile = quitardecimal(chile, "CILINDRADA")

# %%
condicion = chile["CILINDRADA"] == "nan"
chile.loc[condicion, "CILINDRADA"] = None


# %%
chile = chile.drop_duplicates(subset="PATENTE")
chile = chile.dropna(subset=["PATENTE"])


# %%
condicion = chile["NUMERO MOTOR"].isna()
chile.loc[condicion, "NUMERO MOTOR"] = 0

condicion = chile["NUMERO CHASIS / VIN"].isna()
chile.loc[condicion, "NUMERO CHASIS / VIN"] = 0


# %%
chile = identificacionmotor(chile, columnasutiles)

# %%
columnasutiles.remove("PATENTE")
chile = chile[columnasutiles]

# %%
chile.to_csv(r'D:\Basededatos\Limpioparaunir\chile_prt.csv', index=False)


# %%
chile.info(null_counts=True)
# %%
condicion = chile["MARCA"] == "SAMSUNG"
valores(chile[condicion], "MODELO/VERSION")
# %%
