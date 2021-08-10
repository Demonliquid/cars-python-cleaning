# %%
import os
import pandas as pd
import numpy as np
import datetime
import re
from scripts import progreso, motor, quitardecimal, valores, modelogeneral, especifico, origensegunvin, version, modelogenerico, especifico2, corregirmodelo, segmentacion, cilindrada, traccion, versionespecifico, versionurgencia, corregirmarca, marca


# %%
pd.set_option('display.max_colwidth', None)



# %% CARGA DE DATOS

path = r'D:\Basededatos\Origen\Peru\2004-2007'
os.chdir(path)
files = os.listdir(path)
files


# %%
files_xls = [f for f in files if f[-4:] == 'xlsx']
files_xls

# %%
columnas = ["Marca",'Descripción de Mercadería', "Cant. VF", "Código NCM", "Fecha", "País de Origen"]
peru = pd.DataFrame(columns=columnas)



# %%
for f in files_xls:
    data = pd.read_excel(f, engine='openpyxl')
    peru = pd.concat([peru , data], ignore_index=True, join='inner')



# %% COLUMNAS UTILES
peru = peru.rename(columns={
                            "Marca":"MARCA",
                            "Descripción de Mercadería": "MODELO/VERSION",
                            "Cant. VF": "CANTIDAD",
                            "Código NCM": "DATOS PERSONALES",
                            "Fecha": "FECHA DE IMPORTACION",
                            "País de Origen": "ORIGEN"})

peru["MERCADO"] = "PERU"
peru["MODELO"] = None
peru["TIPO_VEHICULO"] = None
peru["SEGMENTO.1"] = None
peru["CARROCERIA"] = None
peru["AÑO"] = None
peru["CHASIS"] = None
peru["NUMERO MOTOR"] = None
peru["TRACCION"] = None
peru["CILINDRADA"] = None
peru["MOTOR"] = None
peru["COMBUSTIBLE"] = None
peru["TRANSMISION"] = None
peru["VERSION"] = None


columnasutiles = [
                  "MERCADO",
                  "TIPO_VEHICULO",
                  "SEGMENTO.1",
                  "MARCA",
                  "MODELO",
                  "MODELO/VERSION",
                  "VERSION",
                  "AÑO",
                  "ORIGEN",
                  "CARROCERIA",
                  "CHASIS",
                  "NUMERO MOTOR",
                  "COMBUSTIBLE",
                  "TRACCION",
                  "CILINDRADA",
                  "TRANSMISION",
                  "MOTOR",
                  "CANTIDAD",
                  "FECHA DE IMPORTACION",
                  "DATOS PERSONALES"
                  ]

peru = peru[columnasutiles]


# %%
peru["MODELO/VERSION"] = peru["MODELO/VERSION"].str.upper()


# %% FECHA DE IMPORTACION
peru["FECHA DE IMPORTACION"] = pd.to_datetime(peru["FECHA DE IMPORTACION"]).dt.year


# %% MARCAS
peru = marca(peru)
peru = corregirmarca(peru, columnasutiles)



# %% MODELO
# MODELOS LISTOS, SOLO QUEDA SEGUIR ACTUALIZANDO DICCIONARIO
peru = especifico2(peru, columnasutiles)
peru = corregirmodelo(peru)


# %% MODELO URGENCIA
condicion = peru["MODELO"].isna()
peru.loc[condicion, "MODELO1"] = peru.loc[condicion, "MODELO/VERSION"].str.extract(r"MODELO\s?:\s?(.+?)[\s,]")[0]
peru.loc[condicion, "MODELO2"] = peru.loc[condicion, "MODELO/VERSION"].str.extract(r"Modelo\s?:\s?(.+?)[\s,]")[0]
peru.loc[condicion, "MODELO3"] = peru.loc[condicion, "MODELO/VERSION"].str.extract(r",MOD\s?:\s?(.+?)[\s,]")[0]

peru.loc[peru["MODELO"].isna(),"MODELO"] = peru["MODELO1"]
peru.loc[peru["MODELO"].isna(),"MODELO"] = peru["MODELO2"]
peru.loc[peru["MODELO"].isna(),"MODELO"] = peru["MODELO3"]

peru = peru[columnasutiles]

peru["MODELO"] = peru["MODELO"].str.strip()


# %% SEGEMNTACION
peru = segmentacion(peru, columnasutiles)

