# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 02:13:40 2017

@author: Itzik Chaimov

"""
import numpy as np
from numpy import linalg
import math
import matplotlib.pyplot as plt

import calc_magnetic_field as cmf
import calc_magnetic_field_v2f_func as cmfvf2
import algorithm_v3_func as av3f
import calc_magnetic_field_v3f_func as cmfvf3

mue0 = 12.5663*10**(-7)

period=40
size=20

B_array_theo = cmfvf2.calc_field_theo(size)
#####
B_array_noised = cmfvf2.calc_field(size)
#####  taking the last improvment results and using is as in input for further improvment:
#B_array_noised[20:820,0] = B_array_fixed2   


wiggler_size = period*4*5+size*2
a=1.0e-3
vol =a**3

x = (15e-3)/2+a
x = 0
z = (20e-3)/2+ 4.355e-3 
z = 4.355e-3 -a
#y=((size_Hlk-1)/2)*10e-3 #inital value (will be changed inside the loop)\
y = 0

Dy = 1.0  # [mm] this is the first space from zero for which dipoles will be placed
dy = 2.0  # [mm] this is the spacing between two magnetic dipoles


Bz = np.empty([int(period*4*5/dy),wiggler_size-2*size], float)
Bz = np.zeros([int(period*4*5/dy),wiggler_size-2*size], float)

for k in range(int(period*4*5/dy)):
    y=k*dy+Dy
    for n in range(wiggler_size-2*size):
        Xnk=math.sqrt(x**2+z**2+((y-n)*1e-3)**2)
        Bz[k,n] =  (mue0 / 4*math.pi ) *  ((3*(((y-n)*1e-3)**2 +z**2)/Xnk**2) - 1) / (Xnk**3)
        #print str(i) + ": " +  str(sbs_Xnk)
        #print "Hy[" + str(i)+ ",1]: " + str(Hy[i,0])

L = np.empty([int(period*4*5/dy), int(period*4*5/dy)], float)
L = np.zeros([int(period*4*5/dy), int(period*4*5/dy)], float)
L = np.dot(Bz,np.transpose(Bz))

#plt.imshow(L)
#
L_inv = linalg.inv(L)
#plt.figure(2)
#plt.imshow(L_inv)
#plt.figure(3)
#for i in range(160):
#    plt.plot(L_inv[i,:])

#####
B_full_array = B_array_noised.copy() - B_array_theo.copy()  
#####
#B_array = B_array_noised.copy() - B_array_theo[size:period*4*5+size,0].copy() 
#####
B_array = B_full_array[size:period*4*5+size,0]
#####

#K_array = np.zeros([period*4,1], float)
F_array= (-1)*np.dot(Bz,B_array)

m_results = 0.5*(np.dot((-1)*L_inv,F_array))/vol

#H_new = [H_array[i,1] for i in range(0,800,5)]

#print (m_results)

#save to file:
fout = open('m_results.txt', 'w')
for line in range(int(period*4*5/dy)):
    fout.write(str(m_results[line])+'\n')
fout.close()      

#B_array_fixed = cmfvf3.calc_fixed_field(size)

C = 0.5*(np.dot(B_array, np.transpose(B_array)))
Tf_min = C - 0.5*np.dot((np.dot(F_array,L_inv)),F_array)
print 'dy[mm]: ', dy, ',Dy[mm]: ', Dy, ',Tf_min:', Tf_min,
#Tf = C + np.dot(m_results,np.transpose(F_array)) + 0.5*(np.dot(np.dot(m_results,L),np.transpose(m_results)))
#print Tf,
Tf = C 
print ',Tf_max:', Tf , ',a[mm]:', a*1e3

fout = open('var_results.txt', 'a')
fout.write(str(dy) + ',' + str(Dy) + ',' + str(Tf_min) + ',' + str(Tf)+ ',' + str(a*1e3) + ',' + str(max(m_results)) + '\n')
fout.close()


X_AXIS = linspace(0,800,m_results.shape[0], endpoint=False)

plt.figure(1)
plt.plot(X_AXIS, m_results)
plt.scatter(X_AXIS,m_results)
plt.title('M results')
plt.xlabel('Series no. of magnetic dipoles')
plt.ylabel('Magnetization values [A/m]')
plt.grid()
#plt.legend()

