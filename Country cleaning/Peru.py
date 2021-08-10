# %%
import os
from typing import Tuple
from numpy.lib.function_base import place
from numpy.lib.shape_base import _column_stack_dispatcher, column_stack
import pandas as pd
import numpy as np
import datetime
import re
from scripts import versionfinal,versionurgencia,versionespecifico,identificacionmotor,motorseguncilindrada,corregirmarca, progreso, motor, quitardecimal, valores, modelogeneral, especifico, origensegunvin, version, modelogenerico, especifico2, corregirmodelo, segmentacion, cilindrada, traccion, marca


# %%
peru04 = pd.read_csv(r"D:\Basededatos\Limpioparaentregar\peru\peru04-07original.csv")
peru08 = pd.read_csv(r"D:\Basededatos\Limpioparaentregar\peru\peru08-11original.csv")
peru12 = pd.read_csv(r"D:\Basededatos\Limpioparaentregar\peru\peru12-15original.csv")
peru16 = pd.read_csv(r"D:\Basededatos\Limpioparaentregar\peru\peru16-21original.csv")


# %%
peru04 = peru08.rename(columns={
                            "DESCRIPCION COMERCIAL 1":"MODELO/VERSION",
                            "AÑO DE IMPORTACION":"FECHA DE IMPORTACION",
                            "AÑO DE FABRICACION": "AÑO"})

peru08 = peru08.rename(columns={
                            "DESCRIPCION COMERCIAL 1":"MODELO/VERSION",
                            "AÑO DE IMPORTACION":"FECHA DE IMPORTACION",
                            "AÑO DE FABRICACION": "AÑO"})

peru12 = peru12.rename(columns={
                            "DESCRIPCION COMERCIAL 1":"MODELO/VERSION",
                            "AÑO DE IMPORTACION":"FECHA DE IMPORTACION",
                            "AÑO DE FABRICACION": "AÑO"})


peru16 = peru16.rename(columns={
                            "DESCRIPCION COMERCIAL 1":"MODELO/VERSION",
                            "AÑO DE IMPORTACION":"FECHA DE IMPORTACION",
                            "AÑO DE FABRICACION": "AÑO"})


# %%
peru = pd.concat([peru04, peru08, peru12, peru16], ignore_index=True)
peru04 = None
peru08 = None
peru12 = None
peru16 = None


# %%
condicion = peru["DATOS PERSONALES"].str.contains(("8711")) == False
peru = peru[condicion]

# # %%
# valores(peru, "TIPO_VEHICULO")


# # %%
# peru.to_csv(r"D:\Basededatos\Limpioparaentregar\peru\peru_original.csv", index=False)

# # %%
# list(peru.columns)

# # %%
# for x in range(1,6):
#     print(f"{x}:",peru[f"DESCRIPCION COMERCIAL {x}"].astype(str).map(len).max())

# # %%
# # NO HAY NADA QUE AGREGAR DESDE LOS DATOS ORIGINALES
# peru04 = pd.read_csv(r"D:\Basededatos\Limpioparaunir\peru04-07.csv")
# peru08 = pd.read_csv(r"D:\Basededatos\Limpioparaunir\peru08-11.csv")
# peru12 = pd.read_csv(r"D:\Basededatos\Limpioparaunir\peru12-15.csv")
# peru16 = pd.read_csv(r"D:\Basededatos\Limpioparaunir\peru16-21.csv")





# # %%
# peru08 = peru08.rename(columns={
#                             "DESCRIPCION COMERCIAL 1":"MODELO/VERSION",
#                             "AÑO DE IMPORTACION":"FECHA DE IMPORTACION",
#                             "AÑO DE FABRICACION": "AÑO"})

# peru12 = peru12.rename(columns={
#                             "DESCRIPCION COMERCIAL 1":"MODELO/VERSION",
#                             "AÑO DE IMPORTACION":"FECHA DE IMPORTACION",
#                             "AÑO DE FABRICACION": "AÑO"})


