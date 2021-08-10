# %%
import os
import pandas as pd
import numpy as np
import re
from scripts import motor, quitardecimal, valores, modelogeneral, especifico, origensegunvin, version, modelogenerico


# %% CARGA DE DATOS
diciembre2016 = pd.read_excel(r"D:\Basededatos\Origen\Panama\Concesionaria\Diciembre 2016.xlsx", engine='openpyxl')
diciembre2020 = pd.read_excel(r"D:\Basededatos\Origen\Panama\Concesionaria\Diciembre 2020.xlsx", engine='openpyxl')


# %%
diciembre2020.dropna(how="all", inplace=True)


# %%
panama = pd.concat([diciembre2016, diciembre2020])


# %% COLUMNAS UTILES
panama.rename(columns={
                'TIPO_DE_VEHICULO': 'SEGMENTO.1',
                "MUNICIPIO": "LOCALIDAD",
                "TAMAÑO_MOTOR": "CILINDRADA",
                "NRO_CILINDROS": "CILINDROS",
                "TRACCION_MOTOR": "TRACCION",
                "TIPO_TRANSMISION": "TRANSMISION",
                "ANO_VEHICULO": "AÑO",
                "TIPO_COMBUSTIBLE": "COMBUSTIBLE",
                "CHASIS": "NUMERO CHASIS / VIN",
                "MOTOR": "NUMERO MOTOR",
                "VEH_NRO_PLACA": "PATENTE",
                "MODELO": "MODELO/VERSION"
                },
                inplace=True)

panama["MERCADO"] = "PANAMA"
panama["ORIGEN"] = None
panama["CANTIDAD"] = 1
panama["MODELO"] = None
panama["MODELO GENERICO"] = None
panama["VERSION"] = None
panama["MOTOR"] = None


columnasutiles = [
                  "MERCADO",
                  "MARCA",
                  "MODELO GENERICO",
                  "MODELO",
                  "MODELO/VERSION",
                  "VERSION",
                  "PROVINCIA",
                  "LOCALIDAD",
                  "CILINDRADA",
                  "CILINDROS",
                  "TRACCION",
                  "TRANSMISION",
                  "FRENOS_DELANTEROS",
                  "FRENOS_TRASEROS",
                  "AÑO",
                  "COMBUSTIBLE",
                  "MOTOR",
                  "NUMERO CHASIS / VIN",
                  "NUMERO MOTOR",
                  "PATENTE",
                  "CANTIDAD",
                  "ORIGEN"
                  ]

panama = panama[columnasutiles]


# %%
panama = origensegunvin(panama)

# %% MOTOR DE MODELO/VERSION
panama = motor(panama)


# %% MODELO GENERAL
panama = modelogeneral(panama)


# %% MODELO ESPECIFICO
panama = especifico(panama, columnasutiles)


# %% MODELO GENERICO
panama = modelogenerico(panama)


# %% VERSION
panama = version(panama)


# %%
panama = panama[0:8988]

# %%
panama = quitardecimal(panama,"CILINDRADA")
panama = quitardecimal(panama,"CILINDROS")
panama = quitardecimal(panama,"AÑO")


# %%
panama["ORIGEN"] = panama["ORIGEN"].str.upper()



# %%
panama.to_csv(r'D:\Basededatos\Limpioparaunir\panamaconcesionaria.csv', index=False)


# %%
valores(panama, "MODELO")
# %%
condicion = panama["MODELO"] == "NEW"
valores(panama[condicion], "MODELO/VERSION")
# %%



