#Plot of the current dependence to temperature for a Circuit breaker:
#https://docdif.fr.grpleg.com/general/MEDIAGRP/NP-FT-GT/F01290FR-02.pdf
import numpy as np
import matplotlib.pyplot as plt

#Datas from datasheet

data = np.array([[2.5,7.5,12.5,20,25,31.25,40],[2.4,7.2,12,19.2,24,30,38.4],
                [2.3,6.9,11.5,18.4,23,28.7,36.8],[2.2,6.6,11,17.6,22,27.5,35.2],
                [2.1,6.3,10.5,16.8,21,26.2,33.6],[2,6,10,16,20,25,32],
                [1.9,5.7,9.5,15.2,19,23.7,30.4],[1.8,5.4,9,14.4,18,22.5,28.8],
                [1.7,5.1,8.5,13.6,17,21.2,27.2],[1.6,4.8,8,12.8,16,20,25.6]])

x = np.arange(7)
plt.figure("Nominal current dependence to Temperature")
i = 0
temperature = np.array([-25,-10,0,10,20,30,40,50,60,70])
for y in data:
    lb = str(temperature[i]) + ' Degree Celsius'
    i += 1
    if (i == 5):
        plt.plot(x, y, marker='o',linestyle = '--', label='Reference, 30 Degree Celsius')
    else:
        plt.plot(x,y,marker = 'x',linestyle = '--',label = lb)

plt.grid()
plt.xlabel('Measurements')
plt.ylabel('Current in Ampere')
plt.legend()
plt.show()