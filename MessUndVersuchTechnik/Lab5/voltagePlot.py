import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Induktive, Kapazitive und Galvanische Kopplung
meas =	{
  "Induktive Kopplung Spannung" : (np.array([[4.9494,9.0424,13.836,17.462,21.360],[5.6087,9.7841,14.721,18.450,21.964],[8.5077,None,24.299,None,37.89]]),
                          ['5kOhm Widerstand','10kOhm Widerstand','Längere schleife'],
                          [20,40,60,80,100],['Störspannung in mV','Frequenz in kHz']),
    "Induktive Kopplung Phase" : (np.array([[69.688,58.844,45.398,37.814,29.737],[51.705,55.541,43.955,33.037,24.583],[70.600,None,42.621,None,26.174]]),
                          ['5kOhm Widerstand','10kOhm Widerstand','Längere schleife'],
                          [20,40,60,80,100],['Phase in Grad','Frequenz in kHz']),
  "Kapazitive Kopplung Spannung": (np.array([[57.099,109.30,164.76,213.80,265.16],[111.15,212.69,309.50,398.20,474.33],[12.820,None,37.566,None,59.789],[25.103,None,72.550,None,116.00]]),
                          ['5kOhm Widerstand','10kOhm Widerstand','Ader 4 Geerdet','Längere schleife'],
                          [20,40,60,80,100],['Störspannung in mV','Frequenz in kHz']),
    "Kapazitive Kopplung Phase": (np.array([[84.780,82.180,79.289,77.019,73.799],[82.388,76.224,72.00,66.600,61.935],[86.536,None,80.317,None,74.861],[84.807,None,79.700,None,74.600]]),
                          ['5kOhm Widerstand','10kOhm Widerstand','Ader 4 Geerdet','Längere schleife'],
                          [20,40,60,80,100],['Phase in Grad','Frequenz in kHz']),
  "Galvanische Kopplung" : (np.array([[42.200,42.198],[41.952,42.110]]),
                            ['5kOhm Widerstand','10kOhm Widerstand'],
                            [50,100],['Störspannung in mV','Frequenz in Hz'])
}
for i in meas:
    plt.figure(i)
    (data,lb,freq,units) = meas.get(i)
    cnt = 0
    for k in data:
        plt.plot(freq, k, linestyle='-', marker='o', label=lb[cnt])

        cnt += 1
    plt.xlabel(units[1])
    plt.ylabel(units[0])
    plt.grid()
    plt.legend()
    plt.show()



data = pd.DataFrame({
    "Abschlüsse": ["Keine", "50 Ohm", "Kurzschluss"],
    "100mm Strecke, Abstand 0.2mm": [91.203, 96.667, 102.00],
    "100mm Strecke, Abstand 0.5mm": [33.205, 45.383, 57.294],
    "50mm Strecke, Abstand 0.5mm": [17.903,24.618,31.168],
    "100mm Strecke, Abstand 1mm": [10.954,20.947,30.583],
    "100mm Geschirmt Strecke, Abstand 0.5mm": [3.8370,7.1024,10.359]
})
ax = data.plot(x = "Abschlüsse", y="100mm Strecke, Abstand 0.2mm", linestyle = '', marker = 'o', markeredgecolor= 'blue', markerfacecolor= 'blue')
data.plot(ax = ax,y="100mm Strecke, Abstand 0.5mm", linestyle = '', marker = 'o', markeredgecolor= 'royalblue', markerfacecolor= 'royalblue')
data.plot(ax = ax,y="100mm Strecke, Abstand 1mm", linestyle = '', marker = 'o', markeredgecolor= 'dodgerblue', markerfacecolor= 'dodgerblue')
data.plot(ax = ax,y="50mm Strecke, Abstand 0.5mm", linestyle = '', marker = 'o', markeredgecolor= 'orange', markerfacecolor= 'orange')
data.plot(ax = ax,y="100mm Geschirmt Strecke, Abstand 0.5mm", linestyle = '', marker = 'o', markeredgecolor= 'forestgreen', markerfacecolor= 'forestgreen')
#data2.plot(x='lb', linestyle = '', marker = 'o')
plt.tight_layout()
plt.legend()
plt.ylabel('Störspannung in mV')
plt.grid(axis = 'y')
plt.show()

data = pd.DataFrame({
    "Abschlüsse": ["Keine", "50 Ohm", "Kurzschluss"],
    "100mm Strecke, Abstand 0.2mm": [61.300, 60.930, 60.510],
    "100mm Strecke, Abstand 0.5mm": [63.000, 60.250, 58.120],
    "50mm Strecke, Abstand 0.5mm": [63.000,60.820,58.750],
    "100mm Strecke, Abstand 1mm": [66.980,59.000,57.370],
    "100mm Geschirmt Strecke, Abstand 0.5mm": [67.180,57.560,53.740]
})
ax = data.plot(x = "Abschlüsse", y="100mm Strecke, Abstand 0.2mm", linestyle = '', color = 'blue',marker = 'o', markeredgecolor= 'blue', markerfacecolor= 'blue')
data.plot(ax = ax,y="100mm Strecke, Abstand 0.5mm", linestyle = '', color = 'royalblue', marker = 'o', markeredgecolor= 'royalblue', markerfacecolor= 'royalblue')
data.plot(ax = ax,y="100mm Strecke, Abstand 1mm", linestyle = '', color = 'dodgerblue',marker = 'o', markeredgecolor= 'dodgerblue', markerfacecolor= 'dodgerblue')
data.plot(ax = ax,y="50mm Strecke, Abstand 0.5mm", linestyle = '', color = 'orange',marker = 'o', markeredgecolor= 'orange', markerfacecolor= 'orange')
data.plot(ax = ax,y="100mm Geschirmt Strecke, Abstand 0.5mm", linestyle = '', color = 'salmon', marker = 'o', markeredgecolor= 'forestgreen', markerfacecolor= 'forestgreen')
#data2.plot(x='lb', linestyle = '', marker = 'o')
plt.tight_layout()
plt.ylabel("Phase in Grad")
plt.legend()
plt.grid(axis = 'y')
plt.show()