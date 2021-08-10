# %%
import os
import pandas as pd
import numpy as np
import re
from scripts import versionfinal,versionurgencia,versionespecifico,identificacionmotor,motorseguncilindrada,corregirmarca, progreso, motor, quitardecimal, valores, modelogeneral, especifico, origensegunvin, version, modelogenerico, especifico2, corregirmodelo, segmentacion, cilindrada, traccion, marca


# %% CARGA DE DATOS
# PAIS - ORIGINALES
costa_rica = pd.read_csv(r"D:\Basededatos\Limpioparaentregar\costa_rica.csv")


# %% IDENTIFICACIONES MUY DISTINTAS AL ESTANDAR DE 17 CHARS
condicion = costa_rica["IDENTIFICACION DEL VEHICULO"].str.len() == 17
costa_rica = costa_rica[condicion]
condicion = None


# %% TRACCION ESTA DIVIDIDA EN Numero ejes y traccion, este script lo cambia como solucion rapida
costa_rica["NUEVATRACCION"] = None

regex = r"(\d\s?[\*xX]\s?\d)"

# EN LAS COLUMNAS QUE CORRESPONDE
condicion = costa_rica["NUEVATRACCION"].isna()
costa_rica.loc[condicion, "NUEVATRACCION"] = costa_rica["TRACCION"].str.extract(regex, expand=False)
condicion = costa_rica["NUEVATRACCION"].isna()
costa_rica.loc[condicion, "NUEVATRACCION"] = costa_rica["Número Ejes"].str.extract(regex, expand=False)


# EN LAS COLUMNAS DE ESTILO MODELO PARA VER QUE ONDA
condicion = costa_rica["NUEVATRACCION"].isna()
costa_rica.loc[condicion, "NUEVATRACCION"] = costa_rica["MODELO"].str.extract(regex, expand=False)
condicion = costa_rica["NUEVATRACCION"].isna()
costa_rica.loc[condicion, "NUEVATRACCION"] = costa_rica["ESTILO"].str.extract(regex, expand=False)


costa_rica["TRACCION"] = costa_rica["NUEVATRACCION"]


# %% MOTOR
costa_rica["MOTOR"] = None
costa_rica["MOTOR 1"] = None
costa_rica["MOTOR 2"] = None
costa_rica = motor(costa_rica, columnamodelo = 'MODELO', columnadestino = "MOTOR 1")
costa_rica = motor(costa_rica, columnamodelo = 'ESTILO', columnadestino = "MOTOR 2")


condicion = costa_rica["MOTOR"].isna()
condicion2 = costa_rica["MOTOR 1"].notna()
condicion3 = costa_rica["MOTOR 2"].notna()
costa_rica.loc[condicion & condicion2, "MOTOR"] = costa_rica.loc[condicion & condicion2, "MOTOR 1"]
costa_rica.loc[condicion & condicion3, "MOTOR"] = costa_rica.loc[condicion & condicion3, "MOTOR 2"]
condicion = None
condicion2 = None
condicion3 = None


# %% Versiones y tipo de vehiculos mezclado entre modelo y version
costa_rica["VERSION"] = None

# CAMBIO
condicion = costa_rica["ESTILO"].isin(["FR 70 GY -3","OF","DEPORTIVA", "MONTANERA","ZS1257"])
costa_rica.loc[condicion, "ESTILO"] = costa_rica.loc[condicion, "MODELO"]
costa_rica.loc[condicion, "MODELO"] = None
condicion = None

condicion = costa_rica["ESTILO"] == "MAXIM"
costa_rica.loc[condicion, "ESTILO"] = "XJ650"
costa_rica.loc[condicion, "VERSION"] = "MAXIM"
condicion = None

# VERSIONES EN MODELO

# VERSIONES
listaversion = ["CROSS MONTAÑERA","PICKUP","PICK UP","STATION WAGON","FAMILIAR","TURISMO","CLASICO","GRANDSALOOM","GRANDSALOON","GRAND SALOON","H 100","SVX","BERLINA","TRX500FA1","KLF300-B14", "PTCYB", "ESTANDARD","ESTANDAR","STD", "GLS", "GL", "EX", "XE", "LX", "DX", "BASE", "SE", "S", "GXE", "LS", "L", "J210LG-GMDF","JX", "KDJ150L-GKAEY", "JB424", "NCP93L-BEMRK", "SEDAN", "XLT", "LE", "CE", "0", "LIMITED", "XLS"]

