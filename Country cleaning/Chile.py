# VIENE DE CHILE 1 y 2

# %% IMPORTAR LIBRERIAS
import os
import pandas as pd
import numpy as np
import datetime
from scripts import motor, quitardecimal, valores, modelogeneral, especifico, origensegunvin


# %%
chile1 = pd.read_csv(r"D:\Basededatos\Limpioparaunir\chile1.csv")
chile2 = pd.read_csv(r"D:\Basededatos\Limpioparaunir\chile2.csv")


# %%
chile = pd.concat([chile1, chile2], ignore_index=True)


# %%
chile = quitardecimal(chile, "AÑO")

# %%
chile.to_csv(r"D:\Basededatos\Limpioparaunir\chile.csv", index=False)

# %%