# peru16 = peru16.rename(columns={
#                             "DESCRIPCION COMERCIAL 1":"MODELO/VERSION",
#                             "AÑO DE IMPORTACION":"FECHA DE IMPORTACION",
#                             "AÑO DE FABRICACION": "AÑO"})


# # %%
# peru = pd.concat([peru04, peru08, peru12, peru16], ignore_index=True)
# peru04 = None
# peru08 = None
# peru12 = None
# peru16 = None

# %%
peru.info()

# %%
peru = quitardecimal(peru, "AÑO")
condicion = peru["AÑO"] == "nan"
peru.loc[condicion, "AÑO"] = None


# %%
peru = quitardecimal(peru, "CANTIDAD")
condicion = peru["CANTIDAD"] == "nan"
peru.loc[condicion, "CANTIDAD"] = 1

# %%
columnasutiles = list(peru.columns)

# %%  PRIMERO EXTRAIGO MODELO, MARCA y VERSION DIRECTO DE REGEX PORQUE DESPUES ME DA PROBLEMAS EL DICCIONARIO
peru["MARCA"] = None
peru["MODELO"] = None
peru["VERSION"] = None

peru["MODELO/VERSION"] = peru["MODELO/VERSION"].astype(str).str.strip()


# TAMBIEN AGREGUE UN PUNTO DESPUES DE LAS LETRAS Y ANTES DEL ESPACIO
# peru["MARCA1"] = peru["MODELO/VERSION"].str.extract(r"MARCA\s?:\s?(.+?)[\s,]")[0]
# peru["MARCA2"] = peru["MODELO/VERSION"].str.extract(r"M\s?:\s?(.+?)[\s,]")[0]

peru["MARCA1"] = peru["MODELO/VERSION"].str.extract(r"MARCA\s?:\s?(\w+[\s-]{0,1}\w+)[-,\s]")[0]
peru["MARCA2"] = peru["MODELO/VERSION"].str.extract(r"M\s?:\s?(\w+[\s-]{0,1}\w+)[,\s-]")[0]



# peru["MODELO1"] = peru["MODELO/VERSION"].str.extract(r"MODELO\s?:\s?(.+?)[\s,]")[0]  # ORIGINAL BIEN PERO PROBLEMAS PARA ESPACIOS ENTRE MODELOS
# peru["MODELO2"] = peru["MODELO/VERSION"].str.extract(r"Modelo\s?:\s?(.+?)[\s,]")[0]
# peru["MODELO3"] = peru["MODELO/VERSION"].str.extract(r",MOD\s?:\s?(.+?)[\s,]")[0]

peru["MODELO1"] = peru["MODELO/VERSION"].str.extract(r"MODELO\s?:\s?(\w+[\s-]{0,1}\w+)[,\s]")[0]  # PRUEBA PARA CONSEGUIR MODELOS SEPARADOS POR ESPACIO
peru["MODELO2"] = peru["MODELO/VERSION"].str.extract(r"Modelo\s?:\s?(\w+[\s-]{0,1}\w+)[,\s]")[0]
peru["MODELO3"] = peru["MODELO/VERSION"].str.extract(r",MOD\s?:\s?(\w+[\s-]{0,1}\w+)[,\s]")[0]
peru["MODELO4"] = peru["MODELO/VERSION"].str.extract(r"MODELO\s?:\s?\(?.+?\)?-(\w+[\s-]{0,1}\w+)[,\s]")[0]


# peru["VERSION1"] = peru["MODELO/VERSION"].str.extract(r"VE\s?:\s?(.+?),?\s")[0]
peru["VERSION1"] = peru["MODELO/VERSION"].str.extract(r"VE\s?:\s?(\w+[\s-]{0,1}\w+)[,\s]")[0]


# %%
# CAMBIO POR REGEX
condicion = peru["MARCA"].isna()
peru.loc[condicion, "MARCA"] = peru.loc[condicion, "MARCA1"]
# QUITAR REGEX DEFECTUOSO
condicion = peru["MARCA"].isin([",","0"])
peru.loc[condicion, "MARCA"] = None
# CAMBIO POR REGEX
condicion = peru["MARCA"].isna()
peru.loc[condicion, "MARCA"] = peru.loc[condicion, "MARCA2"]
# QUITAR REGEX DEFECTUOSO
condicion = peru["MARCA"].isin([",","0"])
peru.loc[condicion, "MARCA"] = None


