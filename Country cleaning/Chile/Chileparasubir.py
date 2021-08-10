# %% IMPORTAR LIBRERIAS
import os
import pandas as pd
import numpy as np
import datetime


# %%
chile1 = pd.read_csv(r"D:\Basededatos\Limpioparaunir\chile1.csv")
chile2 = pd.read_csv(r"D:\Basededatos\Limpioparaunir\chile2.csv")


# %%
chile = pd.concat([chile1, chile2], ignore_index=True)

# %%
chile["AÑO"] = chile["AÑO"].astype("float").map('{:.0f}'.format)

# %%
chile.to_csv(r"D:\Basededatos\Limpioparaunir\chile.csv", index=False)
# %%
