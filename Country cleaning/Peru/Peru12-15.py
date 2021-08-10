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
# UBICACION
path = r'D:\Basededatos\Origen\Peru\2012-2015'
os.chdir(path)
files = os.listdir(path)
files


# %%
# UNIR EN UN DATAFRAME INNER O OUTER SEGUN USE COLUMNAS DE BASE O NO
files_xls = [f for f in files if f[-3:] == 'csv']
files_xls
columnas = []
peru = pd.DataFrame(columns=columnas)
for f in files_xls:
    data = pd.read_csv(f)
    peru = pd.concat([peru , data], ignore_index=True, join='outer')


# %% COLUMNAS A RELLENAR
peru["MERCADO"] = "PERU"
peru["MODELO"] = None
peru["TIPO_VEHICULO"] = None
peru["SEGMENTO.1"] = None
peru["CARROCERIA"] = None
peru["CHASIS"] = None
peru["NUMERO MOTOR"] = None
peru["TRACCION"] = None
peru["CILINDRADA"] = None
peru["MOTOR"] = None
peru["COMBUSTIBLE"] = None
peru["TRANSMISION"] = None
peru["MARCA"] = None
peru["VERSION"] = None

columnasutiles = list(peru.columns)
peru = peru[columnasutiles]


# %% TRABAJAR SOLO EN MAYUS Y ARREGLOS GENERALES
peru["DESCRIPCION COMERCIAL 1"] = peru["DESCRIPCION COMERCIAL 1"].str.upper()
peru["DESCRIPCION COMERCIAL 2"] = peru["DESCRIPCION COMERCIAL 2"].str.upper()
peru["DESCRIPCION COMERCIAL 3"] = peru["DESCRIPCION COMERCIAL 3"].str.upper()
peru["DESCRIPCION COMERCIAL 4"] = peru["DESCRIPCION COMERCIAL 4"].str.upper()
peru["DESCRIPCION COMERCIAL 5"] = peru["DESCRIPCION COMERCIAL 5"].str.upper()
peru["ORIGEN"] = peru["ORIGEN"].str.upper()
condicion = peru["CANTIDAD"].isna()
peru.loc[condicion, "CANTIDAD"] = 1
condicion = None


# %% MARCAS
# UNICA COLUMNA CON MARCAS
peru = marca(peru, columnaorigen="DESCRIPCION COMERCIAL 1")
peru = corregirmarca(peru, columnasutiles)


# %% MODELO
# MODELOS LISTOS, SOLO QUEDA SEGUIR ACTUALIZANDO DICCIONARIO
peru = especifico2(peru, columnasutiles, columnaorigen="DESCRIPCION COMERCIAL 1")
peru = corregirmodelo(peru)