# CAMBIO POR REGEX
condicion = peru["MODELO"].isna()
peru.loc[condicion, "MODELO"] = peru.loc[condicion, "MODELO1"]
# QUITAR REGEX DEFECTUOSO
condicion = peru["MODELO"].isin([",","0"])
peru.loc[condicion, "MODELO"] = None
# CAMBIO POR REGEX
condicion = peru["MODELO"].isna()
peru.loc[condicion,"MODELO"] = peru.loc[condicion, "MODELO2"]
# QUITAR REGEX DEFECTUOSO
condicion = peru["MODELO"].isin([",","0"])
peru.loc[condicion, "MODELO"] = None
# CAMBIO POR REGEX
condicion = peru["MODELO"].isna()
peru.loc[condicion,"MODELO"] = peru.loc[condicion, "MODELO3"]
# QUITAR REGEX DEFECTUOSO
condicion = peru["MODELO"].isin([",","0"])
peru.loc[condicion, "MODELO"] = None
# CAMBIO POR REGEX
condicion = peru["MODELO"].isna()
peru.loc[condicion,"MODELO"] = peru.loc[condicion, "MODELO4"]
# QUITAR REGEX DEFECTUOSO
condicion = peru["MODELO"].isin([",","0"])
peru.loc[condicion, "MODELO"] = None


# CAMBIO POR REGEX
condicion = peru["VERSION"].isna()
peru.loc[condicion,"VERSION"] = peru.loc[condicion, "VERSION1"]
# QUITAR REGEX DEFECTUOSO
condicion = peru["VERSION"].isin([",","0"])
peru.loc[condicion, "VERSION"] = None



peru = peru[columnasutiles]

peru["MARCA"] = peru["MARCA"].str.strip()
peru["MODELO"] = peru["MODELO"].str.strip()
peru["VERSION"] = peru["VERSION"].str.strip()



# %% APLICAR DICCIONARIO SOLO A SECTORES SIN MARCA Y DESPUES MODELOS
condicion = peru["MARCA"].isna()
perusinmarca = peru[condicion]
peruconmarca = peru[~condicion]
peru = None


# %% SE CORRIGE LA MARCA UNA VEZ TODO UNIDO
perusinmarca = marca(perusinmarca)
peru = pd.concat([perusinmarca, peruconmarca], ignore_index=True)
perusinmarca = None
peruconmarca = None
peru = corregirmarca(peru, columnasutiles)





# %% MODELOS
condicion = peru["MODELO"].isna()
perusinmodelo = peru[condicion]
peruconmodelo = peru[~condicion]
peru = None

perusinmodelo = especifico2(perusinmodelo, columnasutiles)

peru = pd.concat([perusinmodelo, peruconmodelo], ignore_index=True)
perusinmodelo = None
peruconmodelo = None


peru = corregirmodelo(peru, columnasutiles)



# %%
condicion = peru["VERSION"].isna()
perusinversion = peru[condicion]
peruconversion = peru[~condicion]
peru = None


perusinversion = versionespecifico(perusinversion)


peru = pd.concat([perusinversion, peruconversion], ignore_index=True)
perusinversion = None
peruconversion = None


# %%
peru = segmentacion(peru,columnasutiles)


# %% AGREGAR TODO LO DE ABAJO A SCRIPTS.py
peru = motorseguncilindrada(peru,columnasutiles)



# %% IDENTIFICACION MOTOR
peru = identificacionmotor(peru, columnasutiles)


# %%
condicion = peru["NUMERO MOTOR"].notna()
condicion2 = peru["IDENTIFICACION MOTOR"].isna()
peru.loc[condicion & condicion2, "IDENTIFICACION MOTOR"] = peru.loc[condicion & condicion2, "NUMERO MOTOR"].str[0:5]