# %% MODELO GENERICO
costa_rica = modelogenerico(peru)


# %% VERSION UGENCIA
condicion = peru["VERSION"].isna()
peru.loc[condicion, "VERSION"] = peru.loc[condicion, "MODELO/VERSION"].str.extract(r"VE\s?:\s?(.+?)[\s,]")[0]
condicion = None


# %% TIPO_VEHICULO URGENCIA
regex = r"(TRIMOVIL|PANEL VAN|TRACTO CAMION|TRACTOR|TRIMOTO|CAMIONETA|REMOLCADOR|BUS|AUTOMOVIL|MOTOCICLETA|MOTOCULTOR|MOTOCUCLTOR|MOTO CULTIVADORA|CULTIVADOR|TRATOR|REMOVEDOR DE TIERRA|CMTA|CAMION)"
condicion = peru["TIPO_VEHICULO"].isna()
peru.loc[condicion, "TIPO_VEHICULO"] = peru.loc[condicion, "MODELO/VERSION"].str.extract(regex)[0]


condicion = peru["TIPO_VEHICULO"] == "AUTOMOVIL"
peru.loc[condicion, "TIPO_VEHICULO"] = "AUTO"
condicion = peru["TIPO_VEHICULO"] == "TRATO"
peru.loc[condicion, "TIPO_VEHICULO"] = "TRACTOR"
condicion = peru["TIPO_VEHICULO"] == "MOTOCUCLTOR"
peru.loc[condicion, "TIPO_VEHICULO"] = "MOTOCULTOR"
condicion = peru["TIPO_VEHICULO"] == "CMTA"
peru.loc[condicion, "TIPO_VEHICULO"] = "CAMIONETA"
condicion = peru["TIPO_VEHICULO"] == "SUV"
peru.loc[condicion, "SEGEMTNO.1"] = "SUV"
peru.loc[condicion, "TIPO_VEHICULO"] = "AUTO"
condicion = peru["TIPO_VEHICULO"] == "MOTOCULTOR"
peru.loc[condicion, "TIPO_VEHICULO"] = "TRACTOR"
condicion = peru["TIPO_VEHICULO"] == "REMOLCADOR"
peru.loc[condicion, "TIPO_VEHICULO"] = "CAMION"
condicion = peru["TIPO_VEHICULO"] == "CAMIONETA"
peru.loc[condicion, "TIPO_VEHICULO"] = "PANEL VAN"
condicion = peru["TIPO_VEHICULO"] == "TRIMOVIL"
peru.loc[condicion, "TIPO_VEHICULO"] = "TRIMOTO"


# %% SEGMENTO.1 URGENCIA
condicion = peru["TIPO_VEHICULO"] == "PANEL VAN"
peru.loc[condicion, "SEGMENTO.1"] = "LIGERO"
condicion = peru["TIPO_VEHICULO"] == "CAMION"
peru.loc[condicion, "SEGMENTO.1"] = "PESADO"
condicion = peru["TIPO_VEHICULO"] == "TRACTOR"
peru.loc[condicion, "SEGMENTO.1"] = "PESADO"


# %% CARROCERIA URGENCIA
regex = r"(BARANDA|MULTIPROPOSITO|CONVERTIBLE|PICK UP|PICKUP|SEDAN|COUPE|STATION WAGON|HATCHBACK|HATCH BACK|SUV)"
condicion = peru["CARROCERIA"].isna()
peru.loc[condicion, "CARROCERIA"] = peru.loc[condicion, "MODELO/VERSION"].str.extract(regex)[0]
regex = None


# %% COMBUSTIBLE
peru["COMBUSTIBLE"] = peru["MODELO/VERSION"].str.extract(r"(DIESEL|GASOLINA|ENCENDIDO POR CHISPA)")[0]

condicion = None
condicion = peru["COMBUSTIBLE"] == "ENCENDIDO POR CHISPA"
peru.loc[condicion, "COMBUSTIBLE"] = "GASOLINA"


