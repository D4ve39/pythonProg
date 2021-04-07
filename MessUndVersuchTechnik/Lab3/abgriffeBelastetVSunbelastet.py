import matplotlib.pyplot as plt
import numpy as np

HVDC_unb= np.ones(20)*13.391
rip_HVDC_unb = 43.019 * 0.001

HVDC_b = np.ones(20)*13.3
rip_HVDC_b = 53.025 * 0.001

glatt = np.ones(20)*6.8195
rip_glatt = 25.637 * 0.001



x = np.arange(0,20,1)


plt.figure("Rippel")
#plt.plot(last,sim_rippel,"red",linestyle = '--',marker='o',label='Rippel Simulation')
#plt.plot(last,meas_rippel,"blue",linestyle = '--',marker='o',label='Rippel Gemessen')
plt.plot(x,HVDC_unb,"b",linestyle= '-',label = 'HVDC Out unbelastet')
plt.fill_between(x, HVDC_unb - rip_HVDC_unb, HVDC_unb + rip_HVDC_unb, color='b', alpha=0.2)

plt.plot(x,HVDC_b,"orange",linestyle= '-',label = 'HVDC Out belastet')
plt.fill_between(x, HVDC_b - rip_HVDC_b, HVDC_b + rip_HVDC_b, color='orange', alpha=0.2)

plt.plot(x,HVDC_b,"green",linestyle= '-',label = 'Glatt 1 unbelastet')
plt.fill_between(x, glatt - rip_glatt, glatt + rip_glatt, color='green', alpha=0.2)

plt.xlabel("Lastwiderstand in Mega Ohm")
plt.ylabel("Rippel in Volt")
plt.legend()
plt.grid()
plt.show()
