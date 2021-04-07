import matplotlib.pyplot as plt
import numpy as np

last = np.array([10,50,100,1000])
rippel1Nf = np.array([149.46,64,53.025,43.019])
rippel10Nf = np.array([76.718,37.573,32.09,26.928])
Uabfall1Nf = np.array([600,204,200,0])
Uabfall10Nf = np.array([500,200,148,0])

#Plot with measured AC voltage and its deviations:
plt.figure("Rippel")
plt.plot(last,rippel1Nf,"red",linestyle = '--',marker='o',label='Rippel 1nF')
plt.plot(last,rippel10Nf,"blue",linestyle = '--',marker='o',label='Rippel 10nF')
plt.xlabel("Lastwiderstand in Mega Ohm")
plt.ylabel("Rippel in Volt")
plt.legend()
plt.grid()
plt.show()

plt.figure("Spannungsabfall")
plt.plot(last,Uabfall1Nf,"red",linestyle = '--',marker='o',label='Spannungsabfall 1nF')
plt.plot(last,Uabfall10Nf,"blue",linestyle = '--',marker='o',label='Spannungsabfall 10nF')
plt.xlabel("Lastwiderstand in Mega Ohm")
plt.ylabel("Spannungsabfall in Volt")
plt.legend()
plt.grid()
plt.show()