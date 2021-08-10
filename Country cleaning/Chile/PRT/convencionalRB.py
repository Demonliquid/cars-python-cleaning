# %%
import os
import pandas as pd
import numpy as np
import datetime


# %% CARGA DE DATOS
path = r'F:\Trabajo\Promotive\Chile\PRT\2'
os.chdir(path)
files = os.listdir(path)
files


# %%
files_xls = [f for f in files if f[-4:] == 'xlsx']
files_xls

# %%
columnas = ['PPU', 'MARCA', 'MODELO', 'ANO_FABRICACION', 'NUM_MOTOR', 'NUM_CHASIS', 'VIN']
chile = pd.DataFrame(columns=columnas)


# %%
for f in files_xls:
    data = pd.read_excel(f, engine='openpyxl')
    chile = pd.concat([chile , data], ignore_index=True, join='outer')

# %%
chile = chile[columnas]

# %%
chile.drop_duplicates(subset="PPU", inplace=True)

# %%
chile.to_csv(r'F:\Trabajo\Promotive\Chile\PRT\Limpio\convencionalRB.csv')

# %%