# %% TRADUCCION MANUAL A PASAR A SCRIPT
peru["ORIGEN"] = peru["ORIGEN"].str.capitalize()
peru["ORIGEN"].replace('China (mainland)', 'China', inplace=True)
peru["ORIGEN"].replace('Taiwan, china', 'China', inplace=True)
peru["ORIGEN"].replace(r"Cote d'ivoire", 'Costa de Marfil', inplace=True)
peru["ORIGEN"].replace(r"Germany/west germany", 'Alemania', inplace=True)
peru["ORIGEN"].replace(r"Korea (south)", 'Corea del Sur', inplace=True)
peru["ORIGEN"].replace(r"Saudi arabia", 'Arabia Saudita', inplace=True)
peru["ORIGEN"].replace(r"United kingdom", 'Reino Unido', inplace=True)
peru["ORIGEN"].replace(r"Italy", 'Italia', inplace=True)
peru["ORIGEN"].replace(r"Greece", 'Grecia', inplace=True)
peru["ORIGEN"].replace(r"Belgium", 'Belgica', inplace=True)
peru["ORIGEN"].replace(r"Luxembourg", 'Luxemburgo', inplace=True)
peru["ORIGEN"].replace(r"United states", 'Estados Unidos', inplace=True)
peru["ORIGEN"].replace(r"Japan", 'Japon', inplace=True)
peru["ORIGEN"].replace(r"Czech republic", 'Republica Checa', inplace=True)
peru["ORIGEN"].replace(r"United arab emirates", 'Emiratos Arabes Unidos', inplace=True)
peru["ORIGEN"].replace(r"Ethiopia", 'Etiopia', inplace=True)
peru["ORIGEN"].replace(r"Hungary", 'Hungria', inplace=True)
peru["ORIGEN"].replace(r"Brazil", 'Brasil', inplace=True)
peru["ORIGEN"].replace(r"Spain", 'España', inplace=True)
peru["ORIGEN"].replace(r"France", 'Francia', inplace=True)
peru["ORIGEN"].replace(r"Switzerland", 'Suiza', inplace=True)
peru["ORIGEN"].replace(r"Thailand", 'Tailandia', inplace=True)
peru["ORIGEN"].replace(r"Denmark", 'Dinamarca', inplace=True)
peru["ORIGEN"].replace(r"Finland", 'Finlandia', inplace=True)
peru["ORIGEN"].replace(r"Poland", 'Polonia', inplace=True)
peru["ORIGEN"].replace(r"Myanmar", 'Birmania', inplace=True)
peru["ORIGEN"].replace(r"Ireland", 'Irlanda', inplace=True)
peru["ORIGEN"].replace(r"Netherlands", 'Paises Bajos', inplace=True)
peru["ORIGEN"].replace(r"South africa", 'Sudafrica', inplace=True)
peru["ORIGEN"].replace(r"Sweden", 'Suecia', inplace=True)
peru["ORIGEN"].replace(r"Malaysia", 'Malasia', inplace=True)
peru["ORIGEN"].replace(r"Ussr/cis", 'Rusia', inplace=True)
peru["ORIGEN"].replace(r"Germany/east germany", 'Alemania', inplace=True)
peru["ORIGEN"].replace(r"Germany", 'Alemania', inplace=True)
peru["ORIGEN"].replace(r"Turkey", 'Turquia', inplace=True)
peru["ORIGEN"].replace(r"Cayman islands", 'Islas Caiman', inplace=True)
peru["ORIGEN"].replace(r"Morocco", 'Marruecos', inplace=True)
peru["ORIGEN"].replace(r"Korea, republic of", 'Corea del sur', inplace=True)
peru["ORIGEN"].replace(r"Corea, republic of", 'Corea del sur', inplace=True)
peru["ORIGEN"].replace(r"Korea, democratic people`s rep. of", 'Corea del sur', inplace=True)
peru["ORIGEN"].replace(r"Slovakia", 'Eslovaquia', inplace=True)
peru["ORIGEN"].replace(r"Viet nam", 'Vietnam', inplace=True)
peru["ORIGEN"].replace(r"Zonas francas del peru", 'Peru', inplace=True)
peru["ORIGEN"].replace(r"Russian federation", 'Rusia', inplace=True)
peru["ORIGEN"].replace(r"Corea, democratic pe", 'Corea del sur', inplace=True)
peru["ORIGEN"].replace(r"New zealand", 'Nueva zelanda', inplace=True)
peru["ORIGEN"].replace(r"Dominican republic", 'Republica Dominicana', inplace=True)
peru["ORIGEN"].replace(r"Swaziland", 'Suiza', inplace=True)
peru["ORIGEN"].replace(r"Ukraine", 'Ucrania', inplace=True)
peru["ORIGEN"] = peru["ORIGEN"].str.upper()


