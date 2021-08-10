# VIENE DE CHILEPREPARABASE.PY

# %% IMPORTAR LIBRERIAS
import os
import pandas as pd
import numpy as np
import datetime
from scripts import motor, quitardecimal, valores, modelogeneral, especifico, origensegunvin, version, modelogenerico


# %%
chile1 = pd.read_csv(r'D:\Basededatos\Limpioparaentregar\chile1.csv')


# %%
chile1.rename(columns={"MODELO / VERSION": "MODELO/VERSION"}, inplace=True)
chile1["MODELO GENERICO"] = None
chile1["MODELO"] = None
chile1["VERSION"] = None
chile1["MOTOR"] = None


columnasutiles = chile1.columns


# %%
chile1 = quitardecimal(chile1, "AÑO")

# %% MOTOR DE MODELO/VERSION
chile1 = motor(chile1)


# %% MODELO GENERAL
chile1 = modelogeneral(chile1)


# %% MODELO ESPECIFICO
chile1 = especifico(chile1, columnasutiles)


# %% MODELO GENERICO
chile1 = modelogenerico(chile1)


# %% VERSION
chile1 = version(chile1)


# %%
chile1.to_csv(r'D:\Basededatos\Limpioparaunir\chile1.csv', index=False)


# %%
chile1.head()
# %%
