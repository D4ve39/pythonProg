import matplotlib.pyplot as plt
import numpy as np

p = np.arange(0,1000,1)
V_ideal = p * 1
V_real = (p + 80) * 0.9
limit = np.ones(1000)


plt.figure("Statische Kennlinie")
plt.plot(p,V_ideal,"b",linestyle= '-',label = 'Ideal')
plt.plot(p,V_real,"orange",linestyle= '-',label = 'Real')
plt.plot(limit * 980,p,"r", linestyle = '--',label= '980 mbar limit')
plt.xlabel("Druck in mbar")
plt.ylabel("Spannung in mV")
plt.legend()
plt.grid()
plt.show()
