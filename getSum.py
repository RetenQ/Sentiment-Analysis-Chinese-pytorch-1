import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 读取文件
df = pd.read_excel('out.xlsx', engine='openpyxl')

# 获取时间和评价值
time = pd.to_datetime(df[df.columns[0]][:151])
value = df[df.columns[4]][:151]

# 绘制点线图
fig, ax = plt.subplots()
ax.plot(time, value, '-o')
ax.xaxis.set_major_locator(mdates.DayLocator(interval=20))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xlabel('Date')
plt.ylabel('Count')
plt.ylim(bottom=0)

# 标注每个点的 y 值（保留两位小数）
for x, y in zip(time, value):
    # 对于评价值是“0.00”的数据，只显示“0”
    if y == 0:
        plt.text(x, y, '0')
    else:
        plt.text(x, y, f'{y:.0f}',fontsize=9)

# 标注时间点是“2022-12-07”和“2022-12-30”的数据


for x, y in zip(time, value):
    if x.strftime('%Y-%m-%d') in ['2022-12-07','2022-12-14','2022-12-30','2023-03-07','2023-02-10']:
        if(x.strftime('%Y-%m-%d') in ['2022-12-07']):
            plt.scatter(x, y, color='green')
            plt.axvline(x=x, color='green', linestyle='--')
            # 在 x 轴下方标注它们的名字
            plt.text(x, ax.get_ylim()[0], x.strftime('%Y-%m-%d'), color='green', ha='center')
        else:
            plt.scatter(x, y, color='red')
            plt.axvline(x=x, color='red', linestyle='--')
            # 在 x 轴下方标注它们的名字
            plt.text(x, ax.get_ylim()[0], x.strftime('%Y-%m-%d'), color='red', ha='center', va='top')

plt.show()