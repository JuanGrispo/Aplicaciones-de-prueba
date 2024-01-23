# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 23:16:58 2024

@author: jgris
"""

#prueba

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from scipy.io import wavfile


datos=pd.read_csv("archivo_datos.csv")

print(datos['tiempo'])

plt.plot(datos['tiempo'],datos['señal'])
plt.show()