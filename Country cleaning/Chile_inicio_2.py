# VIENE DE CHILEPREPARABASE.PY

# %% IMPORTAR LIBRERIAS
import os
import pandas as pd
import numpy as np
import datetime
from scripts import motor, quitardecimal, valores, modelogeneral, especifico, origensegunvin, version, modelogenerico


# %%
chile2 = pd.read_csv(r'D:\Basededatos\Limpioparaentregar\chile2.csv')


# %%
chile2.rename(columns={"MODELO / VERSION": "MODELO/VERSION"}, inplace=True)
chile2["MODELO GENERICO"] = None
chile2["MODELO"] = None
chile2["VERSION"] = None
chile2["MOTOR"] = None


columnasutiles = chile2.columns


# %%
chile2 = quitardecimal(chile2, "AÑO")

# %% MOTOR DE MODELO/VERSION
chile2 = motor(chile2)


# %% MODELO GENERAL
chile2 = modelogeneral(chile2)


# %% MODELO ESPECIFICO
chile2 = especifico(chile2, columnasutiles)


# %% MODELO GENERICO
chile2 = modelogenerico(chile2)


# %% VERSION
chile2 = version(chile2)


# %%
chile2.to_csv(r'D:\Basededatos\Limpioparaunir\chile2.csv', index=False)


# %%
chile2.head()
# %%
