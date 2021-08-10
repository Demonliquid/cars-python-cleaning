# %%
import os
import pandas as pd
import numpy as np
import datetime
import xlrd
from scripts import motor, quitardecimal, valores, modelogeneral, especifico, origensegunvin, version, modelogenerico, especifico2, corregirmodelo, segmentacion, cilindrada, traccion, marca


# %% CARGA DE DATOS
# PROBLEMA: MISMO PAIS EN DISTINTOS ARCHIVOS

# MODELO
base = pd.read_csv(r'D:\Basededatos\esquema.csv')

# PAIS - ORIGINALES
costa_rica0 = pd.read_csv(r"D:\Basededatos\Origen\Costa Rica\SIA1.csv")
costa_rica1 = pd.read_csv(r"D:\Basededatos\Origen\Costa Rica\TICA1.csv")
costa_rica2 = pd.read_csv(r"D:\Basededatos\Origen\Costa Rica\SIA2.csv")
costa_rica3 = pd.read_csv(r"D:\Basededatos\Origen\Costa Rica\TICA2.csv")


# %% ARREGLAR COLUMNAS ORIGINALES
# PROBLEMA: UNO DE LOS ARCHIVOS TIENE COLUMNAS DIFERENTES
costa_rica1.rename(columns={
                'Identificación Vehículo': 'IDENTIFICACION DEL VEHICULO',
                'Marca vehículo': 'CODIGO MARCA',
                'cm cúbicos': 'CILINDRAJE',
                'TRACCION': 'TRACCION',
                'Modelo': 'MODELO',
                'Estilo': 'ESTILO',
                'año modelo': 'AÑO MODELO',
                'PARTIDA ARANCELARIA': 'PARTIDA_AR'
                },
                inplace=True)


costa_rica3.rename(columns={
                'Identificación Vehículo': 'IDENTIFICACION DEL VEHICULO',
                'Marca vehículo': 'CODIGO MARCA',
                'cm cúbicos': 'CILINDRAJE',
                'TRACCION': 'TRACCION',
                'Modelo': 'MODELO',
                'Estilo': 'ESTILO',
                'año modelo': 'AÑO MODELO',
                'PARTIDA ARANCELARIA': 'PARTIDA_AR'
                },
                inplace=True)

# ARREGLAR FORMATO
#costa_rica0['AÑO MODELO'].astype('object', copy=False)
#costa_rica0['PARTIDA_AR'].astype('object', copy=False)


#costa_rica1['AÑO MODELO'].astype('object', copy=False)
#costa_rica1['PARTIDA_AR'].astype('object', copy=False)


#costa_rica2['AÑO MODELO'].astype('object', copy=False)
#costa_rica2['PARTIDA_AR'].astype('object', copy=False)

#costa_rica3['AÑO MODELO'].astype('object', copy=False)
#costa_rica3['PARTIDA_AR'].astype('object', copy=False)


# %% UNIR ORIGINALES
costa_rica = pd.concat([costa_rica0, costa_rica1, costa_rica2, costa_rica3], ignore_index=True, join='outer')
costa_rica0 = None
costa_rica1 = None
costa_rica2 = None
costa_rica3 = None


# %%
costa_rica.drop_duplicates(subset=["IDENTIFICACION DEL VEHICULO"], inplace=True)


# %% COLUMNAS UTILES
costa_rica = costa_rica[["IDENTIFICACION DEL VEHICULO",
                        "CODIGO MARCA",
                        "TRANSMISION",
                        "TRACCION",
                        "Número Ejes",
                        "Posición Cilindros",
                        "Número Motor",
                        "MODELO",
                        "ESTILO",
                        "CILINDRAJE",
                        "CILINDROS",
                        "AÑO MODELO",
                        "PARTIDA_AR"]]


# %% LIMPIEZA GENERAL
# Tiene valores de puro espacio en Año
# Tiene algunos valores mezclados
filasconespacio = costa_rica[costa_rica["AÑO MODELO"].astype("str").str.isspace() == True]
costa_rica = costa_rica.drop(costa_rica[(costa_rica["AÑO MODELO"].astype("str").str.isspace())==True].index)
costa_rica = costa_rica.drop(costa_rica[(costa_rica["AÑO MODELO"].astype("str").str.isupper())==True].index)
filasconespacio["AÑO MODELO"] = 0
costa_rica = pd.concat([costa_rica, filasconespacio], ignore_index=True, join='outer')



# %%
for column in list(costa_rica.columns):
    costa_rica[column] = costa_rica[column].astype(str)
    costa_rica[column] = costa_rica[column].str.strip()


# %%  LIMPIAR MOTOR
costa_rica["Número Motor"] = costa_rica['Número Motor'].str.replace(" ","")
costa_rica["Número Motor"] = costa_rica['Número Motor'].str.replace("/","")
costa_rica["Número Motor"] = costa_rica['Número Motor'].str.replace(".","")
costa_rica["Número Motor"] = costa_rica['Número Motor'].str.replace("-","")
costa_rica["Número Motor"] = costa_rica['Número Motor'].str.replace("(","")
costa_rica["Número Motor"] = costa_rica['Número Motor'].str.replace(")","")
costa_rica["Número Motor"] = costa_rica['Número Motor'].str.replace(",","")
costa_rica["Número Motor"] = costa_rica['Número Motor'].str.replace("*","")


condicion = costa_rica["Número Motor"].str.isalpha() == True
costa_rica.loc[condicion, "Número Motor"] = None

condicion = costa_rica["Número Motor"] == ''
costa_rica.loc[condicion, "Número Motor"] = None

condicion = None


# %%
condicion = costa_rica["CODIGO MARCA"].str.isnumeric()
costa_rica = costa_rica[condicion]
condicion = None
costa_rica["CODIGO MARCA"] = costa_rica["CODIGO MARCA"].astype("float").map('{:.0f}'.format)


# %% ARREGLOS INICIALES
# POSICION DE CILINDROS Y NUMERO DE CILINDROS MEZCLADOS
numeroenposicion = costa_rica["Posición Cilindros"].astype(str).str.isupper() == False
costa_rica.loc[numeroenposicion,["Posición Cilindros", "CILINDROS"]] = costa_rica.loc[numeroenposicion,["CILINDROS", "Posición Cilindros"]].values
numeroenposicion = None


# HAY ALGUNOS VALORES NO ARANCELARIOS
condicion = costa_rica["PARTIDA_AR"].astype(str).str.isnumeric()
costa_rica = costa_rica[condicion]
condicion = None


# ARREGLAR TRANSMISION
costa_rica["TRANSMISION"].replace('M', 'MANUAL', inplace=True) 
costa_rica["TRANSMISION"].replace('A', 'AUTOMATICO', inplace=True) 



# %%
costa_rica.to_csv(r'D:\Basededatos\Limpioparaentregar\costa_rica.csv', index=False)



# %%
costa_rica.head()


# %%
