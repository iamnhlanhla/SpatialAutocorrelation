import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import pysal
from pysal import esda, weights
from esda.moran import Moran, Moran_Local
import splot
from splot.esda import moran_scatterplot, plot_moran, lisa_cluster


#I can read the data in Geopandas
avrg_price_airbnb = gpd.read_file(“‪C:\\Users\\Toshiba\\Desktop\\morans\\listings.csv”)
avrg_price_airbnb.head()

#To calculate Queen contiguity spatial weights, I used Pysal
w = weights.Queen.from_dataframe(avrg_price_airbnb, idVariable=”LSOA_CODE” )
w.transform = "R"

avrg_price_airbnb[“w_price”] = weights.lag_spatial(w, avrg_price_airbnb[“price”])

#Moran’s I statistics is typically used to determine the global spatial autocorrelation,
#So I calculated that
y = avrg_price_airbnb[“price”]
moran = Moran(y, w)
moran.I

fig, ax = moran_scatterplot(moran, aspect_equal=True)
plt.show()

#I had already calculated the weights (w) and determined the price as my variable of interest(y).
#To calculate Moran Local, I used Pysal’s functionality
# calculate Moran Local 
m_local = Moran_Local(y, w)
# Plot
fig, ax = moran_scatterplot(m_local, p=0.05)
ax.set_xlabel(‘Price’)
ax.set_ylabel(‘Spatial Lag of Price’)
plt.text(1.95, 0.5, “HH”, fontsize=25)
plt.text(1.95, -1.5, “HL”, fontsize=25)
plt.text(-2, 1, “LH”, fontsize=25)
plt.text(-1, -1, “LL”, fontsize=25)
plt.show()
