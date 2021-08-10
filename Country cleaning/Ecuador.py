# %%
import os
import pandas as pd
import numpy as np
import re
from scripts import versionfinal,versionurgencia,versionespecifico,identificacionmotor,motorseguncilindrada,corregirmarca, progreso, motor, quitardecimal, valores, modelogeneral, especifico, origensegunvin, version, modelogenerico, especifico2, corregirmodelo, segmentacion, cilindrada, traccion, marca


# %% CARGA DE DATOS

# ecuador
# HAY FILAS CON COLUMNAS MEZCLADAS
ecuador = pd.read_csv(r"D:\Basededatos\Origen\Ecuador\ecuador.csv")

# %%
ecuador = ecuador[["Marca",
                   "Modelo",
                   "Origen",
                   "Año Modelo",
                   "Tipo",
                   "Clase",
                   "Sub Clase",
                   "Motor",
                   "Cilindraje",
                   "Tipo Combustible",
                   "CANTON",
                   "PROVINCIA"]]



# %%
condicion = ecuador["Sub Clase"].isin(["CAMION", "FURGON-C", "BUS", "CAMION PEQUEÑO", "BUS ESCOLAR", "RECOLECTOR", "MOTOBOMBA", "TRACTOR", "DOBLE PISO"])
ecuador.loc[condicion, "Clase"] = ecuador.loc[condicion, "Sub Clase"]


condicion = ecuador["Tipo"] == "PESADO"
ecuador.loc[condicion, "Sub Clase"] = ecuador.loc[condicion, "Tipo"]


condicion = ecuador["Clase"] == "FURGON-C"
ecuador.loc[condicion, "Clase"] = "FURGON"




# %% COLUMNAS UTILES
ecuador["MERCADO"] = "ECUADOR"
ecuador["CANTIDAD"] = 1
ecuador["MODELO"] = None
ecuador["VERSION"] = None
ecuador["MODELO GENERICO"] = None

ecuador.rename(columns={
                'Marca': 'MARCA',
                'Modelo': 'MODELO/VERSION',
                'Origen': 'ORIGEN',
                'Año Modelo': 'AÑO',
                'Clase': 'TIPO_VEHICULO',
                'Sub Clase': 'SEGMENTO.1',
                'Motor': 'MOTOR',
                'Cilindraje': 'CILINDRADA',
                'CANTON': 'LOCALIDAD',
                'Tipo Combustible': 'COMBUSTIBLE',},
                inplace=True)

columnasutiles = list(ecuador.columns)
columnasutiles.remove("Tipo")
ecuador = ecuador[columnasutiles]

# %%
ecuador = corregirmarca(ecuador, columnasutiles)

# %% MODELO GENERAL
ecuador["MODELO/VERSION"] = ecuador["MODELO/VERSION"].astype(str).str.strip()
ecuador = especifico2(ecuador, columnasutiles)
ecuador = versionfinal(ecuador)
ecuador = corregirmodelo(ecuador, columnasutiles)
ecuador = segmentacion(ecuador,columnasutiles)

# %% MODELO GENERICO
ecuador = modelogenerico(ecuador)



# %% MOTOR DE MODELO/VERSION
ecuador = motorseguncilindrada(ecuador,columnasutiles)


# %%
ecuador.info()

# %%
ecuador.to_csv(r'D:\Basededatos\Limpioparaunir\ecuador.csv', index=False)

# %%
valores(ecuador, "VERSION")
# %%
condicion = ecuador["MODELO"].isna()
valores(ecuador[condicion], "MODELO/VERSION")
# %%
