
## Plotting:
import matplotlib.pyplot as plt
import numpy as np
import math #needed for definition of pi

## X axis input
t = np.arange(0, math.pi*2, 0.1)
## Y axis inputs
y1 = np.sin(t)
y2 = np.cos(t)


## Generate plot
plt.figure()

plt.subplot(211)
plt.plot(t,y1,'k')
plt.xlabel("phi")
plt.ylabel("sin(phi)")
plt.title('Sin wave')


plt.subplot(212)
plt.plot(t,y2,'r--')
plt.xlabel("phi")
plt.ylabel("cos(phi)")
plt.title('Cos wave')

plt.grid()

## Show plot
plt.show()
