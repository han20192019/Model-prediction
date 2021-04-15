import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

a=np.cos(np.array(range(0,20)))
b=2*np.cos(np.array(range(0,20))-3)
aoriginal = list(a)
infunc = [a,b]
pred = []
pred.append(np.random.uniform(low = infunc[0][0]-0.1, high = infunc[0][0]+0.1))
for i in range(1,20):
	temp = []
	#generate a random point near the value of every input function
	for j in infunc:
		temp.append(np.random.uniform(low = j[i]-0.1, high = j[i]+0.1))
	mm = temp[0]
	mm_dis = (temp[0]-pred[i-1])*(temp[0]-pred[i-1])
	#pick the one nearest to the value of the predict function at the previous time
	for j in temp:
		if (j-pred[i-1])*(j-pred[i-1])<mm_dis:
			mm_dis = (j-pred[i-1])*(j-pred[i-1])
			mm = j
	pred.append(mm)
time = list(range(0,20))
#red function is the predicted one
color = 'tab:red'
plt.plot(time, pred, color = color)
plt.plot(time, a)
plt.plot(time, b)
plt.show()