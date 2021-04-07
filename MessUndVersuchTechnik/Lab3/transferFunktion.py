import matplotlib.pyplot as plt
import numpy as np
import math


# DC voltage range: 10V to 20V in 1V steps
x = np.array([10,14,16,18])

# Measured AC voltage
y = np.array([4.0851,5.7160,6.5344,7.3788])
# Measured AC voltage (relative) deviations in V
StdAb = np.array([40.321,36.113,47.845,36.955])*0.001

meanDeviations = np.array([1,1,1,1])*0.0001*0.253
# Standard deviation of measurements
deviations = meanDeviations + StdAb
# Upper limit of measurement boxes
maxAb = y+deviations

#Plot with measured AC voltage and its deviations:
plt.figure(1)
plt.errorbar(x,y,deviations,linestyle = 'None',marker='x',markersize = 8,barsabove=True, ecolor='Black',)
plt.xlabel("DC Eingangspannung in V")
plt.ylabel("HV AC Ausgangspannung in kV")
plt.grid()
plt.show()

### Linear fit of measured value
#Scale for more values of the fit
xScale = np.arange(10,20,0.01)
#Linear fit y = mx+c
#Rewriten as y = Ap, with A = [[x 1]] and p = [[m], [c]]
A = np.vstack([x, np.ones(len(x))]).T
limLine = np.ones(xScale.shape[0])*3.375


### Linear fit considering the measurement deviations
m2, c2 = np.linalg.lstsq(A,maxAb,rcond=None)[0]
maxFit = m2*xScale + c2
maxDelt = maxFit - limLine
maxStep = np.sign(maxDelt)
maxIdx = np.argmax(np.diff(maxStep))
maxFound = np.ones(maxFit.shape[0])*xScale[maxIdx]
xMaxFound = xScale[maxIdx]
yMaxFound = maxFit[maxIdx]
print(m2,c2)


#Second plot
plt.figure(2)
#fitted line
plt.plot(xScale,maxFit,'green', label='Fitted line considering deviations')
#measured values with deviations boxes
plt.errorbar(x,y,deviations,linestyle = 'None',marker='x',markersize = 4,barsabove=True, ecolor='Black')
#line for 6kV limit on y axis
plt.plot(xScale,limLine,"red",linestyle= '--',label = '3.375kV limit')
#Intersection point for values+deviation fit
#plt.plot(xMaxFound,yMaxFound,"purple",marker='o',markersize = 6,)
#plt.text(xMaxFound, yMaxFound, '({}, {})'.format(round(xMaxFound,6), round(yMaxFound)))
plt.xlabel("DC Eingangspannung in V")
plt.ylabel("HV AC Ausgangspannung in kV")
plt.grid()
plt.legend()
plt.show()
