import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

column = ['',0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
col = len(column)
row = col-1
data = np.zeros((row,col),dtype='int32')
for i in range(row):
    for j in range(col):
        if j == 0 :
            data[i][j] = i
        else:
            data[i][j] = i*(j-1)


df = pd.DataFrame(data, columns=column)

ax.table(cellText=df.values, colLabels=df.columns, loc='center')

fig.tight_layout()

plt.show()