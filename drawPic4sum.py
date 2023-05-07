# 读取temp.xlsx，其中第一列是情绪，第三列是时间

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('temp.xlsx')
result = df.groupby([df.columns[2], df.columns[0]]).size().reset_index(name='counts')

fig, ax = plt.subplots()
for val in [0, 1, 2]:
    data = result[result[df.columns[0]] == val]
    label = ['neutral', 'positive', 'negative'][val]
    ax.plot(data[df.columns[2]], data['counts'], label=label, color=['black', 'blue', 'red'][val])

ax.set_xlabel('Date')
ax.set_ylabel('Count')
ax.legend()

xticks = ax.get_xticks()
ax.set_xticks(xticks[::20])
plt.ylim(bottom=0)
plt.show()