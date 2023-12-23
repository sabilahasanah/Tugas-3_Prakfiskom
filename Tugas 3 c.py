import pandas as pd
import numpy as np

j = [i for i in range(0, 26)]
k = np.sin(j)

dataframe = pd.DataFrame({
    'j': j,
    'k': k
})

dataframe['z'] = np.cos(j)

print(dataframe)
