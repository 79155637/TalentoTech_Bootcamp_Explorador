# -*- coding: utf-8 -*-
"""EJExplorador12_76.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_pGOl4Ic8-FU1kOmG-P5KtFi_XkxSdwF
"""

#Dataframe

import pandas as pd

data = {'Nombre': ['Ana', 'Carlos', 'María', 'Juan'],
        'Edad': [20, 22, 21, 23],
        'Calificacion': [85, 90, 78, 95]}

df = pd.DataFrame(data)
print(df)