# %%
import os
import pandas as pd
import numpy as np
import datetime
from scripts import versionfinal,versionurgencia,versionespecifico,identificacionmotor,motorseguncilindrada,corregirmarca, progreso, motor, quitardecimal, valores, modelogeneral, especifico, origensegunvin, version, modelogenerico, especifico2, corregirmodelo, segmentacion, cilindrada, traccion, marca


# %% CARGA DE DATOS
path = r'D:\Basededatos\Origen\Honduras'
os.chdir(path)
files = os.listdir(path)
files

files_xls = [f for f in files if f[-4:] == 'xlsx']
files_xls

# %%

honduras = pd.DataFrame()


for f in files_xls:
    data = pd.read_excel(f, engine='openpyxl')
    honduras = pd.concat([honduras , data], ignore_index=True, join='outer')
    data = None




# %% IDENTIFICAR DATOS DE ORIGEN DENTRO DEL FORMATO ESTANDAR
honduras.rename(columns={
                'AÑO DEL VEHICULO': 'AÑO',
                'TIPO': 'SEGMENTO.1',
                "TIPO DE\nCOMBUSTIBLE": "COMBUSTIBLE",
                'MODELO': 'MODELO/VERSION',
                'CILINDRAJE': 'CILINDRADA',
                "CANTIDAD DE\nPLACAS": "CANTIDAD"},
                inplace=True)

# %% COLUMNAS A AGREGARSE E IDENTIFICAR MERCADO
honduras["MERCADO"] = "HONDURAS"
honduras["MOTOR"] = None
honduras["MODELO GENERICO"] = None
honduras["MODELO"] = None
honduras["VERSION"] = None
honduras["TIPO_VEHICULO"] = None


# %% SI NO TIENEN REFERENCIA NO SIRVE
condicion = honduras["MODELO/VERSION"].notna()
honduras = honduras[condicion]


# %%
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
                  "COMBUSTIBLE",
                  "CANTIDAD"
                  ]

honduras = honduras[columnasutiles]


# %% ARREGLAR AÑO
condicion = honduras["AÑO"] == 0
honduras.loc[condicion, "AÑO"] = None
condicion = None

condicion = honduras["AÑO"] > 2021
honduras.loc[condicion, "AÑO"] = None
condicion = None


condicion = honduras["AÑO"].notna()
honduras = honduras[condicion]


# %%
honduras = corregirmarca(honduras, columnasutiles)


# %%
honduras["MODELO/VERSION"] = honduras["MODELO/VERSION"].astype(str).str.strip()
honduras = especifico2(honduras, columnasutiles)
honduras = versionfinal(honduras)
honduras = corregirmodelo(honduras, columnasutiles)
honduras = segmentacion(honduras,columnasutiles)


# %%
condicion = honduras["COMBUSTIBLE"] == "G"
honduras.loc[condicion, "COMBUSTIBLE"] = "GASOLINA"

condicion = honduras["COMBUSTIBLE"] == "D"
honduras.loc[condicion, "COMBUSTIBLE"] = "DIESEL"

condicion = honduras["COMBUSTIBLE"].isin(["GASOLINA", "DIESEL"])
honduras.loc[~condicion, "COMBUSTIBLE"] = None


# %%
honduras = modelogenerico(honduras)


# %% MOTOR
honduras = motor(honduras)


# %%
honduras = quitardecimal(honduras, "AÑO")

# %%
honduras.to_csv(r'D:\Basededatos\Limpioparaunir\honduras.csv', index=False)

# %%
honduras.info(null_counts=True)
# %%
condicion = honduras["MODELO"].isna()
valores(honduras[condicion], "MODELO/VERSION")
# %%
