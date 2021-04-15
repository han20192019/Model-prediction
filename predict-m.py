import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

#a,b are the input function
#t is the time(x axis)
a=np.cos(np.array(range(0,20)))
aoriginal = list(a)
b=2*np.cos(np.array(range(0,20))-3)
boriginal = list(b)
t=np.array(range(0,20))
print(a)
a_maxid = np.argmax(a)
b_maxid = np.argmax(b)
a_minid = np.argmin(a)
b_minid = np.argmin(b)
print(a_maxid)



a_localmax = argrelextrema(a, np.greater)
a_localmax = a_localmax[0]
a_localmin = argrelextrema(a, np.less)
a_localmin = a_localmin[0]
print(a_localmax)
print(a_localmin)

b_localmax = argrelextrema(b, np.greater)
b_localmax = b_localmax[0]
b_localmin = argrelextrema(b, np.less)
b_localmin = b_localmin[0]

#deal with local max
#rmax is the maximimum of the predicted function
rmax = (a[a_maxid]+b[b_maxid])/2
mpa2 = 0
for i in range(len(a_localmax)):
	temp = list(a_localmax)
	if a_localmax[i]==a_maxid:
		mpa2=i
mpb2 = 0
for i in range(len(b_localmax)):
	if b_localmax[i]==b_maxid:
		mpb2=i


#calculate the local maximum at the right side of the global maximum
mpa = mpa2
mpb = mpb2
r_localmaxvalue = []
while mpa<len(a_localmax) and mpb<len(b_localmax):
	r_localmaxvalue.append((a[a_localmax[mpa]]+b[b_localmax[mpb]])/2)
	mpa += 1
	mpb += 1
#calculate the local maximum at the left side of the global maximum
mpa = mpa2-1
mpb = mpb2-1
while mpa>=0 and mpb>=0:
	r_localmaxvalue.insert(0, (a[a_localmax[mpa]]+b[b_localmax[mpb]])/2)
	mpa -= 1
	mpb -= 1
print(r_localmaxvalue)
t2 = np.array(range(len(r_localmaxvalue)))




#rmin id the minimum
rmin = (a[a_minid]+b[b_minid])/2

minpa2 = 0
for i in range(len(a_localmin)):
	temp = list(a_localmin)
	if a_localmin[i]==a_minid:
		minpa2=i
minpb2 = 0
for i in range(len(b_localmin)):
	if b_localmin[i]==b_minid:
		minpb2=i


minpa = minpa2
minpb = minpb2
r_localminvalue = []
#calculate the local minimum at the right side of the global minimum
while minpa<len(a_localmin) and minpb<len(b_localmin):
	r_localminvalue.append((a[a_localmin[minpa]]+b[b_localmin[minpb]])/2)
	minpa += 1
	minpb += 1
#calculate the local minimum at the left side of the global minimum
minpa = minpa2-1
minpb = minpb2-1
while minpa>=0 and minpb>=0:
	r_localminvalue.insert(0, (a[a_localmin[mpa]]+b[b_localmin[mpb]])/2)
	mpa -= 1
	mpb -= 1
print(r_localminvalue)

#find value for every time for the predicted function. 
#Interpolation between local minimum and local maximum based on input function a
model = a
#fix max
model[a_maxid] = np.max(r_localmaxvalue)
r_maxid = np.argmax(r_localmaxvalue)
mpa = mpa2
while r_maxid < len(r_localmaxvalue) and mpa < len(a_localmax):
	model[a_localmax[mpa]] = r_localmaxvalue[r_maxid]
	r_maxid += 1
	mpa += 1
mpa = mpa2-1
r_maxid = np.argmax(r_localmaxvalue)-1
while r_maxid >= 0 and mpa >= 0:
	model[a_localmax[mpa]] = r_localmaxvalue[r_maxid]
	r_maxid -= 1
	mpa -= 1

#fix min
model[a_minid] = np.min(r_localminvalue)
r_minid = np.argmin(r_localminvalue)
minpa = minpa2
while r_minid < len(r_localminvalue) and minpa < len(a_localmin):
	model[a_localmin[minpa]] = r_localminvalue[r_minid]
	r_minid += 1
	minpa += 1
minpa = minpa2-1
r_minid = np.argmin(r_localminvalue)-1
while r_minid >= 0 and minpa >= 0:
	model[a_localmin[minpa]] = r_localminvalue[r_minid]
	r_minid -= 1
	minpa -= 1


color = 'tab:red'
#red is the final based on green and blue
plt.plot(t,model, color=color)
color = 'tab:green'
plt.plot(t,aoriginal)
color = 'tab:blue'
plt.plot(t,boriginal)
plt.show()