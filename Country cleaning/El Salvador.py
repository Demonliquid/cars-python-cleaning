# %%
import os
import pandas as pd
import numpy as np
import re
from scripts import versionfinal,versionurgencia,versionespecifico,identificacionmotor,motorseguncilindrada,corregirmarca, progreso, motor, quitardecimal, valores, modelogeneral, especifico, origensegunvin, version, modelogenerico, especifico2, corregirmodelo, segmentacion, cilindrada, traccion, marca


# %% CARGA DE DATOS

# PAIS
# HAY FILAS CON COLUMNAS MEZCLADAS
elsalvador =  pd.read_csv(r"D:\Basededatos\Origen\El Salvador\El Salvador.txt", encoding='latin-1')


# %% EQUIVALENCIAS
elsalvador.rename(columns={
                'Veh Clase': 'TIPO_VEHICULO',
                'Veh Marca': 'MARCA',
                'Veh Modelo': 'MODELO/VERSION',
                'Veh Ano De Fabricacion': 'AÑO',
                'Veh Chasis': 'NUMERO CHASIS / VIN',
                'Veh Motor': 'NUMERO MOTOR',
                'Pro Departamento': 'PROVINCIA',
                'Pro Municipio': 'LOCALIDAD'
                },
                inplace=True)

elsalvador["MERCADO"] = "EL SALVADOR"
elsalvador["CANTIDAD"] = 1
elsalvador["MOTOR"] = None
elsalvador["MODELO"] = None
elsalvador["VERSION"] = None
elsalvador["MODELO GENERICO"] = None
elsalvador["SEGMENTO.1"] = None
elsalvador["ORIGEN"] = None
elsalvador["TRACCION"] = None
elsalvador["CILINDRADA"] = None
elsalvador["IDENTIFICACION MOTOR"] = None


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
                  "CANTIDAD",
                  "NUMERO CHASIS / VIN",
                  "MOTOR",
                  "NUMERO MOTOR",
                  "PROVINCIA",
                  "LOCALIDAD",
                  "ORIGEN",
                  "CILINDRADA",
                  "TRACCION",
                  "IDENTIFICACION MOTOR"
                  ]
elsalvador = elsalvador[columnasutiles]


# %% Hay modelos sin datos, elsalvador[modelo] es todo valor razonable
condicion = elsalvador["MODELO/VERSION"] != "N/D"
elsalvador = elsalvador[condicion]

condicion = elsalvador["MODELO/VERSION"].notna()
elsalvador = elsalvador[condicion]


# %%
elsalvador["MODELO/VERSION"] = elsalvador["MODELO/VERSION"].astype(str).str.strip()
elsalvador = especifico2(elsalvador, columnasutiles)
elsalvador = versionfinal(elsalvador)
elsalvador = corregirmodelo(elsalvador, columnasutiles)
elsalvador = segmentacion(elsalvador,columnasutiles)


# %% MODELO GENERICO
elsalvador = modelogenerico(elsalvador)


# %%
elsalvador = corregirmarca(elsalvador, columnasutiles)



# %% MOTOR DE MODELO/VERSION
elsalvador = motor(elsalvador)





# %% CILINDRADA
elsalvador = cilindrada(elsalvador, columnasutiles)


# %% TRACCION
elsalvador = traccion(elsalvador)


# %%
condicion = elsalvador["MERCADO"].notna()
elsalvador = elsalvador[condicion]

# %%
elsalvador = quitardecimal(elsalvador, "AÑO")
elsalvador = identificacionmotor(elsalvador, columnasutiles)



# %%
elsalvador.to_csv(r'D:\Basededatos\Limpioparaunir\elsalvador.csv', index=False)

# %%
valores(elsalvador, "TIPO_VEHICULO")
# %%
elsalvador.head()
# %%
