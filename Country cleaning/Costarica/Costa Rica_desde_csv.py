# %%
import os
import pandas as pd
import numpy as np
import datetime
import xlrd
from vininfo import Vin
from scripts import origensegunvin


# %% CARGA DE DATOS

# PAIS - ORIGINALES
costa_rica = pd.read_csv(r"F:\Bases de datos\Costa Rica\csv\costa_rica.csv")


# %%
costa_rica["ORIGEN"] = None

# %%
costa_rica.head()

# %%
costa_rica = origensegunvin(costa_rica, "IDENTIFICACION DEL VEHICULO")



# %% CAMBIAR POSICION DE CILINDROS - ARREGLAR
# PROBLEMA: CILINDROS TIENE QUE SER NUMEROS Y POSICION TIENE QUE SER LETRA
cambiarcilindroyposicion = costa_rica.loc[costa_rica["CILINDROS"].astype("str").str.isupper() == True]


# %%
costa_rica = costa_rica.drop(costa_rica[costa_rica["CILINDROS"].str.isalpha() == True].index)


# %%
cambiarcilindroyposicion.rename(columns={
                'CILINDROS': 'cilindros',
                'Posición Cilindros': 'CILINDROS',
                'cilindros': 'CILINDROS',
                },
                inplace=True)


# %% 
costa_rica = pd.concat([costa_rica, cambiarcilindroyposicion], join='outer')
costa_rica.drop(columns=['cilindros'], inplace=True)


# %% EQUIVALENCIAS
costa_rica["MERCADO"] = "COSTA RICA"
costa_rica["CANTIDAD"] = 1
costa_rica["TRANSMISION"].replace('M', 'MANUAL', inplace=True) 
costa_rica["TRANSMISION"].replace('A', 'AUTOMATICO', inplace=True) 
costa_rica["DISPOSICION CILINDROS"] =  costa_rica["Posición Cilindros"].astype("str") + costa_rica["CILINDROS"].astype("str")



costa_rica.rename(columns={
                'MODELO': 'MODELOAREVISAR',
                'CODIGO MARCA': 'MARCA',
                'ESTILO': 'MODELO',
                'Número Motor': 'NUMERO MOTOR',
                'AÑO MODELO': 'AÑO',
                'CILINDRAJE': 'CILINDRADA',
                'TRACCION': 'TRACCION'
                },
                inplace=True)


# %%
costa_rica["CILINDRADA"].replace('nan', None, inplace=True)
costa_rica["CILINDRADA"].replace('NaN', None, inplace=True)

# %%
costa_rica["CILINDRADA"] = costa_rica["CILINDRADA"].astype("float").map('{:.0f}'.format)

# %%
costa_rica["AÑO"] = costa_rica["AÑO"].astype(int)
costa_rica["AÑO"] = costa_rica["AÑO"].astype(str)


# %% AGREGAR MARCAS
marcas = pd.read_excel(r'D:\Basededatos\Origen\Costa Rica\Codigo Marca Costa Rica.xlsx', engine='openpyxl' )


# %%
costa_rica = pd.merge(
    costa_rica,
    marcas[['MARCA', 'Nombre de marca']],
    on='MARCA'
    )


# %%
costa_rica.rename(columns={
                'MARCA': 'CODIGO DE MARCA',
                'Nombre de marca': 'MARCA',
                },
                inplace=True)


# %%




# %% GENERAR ORIGEN SEGUN VIN
costa_ricaconvin["ORIGEN"] = costa_ricaconvin["IDENTIFICACION DEL VEHICULO"].map(lambda x: Vin(x).country)
costa_ricaconvin['ORIGEN'].replace('China (Mainland)', 'China', inplace=True)
costa_ricaconvin['ORIGEN'].replace('Taiwan, China', 'China', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"Cote d'Ivoire", 'Costa de Marfil', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"Germany/West Germany", 'Alemania', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"Korea (South)", 'Corea del Sur', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"Saudi Arabia", 'Arabia Saudita', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"United Kingdom", 'Reino Unido', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"Italy", 'Italia', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"Greece", 'Grecia', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"Belgium", 'Belgica', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"Luxembourg", 'Luxemburgo', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"United States", 'Estados Unidos', inplace=True)
costa_ricasinvin = pd.concat([costa_rica, costa_ricaconvin]).drop_duplicates(keep=False)
costa_rica = pd.concat([costa_ricaconvin, costa_ricasinvin])


# %%
columnasutiles = [
                  "IDENTIFICACION DEL VEHICULO",
                  "MERCADO",
                  "MARCA",
                  "MODELO",
                  "DISPOSICION CILINDROS",
                  "CILINDRADA",
                  "CILINDROS",
                  "TRACCION",
                  "TRANSMISION",
                  "AÑO",
                  "CANTIDAD",
                  "NUMERO MOTOR",
                  "ORIGEN",
                  "PARTIDA_AR"]


costa_rica = costa_rica[columnasutiles]


# %%
costa_rica.rename(columns={"MODELO": "MODELO/VERSION", "IDENTIFICACION DEL VEHICULO": "NUMERO CHASIS / VIN"}, inplace=True)
new = costa_rica["MODELO/VERSION"].str.split(" ", n = 1, expand = True)
costa_rica["MODELO"] = new[0]


# %%
costa_rica["SEGMENTO.1"] = None
listamarca = r'''(HINO|ISUZU|MITSUBISHI|MACK|VOLVO|INTERNATIONAL|FREIGHLINER)'''
condicion1 = costa_rica["PARTIDA_AR"].str.contains("8704", na=False)
condicion2 = costa_rica["MARCA"].str.contains(listamarca)
costa_rica[condicion].head()
costa_rica.loc[condicion1 & condicion2, "SEGMENTO.1"] = "CAMION"


# %%
costa_rica.head()

# %%
costa_rica.to_csv(r'D:\Basededatos\Limpioparaunir\costa_rica.csv', index=False)


# %%
costa_rica[condicion1 & condicion2]

# %%
listamarca = r'''(HINO|ISUZU|MITSUBISHI|MACK|VOLVO|INTERNATIONAL|FREIGHLINER)'''
condicion1 = costa_rica["PARTIDA_AR"].str.contains("8704", na=False)
condicion2 = costa_rica["MARCA"].str.contains(listamarca)

# %%
