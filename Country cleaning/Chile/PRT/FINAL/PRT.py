# %%
import os
import pandas as pd
import numpy as np
import datetime

# %%
OFFLINE = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\FINAL\offline.csv")
OTROS = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\FINAL\otros.csv")
SGPRT = pd.read_csv(r"F:\Trabajo\Promotive\Chile\PRT\FINAL\sgprtRB.csv")


# %%
PRT = pd.concat([OFFLINE,
                 OTROS,
                 SGPRT], ignore_index=True, join='outer')

# %%
PRT = PRT[["PPU", "MARCA", "MODELO", "ANO_FABRICACION", "NUM_MOTOR", "NUM_CHASIS","VIN"]]

# %%
PRT.drop_duplicates(subset="PPU", inplace=True)

# %%
PRT.info()
# %%
PRT.to_csv(r'F:\Trabajo\Promotive\Chile\PRT\FINAL\PRT_FINAL.csv', index=False)

