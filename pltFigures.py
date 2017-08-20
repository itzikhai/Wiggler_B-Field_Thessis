# -*- coding: utf-8 -*-
"""
Created on Wed Jul 05 01:07:24 2017

@author: CHAIMOVS
"""

import matplotlib.pyplot as plt
import numpy as np


dotRes=np.dot(m_results, Bz)
dotResVol=dotRes*vol

B_array_noised_reduced = B_array_noised[size:period*4*5+size,0]
#B_array_noised_reduced = B_array_noised
B_array_theory_reduced = B_array_theo[size:period*4*5+size,0]

#B_array_fixed2 = np.zeros([840], float)
#B_array_fixed2 = B_array_noised.copy
#B_array_fixed2()[20:820] = B_array_noised[20:820] - dotResVol
#B_array_noised = np.zeros([840], float)

B_array_fixed2 = B_array_noised_reduced - dotResVol

B_array_shifted1 = np.zeros([800], float)
B_array_shifted1[1:799] = dotResVol[0:798]     #shifting the dipoles 1mm to the right
B_array_fixed3 = B_array_noised_reduced - B_array_shifted1

B_array_shifted2 = np.zeros([800], float)
B_array_shifted2[2:799] = dotResVol[0:797]     #shifting the dipoles 2mm to the right
B_array_fixed4 = B_array_noised_reduced - B_array_shifted2


B_array_shifted3 = np.zeros([800], float)
B_array_shifted3[3:799] = dotResVol[0:796]     #shifting the dipoles 3mm to the right
B_array_fixed5 = B_array_noised_reduced - B_array_shifted3


B_array_shifted4 = np.zeros([800], float)
B_array_shifted4[0:798] = dotResVol[1:799]     #shifting the dipoles 1mm to the left
B_array_fixed6 = B_array_noised_reduced - B_array_shifted4

#plt.figure(1)
#plt.plot(B_array, label="Delta B-field")
#plt.plot(dotResVol, label="dot(mk,Bnk)")
#
#fix = dotResVol - B_array
#fix = B_array - dotResVol
#
#plt.plot(fix, label="fix result")
#fix = fix**2
#plt.plot(fix, label="fix^2 result")
#plt.xlabel('Y axis [mm]')
#plt.ylabel('Bz values [T]')
#plt.legend()
#plt.grid()

plt.figure(2)
#B_array_noised_reduced = B_array_noised
plt.plot(B_array_noised_reduced, label = "Bz_noised")
plt.plot(B_array_theory_reduced, label = "Bz_ideal")
plt.plot(B_array_fixed2, label = "Fixed B-field")
plt.xlabel('Y axis [mm]')
plt.ylabel('Bz values [T]')
plt.legend()

plt.figure(3)
plt.plot(np.abs(B_array_theory_reduced - B_array_noised_reduced)  , label = "|Bz_ideal - Bz_noised| [T]")
plt.plot(np.abs(B_array_theory_reduced - B_array_fixed2), label = "|Bz_ideal - Fixed B-field| [T]")
plt.xlabel('Y axis [mm]')
plt.ylabel('Bz values [T]')
plt.legend()

#
#plt.figure(4)
#plt.plot(np.abs(B_array_theory_reduced - B_array_noised_reduced)  , label = "|Bz_ideal - Bz_noised| [T]")
#plt.plot(np.abs(B_array_theory_reduced - B_array_fixed2), label = "|Bz_ideal - Fixed B-field| [T]")
#plt.plot(np.abs(B_array_theory_reduced - B_array_fixed3), label = "|Bz_ideal - Fixed B-field (1mm right shifted)| [T]")
#plt.xlabel('Y axis [mm]')
#plt.ylabel('Bz values [T]')
#plt.legend()
#
#plt.figure(5)
#plt.plot(np.abs(B_array_theory_reduced - B_array_noised_reduced)  , label = "|Bz_ideal - Bz_noised| [T]")
#plt.plot(np.abs(B_array_theory_reduced - B_array_fixed2), label = "|Bz_ideal - Fixed B-field| [T]")
#plt.plot(np.abs(B_array_theory_reduced - B_array_fixed4), label = "|Bz_ideal - Fixed B-field (2mm right shifted)| [T]")
#plt.xlabel('Y axis [mm]')
#plt.ylabel('Bz values [T]')
#plt.legend()
#
#plt.figure(6)
#plt.plot(np.abs(B_array_theory_reduced - B_array_noised_reduced)  , label = "|Bz_ideal - Bz_noised| [T]")
#plt.plot(np.abs(B_array_theory_reduced - B_array_fixed2), label = "|Bz_ideal - Fixed B-field| [T]")
#plt.plot(np.abs(B_array_theory_reduced - B_array_fixed5), label = "|Bz_ideal - Fixed B-field (3mm right shifted)| [T]")
#plt.xlabel('Y axis [mm]')
#plt.ylabel('Bz values [T]')
#plt.legend()

#plt.figure(7)
#plt.plot(np.abs(B_array_theory_reduced - B_array_noised_reduced)  , label = "|Bz_ideal - Bz_noised| [T]")
#plt.plot(np.abs(B_array_theory_reduced - B_array_fixed6), label = "|Bz_ideal - Fixed B-field (1mm left shifted)| [T]")
#plt.xlabel('Y axis [mm]')
#plt.ylabel('Bz values [T]')
#plt.legend()
#

#prepearing the arrays:
x_val = []
y_val = []
y2_val = []
# reading the file:
fin = open('var_results.txt','r')
buffer1 = fin.read()
lines = buffer1.split('\n')
a=0
for line in lines:
    if (line== ''):
        break
    y_val.append(float(lines[a].split(',')[2]))
    x_val.append(float(lines[a].split(',')[0]))
    y2_val.append(float(lines[a].split(',')[4]))
    a=a+1
fin.close()

#plt.figure(4)
#plt.plot(x_val, y_val)
#plt.scatter(x_val, y_val)
#plt.title('Magnetic cubic side length vs. minimum target function values')
#plt.xlabel('dipole cubical side length (a) in [mm]')
#plt.ylabel('Tf_min [-]')



#plt.figure(5)
#plt.grid()
#plt.hold(True)
#plt.plot(x_val[0:3], y_val[0:3], label='dipole side length (a)=' +str(y2_val[0]) + ' [mm] ')
#plt.scatter(x_val[0:3], y_val[0:3])
#plt.plot(x_val[3:6], y_val[3:6], label='dipole side length (a)=' +str(y2_val[3]) + ' [mm] ')
#plt.scatter(x_val[3:6], y_val[3:6])
#plt.plot(x_val[6:9], y_val[6:9], label='dipole side length (a)=' +str(y2_val[6]) + ' [mm] ')
#plt.scatter(x_val[6:9], y_val[6:9])
#plt.title('Number of corrective magnets (dipoles) vs. minimum target function values')
#plt.xlabel('Space in [mm] between two corrective magnets')
#plt.ylabel('Tf_min [-]')
#plt.legend(loc='best')