# EN MODELO - Si esta en modelo llevar a version y borrar
condicion = costa_rica["MODELO"].isin(listaversion)
costa_rica.loc[condicion, "VERSION"] = costa_rica.loc[condicion, "MODELO"]
costa_rica.loc[condicion, "MODELO"] = None
condicion = None

# EN ESTILO - Si esta en estilo llevar a version y traer modelo
condicion = costa_rica["ESTILO"].isin(listaversion)
costa_rica.loc[condicion, "VERSION"] = costa_rica.loc[condicion, "ESTILO"]
costa_rica.loc[condicion, "ESTILO"] = costa_rica.loc[condicion, "MODELO"]
condicion = None

# TIPO 
costa_rica["TIPO_VEHICULO"] = None
listatipo = ["TRIMOTO","TRICICLO","SCOOTER","MOTOCICLETA","CAMION","TRACTOR", "CABEZAL", "MOTOCULTOR"]

# EN ESTILO
condicion = costa_rica["ESTILO"].isin(listatipo)
costa_rica.loc[condicion, "TIPO_VEHICULO"] = costa_rica.loc[condicion, "ESTILO"]
costa_rica.loc[condicion, "ESTILO"] = costa_rica.loc[condicion, "MODELO"]
condicion = None

#  EN MODELO
condicion = costa_rica["MODELO"].isin(listatipo)
costa_rica.loc[condicion, "TIPO_VEHICULO"] = costa_rica.loc[condicion, "MODELO"]
costa_rica.loc[condicion, "MODELO"] = None


# MODELO FUERA DE LUGAR
condicion = costa_rica["MODELO"] != costa_rica["ESTILO"]
condicion2 = costa_rica["MODELO"] == "ZS 150-7"
costa_rica.loc[condicion & condicion2, "ESTILO"] = costa_rica.loc[condicion & condicion2, "MODELO"]


# DEJO MODELO COMO VERSION
condicion = costa_rica["MODELO"] == costa_rica["ESTILO"]
costa_rica.loc[condicion,"MODELO"] = None

condicion = costa_rica["MODELO"].notna()
condicion2 = costa_rica["VERSION"].isna()
costa_rica.loc[condicion & condicion2, "VERSION"] = costa_rica.loc[condicion & condicion2, "MODELO"]


# %% COLUMNAS UTILES
costa_rica["MERCADO"] = "COSTA RICA"
costa_rica["CANTIDAD"] = 1

costa_rica.rename(columns={
                "IDENTIFICACION DEL VEHICULO": "NUMERO CHASIS / VIN",
                "CODIGO MARCA": "MARCA",
                'Posición Cilindros': "DISPOSICION CILINDROS",
                'Número Motor': 'NUMERO MOTOR',
                'ESTILO': 'MODELO/VERSION',
                'CILINDRAJE': 'CILINDRADA',
                'AÑO MODELO': 'AÑO'
                },
                inplace=True)

costa_rica["SEGMENTO.1"] = None
costa_rica["MODELO"] = None
costa_rica["ORIGEN"] = None
costa_rica["MODELO GENERICO"] = None
costa_rica["CARROCERIA"] = None
costa_rica["IDENTIFICACION MOTOR"] = None

columnasutiles = ["MERCADO",
                  "TIPO_VEHICULO",
                  "SEGMENTO.1",
                  "MARCA",
                  "MODELO GENERICO",
                  "MODELO",
                  "MODELO/VERSION",
                  "VERSION",
                  "AÑO",
                  "ORIGEN",
                  "MOTOR",
                  "IDENTIFICACION MOTOR",
                  "CARROCERIA",
                  "CILINDRADA",
                  "CILINDROS",
                  "DISPOSICION CILINDROS",
                  "TRANSMISION",
                  "TRACCION",
                  "NUMERO CHASIS / VIN",
                  "NUMERO MOTOR",
                  "PARTIDA_AR",
                  "CANTIDAD"
                  ]