# %%
peru = peru.rename(columns={
                            "MODELO/VERSION":"DESCRIPCION COMERCIAL 1"})




# %%
peru["MODELO"].isna().sum()


# %%
peru.info(null_counts=True)



# %% ARREGLOS FINALES Y MANUALES DESPUSE DE REVISION
# SACAR DEUTZ QUE ES UNA MARCA DE MOTORES
condicion = peru["MARCA"] != "DEUTZ"
peru = peru[condicion]


# SACAR ATLAS QUE ES UNA MARCA DE GENERADORES
condicion = peru["MARCA"] != "ATLAS COPCO"
peru = peru[condicion]


# SI HAY VERSION UNA S SOLA SON BASTANTE IRRECUPERABLES
condicion = peru["MARCA"].isna()
condicion2 = peru["MODELO"].isna()
condicion3 = peru["VERSION"].notna()
peru.loc[condicion & condicion2 & condicion3, "VERSION"] = None



# %%
condicion = peru["MARCA"].isna()
condicion2 = peru["MODELO"].notna()
valores(peru[condicion & condicion2], "DESCRIPCION COMERCIAL 1")


# %%
peru.to_csv(r"D:\Basededatos\Limpioparaunir\peruoriginal.csv", index=False)
#peru.to_csv(r"D:\Basededatos\Limpioparaunir\peru.csv", index=False)


# %%
valores(peru, "IDENTIFICACION MOTOR")


# %%
condicion = peru["MODELO"].isna()

list(valores(peru[condicion], "MODELO/VERSION"))[0:50]
]





# %% CODIFICAR PARA SCHEMA  -- CODIFICAR -- PROBAR ACA Y PASAR A SCRIPTS


# La base codificada no soporta campos sin marca y modelo
condicion = peru["MODELO"].notna()
condicion2 = peru["MARCA"].notna()
peru = peru[condicion & condicion2]
condicion = None
condicion2 = None


# Diccionarios
models = pd.read_excel(r"D:\Basededatos\schema\models.xlsx", engine="openpyxl")
brands = pd.read_excel(r"D:\Basededatos\schema\brands.xlsx", engine="openpyxl")


# %% CODIFICAR CON MARCA Y MODELO

# Unir base con marca
perucodificado = pd.merge(left=peru,
                          right=brands,
                          left_on="MARCA",
                          right_on="MARCAS",
                          how="left")
peru = None
brands = None

# Dejar marca codificada y limpiar campos adicionales
perucodificado["MARCA"] = perucodificado["CODIGO_MARCA"]
perucodificado = perucodificado[columnasutiles]


# %% Unir base con modelo - Si agrega vehiculos es porque hay duplicados en el diccionario
# Se une teniendo en cuenta marca y modelo
perucodificado = pd.merge(left=perucodificado,
                          right=models,
                          left_on=["MARCA", "MODELO"],
                          right_on=["CODIGO_MARCA", "MODELOS"],
                          how="left")


# Dejar marca codificada y limpiar campos adicionales
perucodificado["MODELO"] = perucodificado["CODIGO_MODELO"]
perucodificado = perucodificado[columnasutiles]
models = None


# %% Quitar campos redundantes de la base
for item in ['MARCA', 'TIPO_VEHICULO', 'SEGMENTO.1', 'CARROCERIA']:
    columnasutiles.remove(item)

