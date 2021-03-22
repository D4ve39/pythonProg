import matplotlib.pyplot as plt
import numpy as np


# DC voltage range: 10V to 20V in 1V steps
x = np.arange(10,21,1)

# Measured AC voltage
y = np.array([4.1003,4.5002,4.9464,5.3367,5.79,6.19,6.5996,7.0643,7.4445,7.9709,8.400])
# Measured AC voltage (relative) deviations in V
relStdAb = np.array([4.5362,2.8228,25.4,26.373,0,1.26,18.9,21.072,27.476,43.040,0])*0.001

measDeviations = np.array([116.9,121.2,128.8,133.6,136.6,141.8,148.4,155,161.2,235.1,235.9])*0.0001
# Standard deviation of measurements
stdAb = np.multiply(y,measDeviations)
# Upper limit of measurement boxes
maxAb = y+stdAb

#Plot with measured AC voltage and its deviations:
plt.figure(1)
plt.errorbar(x,y,stdAb,linestyle = 'None',marker='x',markersize = 8,barsabove=True, ecolor='Black',)
plt.xlabel("DC Eingangspannung in V")
plt.ylabel("HV AC Ausgangspannung in kV")
plt.grid()
plt.show()

# Add measurement deviations to the the standard deviation:


### Linear fit of measured value
#Scale for more values of the fit
xScale = np.arange(10,20,0.01)
#Linear fit y = mx+c
#Rewriten as y = Ap, with A = [[x 1]] and p = [[m], [c]]
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A,y,rcond=None)[0] # use least-squares solution to a linear matrix equation
fit = m*xScale + c
limLine = np.ones(xScale.shape[0])*6
#compute difference between limit and interpolation
delt = fit - limLine
#build step funktion out of this difference array
step = np.sign(delt)
#differenziate the step funktion to get a delta peak, then get the max value of array
idx=np.argmax(np.diff(step))
#vertical line for the found value
found = np.ones(fit.shape[0])*xScale[idx]
#X and Y coordinates of intersection point between limit line and fit line
xfound = xScale[idx]
yfound = fit[idx]

### Linear fit considering the measurement deviations
m2, c2 = np.linalg.lstsq(A,maxAb,rcond=None)[0]
maxFit = m2*xScale + c2
maxDelt = maxFit - limLine
maxStep = np.sign(maxDelt)
maxIdx = np.argmax(np.diff(maxStep))
maxFound = np.ones(maxFit.shape[0])*xScale[maxIdx]
xMaxFound = xScale[maxIdx]
yMaxFound = maxFit[maxIdx]


#Second plot
plt.figure(2)
#fitted line
plt.plot(xScale,fit,'orange',label='Fitted line')
plt.plot(xScale,maxFit,'purple', label='Fitted line considering deviations')
#measured values with deviations boxes
plt.errorbar(x,y,stdAb,linestyle = 'None',marker='x',markersize = 8,barsabove=True, ecolor='Black')
#line for 6kV limit on y axis
plt.plot(xScale,limLine,"red",linestyle= '--',label = '6kV limit')
#found intersection points
#intersection for normal fit
plt.plot(xfound,yfound,"red",marker='o',markersize = 6,)
plt.plot(maxFound, maxFit, "purple", linestyle='--')
#Intersection point for values+deviation fit
plt.plot(xMaxFound,yMaxFound,"purple",marker='o',markersize = 6,)
plt.text(xMaxFound, yMaxFound, '({}, {})'.format(round(xMaxFound,6), round(yMaxFound)))
plt.xlabel("DC Eingangspannung in V")
plt.ylabel("HV AC Ausgangspannung in kV")
plt.grid()
plt.legend()
plt.show()