# %% AÑOS
# EXTRAER DE MODELO/VERSION
condicion = peru["AÑO"].isna()
peru.loc[condicion, "AÑO"] = peru.loc[condicion, "MODELO/VERSION"].str.extract(r"FABR?\.*\s*:\s*(\d{4})")[0]
peru.loc[condicion, "AÑO"] = peru.loc[condicion, "MODELO/VERSION"].str.extract(r"AÃO\s?:\s?(\d{4})")[0]
peru.loc[condicion, "AÑO"] = peru.loc[condicion, "MODELO/VERSION"].str.extract(r"AÃÂO\s?:\s?(\d{4})")[0]
peru.loc[condicion, "AÑO"] = peru.loc[condicion, "MODELO/VERSION"].str.extract(r"Fabr\.*\s?:\s?(\d{4})")[0]
peru.loc[condicion, "AÑO"] = peru.loc[condicion, "MODELO/VERSION"].str.extract(r"AÂ¤o\.*\s?:\s?(\d{4})")[0]
peru.loc[condicion, "AÑO"] = peru.loc[condicion, "MODELO/VERSION"].str.extract(r"/?(\d{4})")[0]


# FORMATO DE NUMERO
peru["AÑO"] = peru["AÑO"].fillna("1")
peru["AÑO"] = peru["AÑO"].astype("int64")

# AÑOS COHERENTES
condicion = peru["AÑO"] < 1975
condicion2 = peru["AÑO"] > 2020

peru.loc[condicion|condicion2, "AÑO"] = None

peru = quitardecimal(peru)

# nan en años
condicion = peru["AÑO"] == "nan"
peru.loc[condicion, "AÑO"] = None



# %% CHASIS
peru["CHASIS1"] = peru["MODELO/VERSION"].str.extract(r"CHA?S?I?S?\/?V?I?N?\s?:\s?(.{17})")
peru["CHASIS2"] = peru["MODELO/VERSION"].str.extract(r"VI?N?\s?:\s?(.{17})")
peru["CHASIS3"] = peru["MODELO/VERSION"].str.extract(r"VIN NÂº?°?\s?:\s?(.{17})")
condicion1 = peru["CHASIS1"].notna()
condicion2 = peru["CHASIS2"].notna()
condicion3 = peru["CHASIS3"].notna()
peru.loc[condicion1, "CHASIS"] = peru["CHASIS1"]
peru.loc[condicion2, "CHASIS"] = peru["CHASIS2"]
peru.loc[condicion3, "CHASIS"] = peru["CHASIS3"]
condicion1 = None
condicion2 = None
condicion3 = None
peru = peru[columnasutiles]


# %%
peru["MOTOR1"] = peru["MODELO/VERSION"].str.extract(r"MOTOR\s?NÃÂ°:?\s?(.+?)[\s,]")
peru["MOTOR2"] = peru["MODELO/VERSION"].str.extract(r"MOTOR:?\s?(.+?)[\s,]")
peru["MOTOR3"] = peru["MODELO/VERSION"].str.extract(r"MO:\s?(.+?)[\s,]")
peru["MOTOR4"] = peru["MODELO/VERSION"].str.extract(r"MOT:\s?(.+?)[\s,]")
condicion1 = peru["MOTOR1"].notna()
condicion2 = peru["MOTOR2"].notna()
condicion3 = peru["MOTOR3"].notna()
condicion4 = peru["MOTOR4"].notna()
peru.loc[condicion1, "NUMERO MOTOR"] = peru["MOTOR1"]
peru.loc[condicion2, "NUMERO MOTOR"] = peru["MOTOR2"]
peru.loc[condicion3, "NUMERO MOTOR"] = peru["MOTOR3"]
peru.loc[condicion4, "NUMERO MOTOR"] = peru["MOTOR4"]
condicion1 = None
condicion2 = None
condicion3 = None
condicion4 = None
peru = peru[columnasutiles]


# %%
peru = traccion(peru)



# %%
peru = cilindrada(peru, columnasutiles)


# %%
peru = motor(peru)


# %%
peru["TRANSMISION"] = peru["MODELO/VERSION"].str.extract(r"(AUTOMATICO|MECANICO|TT:MEC)")[0]
condicion = peru["TRANSMISION"] == "TT:MEC"
peru.loc[condicion, "TRANSMISION"] = "MECANICO"


# %%




# %%
peru.to_csv(r"D:\Basededatos\Limpioparaunir\peru04-07.csv", index=False)


# %%
peru = peru.rename(columns={
                            "MODELO/VERSION":"DESCRIPCION COMERCIAL 1"})

peru.to_csv(r"D:\Basededatos\Limpioparaentregar\peru\peru04-07original.csv", index=False)

# %%
