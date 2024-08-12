from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

m = Basemap(llcrnrlon=40., llcrnrlat=24., urcrnrlon=65., urcrnrlat=40.,
            rsphere=(6378137.00, 6356752.3142),
            resolution='l', projection='merc',
            lat_0=10., lon_0=-20., lat_ts=20.)

data = pd.read_excel("city.xlsx")
print(data)

long_list = np.array(data["Longitude"].tolist())
lats_list = np.array(data["Latitude"].tolist())
people_list = np.array(data["People"].tolist()) / 90000

long = long_list
lats = lats_list
scale = people_list

x, y = m(long, lats)

m.drawcoastlines()
m.fillcontinents()

m.drawparallels(np.arange(24., 41., 2.), labels=[1, 1, 0, 1])

m.drawmeridians(np.arange(40., 66., 2.), labels=[1, 1, 0, 1])

plt.scatter(x, y, color="red", marker="o", s=scale)

ax.set_title('Iran')
plt.show()
