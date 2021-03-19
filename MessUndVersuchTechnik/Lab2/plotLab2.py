import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10,21,1)

y = np.array([4.1003,4.5002,4.9464,5.3367,5.79,6.19,6.5996,7.0643,7.4445,7.9709,8.400])
relStdAb = np.array([4.5362,2.8228,25.4,26.373,0,1.26,18.9,21.072,27.476,43.040,0])*0.001
stdAb = np.multiply(y,relStdAb)

plt.figure(1)
plt.errorbar(x,y,stdAb,linestyle = 'None',marker='x',markersize = 6,barsabove=True, ecolor='Black',)
plt.xlabel("DC Eingangspannung in V")
plt.ylabel("HV AC Ausgangspannung in kV")
plt.grid()
plt.show()

# Add various deviations to the already existing ones:
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
found = np.ones(fit.shape[0])*xScale[idx]
yfound = fit[idx]
xfound = xScale[idx]
#Find intersection between fit and limit line


#Second plot
plt.figure(2)
#fitted line
plt.plot(xScale[idx], fit[idx], 'green',xScale,fit,'orange',label='Fitted line')

plt.errorbar(x,y,stdAb,linestyle = 'None',marker='x',markersize = 8,barsabove=True, ecolor='Black')
#line for 6kV limit
plt.plot(xScale,limLine,"red",linestyle= '--')
plt.plot(found,fit,"red",linestyle= '--')
plt.plot(xfound,yfound,"red",marker='o',markersize = 6,)
#intersection point
plt.xlabel("DC Eingangspannung in V")
plt.ylabel("HV AC Ausgangspannung in kV")
plt.grid()
plt.show()