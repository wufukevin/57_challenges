import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

data = np.fromfunction(lambda i, j: (i + 1) * (j + 1), (9, 9))

df = pd.DataFrame(data, columns=list('1234567890'))

ax.table(cellText=df.values, colLabels=df.columns, loc='center')

fig.tight_layout()

plt.show()