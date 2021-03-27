import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

data = np.zeros((13,14),dtype='int32')
for i in range(13):
    for j in range(14):
        if j == 0 :
            data[i][j] = i
        else:
            data[i][j] = int((i)*(j-1))

column = ['',0,1,2,3,4,5,6,7,8,9,10,11,12]
df = pd.DataFrame(data, columns=column)

ax.table(cellText=df.values, colLabels=df.columns, loc='center')

fig.tight_layout()

plt.show()