costa_rica = costa_rica[columnasutiles]


# %% ORIGEN SEGUN VIN
costa_rica = origensegunvin(costa_rica)


# %% FILTRAR MODELO/VERSION
listaproblema = ["SIN EMBLEMA",
                 "SIN EMBLEMAS",
                 "NO TIENE",
                 "SIN ENBLEMAS",
                 "S/EMBLEMA",
                 "MOTOCICLETA",
                 "RURAL",
                 ]

condicion = costa_rica["MODELO/VERSION"].isin(listaproblema)
costa_rica.loc[condicion, "MODELO/VERSION"] = None


# %% CORREGIR MARCAS
costa_rica = corregirmarca(costa_rica, columnasutiles)


# %% MODELO
costa_rica["MODELO/VERSION"] = costa_rica["MODELO/VERSION"].astype(str).str.strip()
costa_rica = especifico2(costa_rica, columnasutiles, columnaorigen="MODELO/VERSION", columnadestino = "MODELO")
costa_rica = versionfinal(costa_rica)
costa_rica = corregirmodelo(costa_rica, columnasutiles)
costa_rica = segmentacion(costa_rica, columnasutiles)


# %% MODELO GENERICO
costa_rica = modelogenerico(costa_rica)


# %% FORMATO GENERAL
costa_rica["ORIGEN"] = costa_rica["ORIGEN"].str.upper()


costa_rica = quitardecimal(costa_rica, "CANTIDAD")

condicion = costa_rica["MERCADO"].notna()
costa_rica = costa_rica[condicion]


# %%
condicion = costa_rica["CILINDRADA"].isna()
costa_rica.loc[condicion, "CILINDRADA"] = 0

condicion = costa_rica["CILINDRADA"].isnull()
costa_rica.loc[condicion, "CILINDRADA"] = 0




costa_rica["CILINDRADA"]=costa_rica["CILINDRADA"].str.replace('C.C','')
costa_rica["CILINDRADA"]=costa_rica["CILINDRADA"].str.replace('CC','')
costa_rica["CILINDRADA"]=costa_rica["CILINDRADA"].str.replace('C.C.','')
costa_rica["CILINDRADA"]=costa_rica["CILINDRADA"].str.replace('ELECTRICO','')

costa_rica["CILINDRADA"] = costa_rica["CILINDRADA"].str.strip(to_strip="cC.,")

costa_rica["CILINDRADA"] = costa_rica["CILINDRADA"].str.strip()

condicion = costa_rica["CILINDRADA"].isnull()
costa_rica.loc[condicion, "CILINDRADA"] = 0

condicion = costa_rica["CILINDRADA"].str.isnumeric() == False
costa_rica.loc[condicion, "CILINDRADA"] = costa_rica.loc[condicion, "CILINDRADA"].str.replace(',', '.')

condicion = costa_rica["CILINDRADA"].str.isupper() == True
costa_rica.loc[condicion, "CILINDRADA"] = 0


condicion = costa_rica["CILINDRADA"].str.islower() == True
costa_rica.loc[condicion, "CILINDRADA"] = 0


condicion = costa_rica["CILINDRADA"].str.isnumeric() == False
costa_rica.loc[condicion, "CILINDRADA"] = 0

costa_rica["CILINDRADA"] = costa_rica["CILINDRADA"].astype(float)

# %%
costa_rica = motorseguncilindrada(costa_rica, columnasutiles)


# %%
costa_rica = identificacionmotor(costa_rica, columnasutiles)


# %% TUVE QUE AGREGAR 0's PARA PROCESAR, LOS VUELVO A DEJAR EN BLANCO PARA SQL
condicion = costa_rica["AÑO"] == 0
costa_rica.loc[condicion, "AÑO"] = None

condicion = costa_rica["CILINDRADA"] == 0
costa_rica.loc[condicion, "CILINDRADA"] = None

condicion = costa_rica["MOTOR"] == 0
costa_rica.loc[condicion, "MOTOR"] = None



# %%
costa_rica.to_csv(r'D:\Basededatos\Limpioparaunir\costa_rica.csv', index=False)


# %%
costa_rica.info()


# %%
