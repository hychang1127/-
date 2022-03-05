import astroquery.solarsystem as ss
from astroquery.jplhorizons import Horizons
import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

obj = Horizons(id='2012 TC4', location='500@10', epochs={'start':'2000-10-01', 'stop':'2017-10-01','step':'1d'})
vec = obj.vectors()
vec_list_x=list(vec['x'])
vec_list_y=list(vec['y'])
vec_list_z=list(vec['z'])


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1,projection='3d')
ax.scatter(vec_list_x,vec_list_y,vec_list_z) # plot the point (2,3,4) on the figure
plt.show()