perucodificado = perucodificado[columnasutiles]


# %% TRADUCCION MANUAL A PASAR A SCRIPT
perucodificado["ORIGEN"] = perucodificado["ORIGEN"].str.capitalize()
perucodificado["ORIGEN"].replace('China (mainland)', 'China', inplace=True)
perucodificado["ORIGEN"].replace('Taiwan, china', 'China', inplace=True)
perucodificado["ORIGEN"].replace(r"Cote d'ivoire", 'Costa de Marfil', inplace=True)
perucodificado["ORIGEN"].replace(r"Germany/west germany", 'Alemania', inplace=True)
perucodificado["ORIGEN"].replace(r"Korea (south)", 'Corea del Sur', inplace=True)
perucodificado["ORIGEN"].replace(r"Saudi arabia", 'Arabia Saudita', inplace=True)
perucodificado["ORIGEN"].replace(r"United kingdom", 'Reino Unido', inplace=True)
perucodificado["ORIGEN"].replace(r"Italy", 'Italia', inplace=True)
perucodificado["ORIGEN"].replace(r"Greece", 'Grecia', inplace=True)
perucodificado["ORIGEN"].replace(r"Belgium", 'Belgica', inplace=True)
perucodificado["ORIGEN"].replace(r"Luxembourg", 'Luxemburgo', inplace=True)
perucodificado["ORIGEN"].replace(r"United states", 'Estados Unidos', inplace=True)
perucodificado["ORIGEN"].replace(r"Japan", 'Japon', inplace=True)
perucodificado["ORIGEN"].replace(r"Czech republic", 'Republica Checa', inplace=True)
perucodificado["ORIGEN"].replace(r"United arab emirates", 'Emiratos Arabes Unidos', inplace=True)
perucodificado["ORIGEN"].replace(r"Ethiopia", 'Etiopia', inplace=True)
perucodificado["ORIGEN"].replace(r"Hungary", 'Hungria', inplace=True)
perucodificado["ORIGEN"].replace(r"Brazil", 'Brasil', inplace=True)
perucodificado["ORIGEN"].replace(r"Spain", 'España', inplace=True)
perucodificado["ORIGEN"].replace(r"France", 'Francia', inplace=True)
perucodificado["ORIGEN"].replace(r"Switzerland", 'Suiza', inplace=True)
perucodificado["ORIGEN"].replace(r"Thailand", 'Tailandia', inplace=True)
perucodificado["ORIGEN"].replace(r"Denmark", 'Dinamarca', inplace=True)
perucodificado["ORIGEN"].replace(r"Finland", 'Finlandia', inplace=True)
perucodificado["ORIGEN"].replace(r"Poland", 'Polonia', inplace=True)
perucodificado["ORIGEN"].replace(r"Myanmar", 'Birmania', inplace=True)
perucodificado["ORIGEN"].replace(r"Ireland", 'Irlanda', inplace=True)
perucodificado["ORIGEN"].replace(r"Netherlands", 'Paises Bajos', inplace=True)
perucodificado["ORIGEN"].replace(r"South africa", 'Sudafrica', inplace=True)
perucodificado["ORIGEN"].replace(r"Sweden", 'Suecia', inplace=True)
perucodificado["ORIGEN"].replace(r"Malaysia", 'Malasia', inplace=True)
perucodificado["ORIGEN"].replace(r"Ussr/cis", 'Rusia', inplace=True)
perucodificado["ORIGEN"].replace(r"Germany/east germany", 'Alemania', inplace=True)
perucodificado["ORIGEN"].replace(r"Germany", 'Alemania', inplace=True)
perucodificado["ORIGEN"].replace(r"Turkey", 'Turquia', inplace=True)
perucodificado["ORIGEN"].replace(r"Cayman islands", 'Islas Caiman', inplace=True)
perucodificado["ORIGEN"].replace(r"Morocco", 'Marruecos', inplace=True)
perucodificado["ORIGEN"].replace(r"Korea, republic of", 'Corea del sur', inplace=True)
perucodificado["ORIGEN"].replace(r"Corea, republic of", 'Corea del sur', inplace=True)
perucodificado["ORIGEN"].replace(r"Korea, democratic people`s rep. of", 'Corea del sur', inplace=True)
perucodificado["ORIGEN"].replace(r"Slovakia", 'Eslovaquia', inplace=True)
perucodificado["ORIGEN"].replace(r"Viet nam", 'Vietnam', inplace=True)
perucodificado["ORIGEN"].replace(r"Zonas francas del peru", 'Peru', inplace=True)
perucodificado["ORIGEN"].replace(r"Russian federation", 'Rusia', inplace=True)
perucodificado["ORIGEN"].replace(r"Corea, democratic pe", 'Corea del sur', inplace=True)
perucodificado["ORIGEN"].replace(r"New zealand", 'Nueva zelanda', inplace=True)
perucodificado["ORIGEN"].replace(r"Dominican republic", 'Republica Dominicana', inplace=True)
perucodificado["ORIGEN"].replace(r"Swaziland", 'Suiza', inplace=True)
perucodificado["ORIGEN"].replace(r"Ukraine", 'Ucrania', inplace=True)
perucodificado["ORIGEN"] = perucodificado["ORIGEN"].str.upper()