# %% MODELO URGENCIA
condicion = peru["MODELO"].isna()
peru.loc[condicion, "MODELO1"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 1"].str.extract(r"MODELO\s?:\s?(.+?)[\s,]")[0]
peru.loc[condicion, "MODELO2"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 1"].str.extract(r"Modelo\s?:\s?(.+?)[\s,]")[0]
peru.loc[condicion, "MODELO3"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 1"].str.extract(r",MOD\s?:\s?(.+?)[\s,]")[0]

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
peru.loc[condicion, "VERSION"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 1"].str.extract(r"VE\s?:\s?(.+?)[\s,]")[0]
condicion = None


# %% TIPO_VEHICULO URGENCIA 1063544 SIN TRACTO CAMION Y CULTIVADORA
regex = r"(TRIMOVIL|PANEL VAN|TRACTO CAMION|TRACTOR|TRIMOTO|CAMIONETA|REMOLCADOR|BUS|AUTOMOVIL|MOTOCICLETA|MOTOCULTOR|MOTOCUCLTOR|MOTO CULTIVADORA|CULTIVADOR|TRATOR|REMOVEDOR DE TIERRA|CMTA|CAMION)"
condicion = None
condicion = peru["TIPO_VEHICULO"].isna()
peru.loc[condicion, "TIPO_VEHICULO"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 1"].str.extract(regex)[0]
condicion = None
condicion = peru["TIPO_VEHICULO"].isna()
peru.loc[condicion, "TIPO_VEHICULO"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 2"].str.extract(regex)[0]
condicion = None
condicion = peru["TIPO_VEHICULO"].isna()
peru.loc[condicion, "TIPO_VEHICULO"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 3"].str.extract(regex)[0]
condicion = None
condicion = peru["TIPO_VEHICULO"].isna()
peru.loc[condicion, "TIPO_VEHICULO"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 4"].str.extract(regex)[0]
condicion = None
condicion = peru["TIPO_VEHICULO"].isna()
peru.loc[condicion, "TIPO_VEHICULO"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 5"].str.extract(regex)[0]
regex = None

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
condicion = None
condicion = peru["CARROCERIA"].isna()
peru.loc[condicion, "CARROCERIA"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 1"].str.extract(regex)[0]
condicion = None
condicion = peru["CARROCERIA"].isna()
peru.loc[condicion, "CARROCERIA"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 2"].str.extract(regex)[0]
condicion = None
condicion = peru["CARROCERIA"].isna()
peru.loc[condicion, "CARROCERIA"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 3"].str.extract(regex)[0]
condicion = None
condicion = peru["CARROCERIA"].isna()
peru.loc[condicion, "CARROCERIA"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 4"].str.extract(regex)[0]
condicion = None
condicion = peru["CARROCERIA"].isna()
peru.loc[condicion, "CARROCERIA"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 5"].str.extract(regex)[0]
condicion = None
condicion = peru["CARROCERIA"] == "PICK UP"
peru.loc[condicion, "CARROCERIA"] = "PICKUP"


# %% COMBUSTIBLE
# EN MULTIPLES COLUMNAS
# LA CONDICION None reptida es porque si tiene el mismo codigo pandas me lo guarda en el cache y no vuelve a buscar
condicion = peru["COMBUSTIBLE"].isna()
peru.loc[condicion, "COMBUSTIBLE"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 2"].str.extract(r"(DIESEL|GASOLINA|ENCENDIDO POR CHISPA)")[0]
condicion = None
condicion = peru["COMBUSTIBLE"].isna()
peru.loc[condicion, "COMBUSTIBLE"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 3"].str.extract(r"(DIESEL|GASOLINA|ENCENDIDO POR CHISPA)")[0]
condicion = None
condicion = peru["COMBUSTIBLE"].isna()
peru.loc[condicion, "COMBUSTIBLE"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 4"].str.extract(r"(DIESEL|GASOLINA|ENCENDIDO POR CHISPA)")[0]
condicion = None
condicion = peru["COMBUSTIBLE"].isna()
peru.loc[condicion, "COMBUSTIBLE"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 5"].str.extract(r"(DIESEL|GASOLINA|ENCENDIDO POR CHISPA)")[0]

condicion = None
condicion = peru["COMBUSTIBLE"] == "ENCENDIDO POR CHISPA"
peru.loc[condicion, "COMBUSTIBLE"] = "GASOLINA"


# %% AÑOS
# EXTRAER DE MODELO/VERSION
condicion = peru["AÑO DE FABRICACION"].isna()
peru.loc[condicion, "AÑO DE FABRICACION"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 1"].str.extract(r"FABR?\.*\s*:\s*(\d{4})")[0]
condicion = peru["AÑO DE FABRICACION"].isna()
peru.loc[condicion, "AÑO DE FABRICACION"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 1"].str.extract(r"AÃO\s?:\s?(\d{4})")[0]
condicion = peru["AÑO DE FABRICACION"].isna()
peru.loc[condicion, "AÑO DE FABRICACION"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 1"].str.extract(r"AÃÂO\s?:\s?(\d{4})")[0]
condicion = peru["AÑO DE FABRICACION"].isna()
peru.loc[condicion, "AÑO DE FABRICACION"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 1"].str.extract(r"Fabr\.*\s?:\s?(\d{4})")[0]
condicion = peru["AÑO DE FABRICACION"].isna()
peru.loc[condicion, "AÑO DE FABRICACION"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 1"].str.extract(r"AÂ¤o\.*\s?:\s?(\d{4})")[0]
condicion = peru["AÑO DE FABRICACION"].isna()
peru.loc[condicion, "AÑO DE FABRICACION"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 1"].str.extract(r"AÑO\.*\s?:\s?(\d{4})")[0]
condicion = peru["AÑO DE FABRICACION"].isna()
peru.loc[condicion, "AÑO DE FABRICACION"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 1"].str.extract(r"/?(\d{4})")[0]


condicion = peru["AÑO DE FABRICACION"].str.isnumeric() == False
condicion.fillna(False, inplace=True)
peru.loc[condicion, "AÑO DE FABRICACION"] = None
condicion = None

# FORMATO DE NUMERO
peru["AÑO DE FABRICACION"] = peru["AÑO DE FABRICACION"].fillna("1")
peru["AÑO DE FABRICACION"] = peru["AÑO DE FABRICACION"].astype("int64")

# AÑOS COHERENTES
condicion = peru["AÑO DE FABRICACION"] < 1975
condicion2 = peru["AÑO DE FABRICACION"] > 2020

peru.loc[condicion|condicion2, "AÑO DE FABRICACION"] = None

peru = quitardecimal(peru, columna="AÑO DE FABRICACION")

# nan en años
condicion = peru["AÑO DE FABRICACION"] == "nan"
peru.loc[condicion, "AÑO DE FABRICACION"] = None


# %% CHASIS NUEVO
condicion = peru["CHASIS"].isna()
peru.loc[condicion, "CHASIS"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 2"].str.extract(r"CHA?S?I?S?\/?V?I?N?\s?:\s?(.{17})")[0]
condicion = None
condicion = peru["CHASIS"].isna()
peru.loc[condicion, "CHASIS"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 3"].str.extract(r"CHA?S?I?S?\/?V?I?N?\s?:\s?(.{17})")[0]
condicion = None
condicion = peru["CHASIS"].isna()
peru.loc[condicion, "CHASIS"] = peru.loc[condicion, "DESCRIPCION COMERCIAL 4"].str.extract(r"CHA?S?I?S?\/?V?I?N?\s?:\s?(.{17})")[0]


# %% NUMERO MOTOR
peru["MOTOR1"] = peru["DESCRIPCION COMERCIAL 2"].str.extract(r"MOTOR\s?NÃÂ°:?\s?(.+?)[\s,]")
peru["MOTOR2"] = peru["DESCRIPCION COMERCIAL 2"].str.extract(r"MOTOR:?\s?(.+?)[\s,]")
peru["MOTOR3"] = peru["DESCRIPCION COMERCIAL 2"].str.extract(r"MOT?:\s?(.+?)[\s,]")
peru["MOTOR4"] = peru["DESCRIPCION COMERCIAL 3"].str.extract(r"MOTOR\s?NÃÂ°:?\s?(.+?)[\s,]")
peru["MOTOR5"] = peru["DESCRIPCION COMERCIAL 3"].str.extract(r"MOTOR:?\s?(.+?)[\s,]")
peru["MOTOR6"] = peru["DESCRIPCION COMERCIAL 3"].str.extract(r"MOT?:\s?(.+?)[\s,]")
peru["MOTOR7"] = peru["DESCRIPCION COMERCIAL 4"].str.extract(r"MOTOR\s?NÃÂ°:?\s?(.+?)[\s,]")
peru["MOTOR8"] = peru["DESCRIPCION COMERCIAL 4"].str.extract(r"MOTOR:?\s?(.+?)[\s,]")
peru["MOTOR9"] = peru["DESCRIPCION COMERCIAL 4"].str.extract(r"MOT?:\s?(.+?)[\s,]")

condicion1 = peru["MOTOR1"].notna()
condicion2 = peru["MOTOR2"].notna()
condicion3 = peru["MOTOR3"].notna()
condicion4 = peru["MOTOR4"].notna()
condicion5 = peru["MOTOR5"].notna()
condicion6 = peru["MOTOR6"].notna()
condicion7 = peru["MOTOR7"].notna()
condicion8 = peru["MOTOR8"].notna()
condicion9 = peru["MOTOR9"].notna()

peru.loc[condicion1, "NUMERO MOTOR"] = peru["MOTOR1"]
peru.loc[condicion2, "NUMERO MOTOR"] = peru["MOTOR2"]
peru.loc[condicion3, "NUMERO MOTOR"] = peru["MOTOR3"]
peru.loc[condicion4, "NUMERO MOTOR"] = peru["MOTOR4"]
peru.loc[condicion5, "NUMERO MOTOR"] = peru["MOTOR5"]
peru.loc[condicion6, "NUMERO MOTOR"] = peru["MOTOR6"]
peru.loc[condicion7, "NUMERO MOTOR"] = peru["MOTOR7"]
peru.loc[condicion8, "NUMERO MOTOR"] = peru["MOTOR8"]
peru.loc[condicion9, "NUMERO MOTOR"] = peru["MOTOR9"]
condicion1 = None
condicion2 = None
condicion3 = None
condicion4 = None
condicion5 = None
condicion6 = None
condicion7 = None
condicion8 = None
condicion9 = None
peru = peru[columnasutiles]


# %% TRACCION
condicion = peru["TRACCION"].isna()
peru[condicion] = traccion(peru[condicion], columnaorigen="DESCRIPCION COMERCIAL 2")
condicion = peru["TRACCION"].isna()
peru[condicion] = traccion(peru[condicion], columnaorigen="DESCRIPCION COMERCIAL 3")
condicion = peru["TRACCION"].isna()
peru[condicion] = traccion(peru[condicion], columnaorigen="DESCRIPCION COMERCIAL 4")


# %% CILINDRADA
condicion = None
condicion = peru["CILINDRADA"].isna()
peru[condicion] = cilindrada(peru[condicion], columnasutiles, columnaorigen="DESCRIPCION COMERCIAL 2")
condicion = None
condicion = peru["CILINDRADA"].isna()
peru[condicion] = cilindrada(peru[condicion], columnasutiles, columnaorigen="DESCRIPCION COMERCIAL 3")
condicion = None
condicion = peru["CILINDRADA"].isna()
peru[condicion] = cilindrada(peru[condicion], columnasutiles, columnaorigen="DESCRIPCION COMERCIAL 4")




# %% VERSION DEL MOTOR n.n
condicion = None
condicion = peru["MOTOR"].isna()
peru[condicion] = motor(peru[condicion], columnamodelo="DESCRIPCION COMERCIAL 1")
condicion = None
condicion = peru["MOTOR"].isna()
peru[condicion] = motor(peru[condicion], columnamodelo="DESCRIPCION COMERCIAL 2")
condicion = None
condicion = peru["MOTOR"].isna()
peru[condicion] = motor(peru[condicion], columnamodelo="DESCRIPCION COMERCIAL 3")
condicion = None
condicion = peru["MOTOR"].isna()
peru[condicion] = motor(peru[condicion], columnamodelo="DESCRIPCION COMERCIAL 4")


# %% TRANSMISION
peru["TRANSMISION"] = peru["DESCRIPCION COMERCIAL 2"].str.extract(r"(AUTOMATICO|MECANICO|TT:MEC)")[0]
condicion = peru["TRANSMISION"] == "TT:MEC"
peru.loc[condicion, "TRANSMISION"] = "MECANICO"


# %%
peru.to_csv(r"D:\Basededatos\Limpioparaentregar\peru\peru12-15original.csv", index=False)



# %% DEJARIA SOLO LA PRIMER DESCRIPCION COMO MODELO/VERSION
columnasutiles = list(peru.columns)
del columnasutiles[1:5]
peru = peru[columnasutiles]


# %%
peru.to_csv(r"D:\Basededatos\Limpioparaunir\peru12-15.csv", index=False)


# %%
peru.info(null_counts=True)


# %%
peru.head()
# %%
