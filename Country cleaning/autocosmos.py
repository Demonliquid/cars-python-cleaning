# %%
import os
import pandas as pd
import numpy as np
import datetime
import re
from scripts import motor, quitardecimal, valores, modelogeneral, especifico, origensegunvin, version, modelogenerico, especifico2, corregirmodelo, segmentacion, cilindrada, traccion, marca


# %% CARGA DE DATOS
path = r'D:\Basededatos\Origen\Autocosmos'
os.chdir(path)
files = os.listdir(path)
files

files_xls = [f for f in files if f[-4:] == 'xlsx']
files_xls

# %%

autocosmos = pd.DataFrame()


for f in files_xls:
    data = pd.read_excel(f, engine='openpyxl')
    autocosmos = pd.concat([autocosmos , data], ignore_index=True, join='outer')
    data = None


# %%
df.info(verbose=True,null_counts=True)

# %%
condicion = autocosmos["Moneda"].isna()
print("Moneda: \n\t", valores(autocosmos[condicion], "Mercado"))

# %%
for column in list(autocosmos.columns):
    condicion = autocosmos[column].isna()
    print(f"{column}: \n\t", valores(autocosmos[condicion], "Mercado"), "\n")


# %%
list(autocosmos.columns)[0]
# %%
autocosmos.to_csv(r"D:\Basededatos\Limpioparaunir\autocosmos.csv", index=False, sep=";")

# %%
df = autocosmos
# %%
import unicodedata
cols = df.select_dtypes(include=[np.object]).columns
df[cols] = df[cols].apply(lambda x: x.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
df


# %%
df.to_csv(r"D:\Basededatos\Limpioparaunir\autocosmos.csv", index=False, sep=",", encoding="utf-8")

# %%
df.to_excel(r"D:\Basededatos\Limpioparaunir\autocosmos.xlsx", index=False)



# %%
for column in list(df.columns):
    df[column] = df[column].astype(str).str.replace("|","/")
    df[column] = df[column].astype(str).str.replace("ñ","n")

df.columns = df.columns.str.replace(r"ñ", "n")

# %%
df.columns = df.columns.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

# %%
df.info()
# %%
df = pd.read_excel(r"D:\Basededatos\Limpioparaunir\autocosmos.xlsx", engine='openpyxl')

# %%
df.to_csv(r"D:\Basededatos\Limpioparaunir\autocosmos.csv", index=True)

# %%