# %% LIMPIAR UN ERROR PARTICULAR
condicion = perucodificado["ORIGEN"] == "ESPAÃ\x91A"
perucodificado.loc[condicion, "ORIGEN"] = "ESPAÑA"




# %% Codificar lugares geograficos
places = pd.read_excel(r"D:\Basededatos\schema\places.xlsx", engine="openpyxl")


# Codificar MERCADO
perucodificado = pd.merge(left=perucodificado,
                          right=places,
                          left_on="MERCADO",
                          right_on="country",
                          how="left")

perucodificado["MERCADO"] = perucodificado["place_id"]
perucodificado = perucodificado[columnasutiles]

# Codificar ORIGEN
perucodificado = pd.merge(perucodificado, places, left_on="ORIGEN", right_on="country", how="left")
perucodificado["ORIGEN"] = perucodificado["place_id"]
perucodificado = perucodificado[columnasutiles]

places = None


# %% Relacionar bases
perucodificado["specs_id"] = range(1, len(perucodificado) + 1)
perucodificado["vehicle_id"] = range(1, len(perucodificado) + 1)
perucodificado["identification_id"] = range(1, len(perucodificado) + 1)
columnasutiles.append("specs_id")
columnasutiles.append("vehicle_id")
columnasutiles.append("identification_id")


# %%
specs = perucodificado[["specs_id", "vehicle_id", "NUMERO MOTOR", "COMBUSTIBLE", "TRACCION", "CILINDRADA", "TRANSMISION", "MOTOR"]]
identification = perucodificado[["identification_id", "vehicle_id", "CHASIS", "FECHA DE IMPORTACION", "DATOS PERSONALES"]]

# %%
for item in ["NUMERO MOTOR", "COMBUSTIBLE", "TRACCION", "CILINDRADA", "TRANSMISION", "MOTOR", "CHASIS", "FECHA DE IMPORTACION", "DATOS PERSONALES"]:
    columnasutiles.remove(item)



# %%
perucodificado = perucodificado[columnasutiles]
perucodificado = perucodificado[["vehicle_id", "MERCADO", "MODELO/VERSION", "MODELO", "VERSION", "ORIGEN", "AÑO", "CANTIDAD"]]

# %%
perucodificado

# %%
specs
# %%
identification
# %%
perucodificado.to_csv(r"D:\Basededatos\schema\bases\peru\flotaperu.csv", index=False)
specs.to_csv(r"D:\Basededatos\schema\bases\peru\specsperu.csv", index=False)
identification.to_csv(r"D:\Basededatos\schema\bases\peru\identificationperu.csv", index=False)

# %%
perucodificado.info()
# %%
condicion = perucodificado["MODELO"].isna()
perucodificado[condicion]
# %%
perucodificado[135:137]
# %%
