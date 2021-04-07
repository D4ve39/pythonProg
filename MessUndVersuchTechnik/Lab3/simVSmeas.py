import matplotlib.pyplot as plt
import numpy as np

last = np.array([10,50,100,1000])
sim_rippel = np.array([61.364,12.273,6.136,0.614])
meas_rippel = np.array([149.46,64,53.025,43.019])
std_meas_rippel = np.array([5.379,2.162,2.077,2.004])
sim_Uabfall = np.array([347.727,69.545,34.773,3.477])
meas_Uabfall= np.array([600,204,200,0])

x = np.arange(len(meas_rippel))

plt.figure("Rippel")
plt.plot(last,sim_rippel,"red",linestyle = '--',marker='o',label='Rippel Simulation')
plt.plot(last,meas_rippel,"blue",linestyle = '--',marker='o',label='Rippel Gemessen')
plt.fill_between(last, meas_rippel - std_meas_rippel, meas_rippel + std_meas_rippel, color='b', alpha=0.2)
plt.xlabel("Lastwiderstand in Mega Ohm")
plt.ylabel("Rippel in Volt")
plt.legend()
plt.grid()
plt.show()

plt.figure("Spannungsabfall")
plt.plot(last,sim_Uabfall,"red",linestyle = '--',marker='o',label='Spannungsabfall Simulation')
plt.plot(last,meas_Uabfall,"blue",linestyle = '--',marker='o',label='Spannungsabfall Gemessen')
plt.xlabel("Lastwiderstand in Mega Ohm")
plt.ylabel("Spannungsabfall in Volt")
plt.legend()
plt.grid()
plt.show()