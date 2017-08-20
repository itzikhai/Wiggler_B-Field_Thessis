# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 01:05:20 2016

Continuation of the 'calc_magnetic_field_v2f.py' which calcuates the B-field along the Wiggler.
This script make a usage of the m_results (obtained from 'algorithm_v3.py') which are the obtained M values of the fixing magnets elements.

@author: CHAIMOVS
"""

def calc_fixed_field(size):    
    import numpy as np
    import matplotlib.pyplot as plt
    import math
    import calc_magnetic_field as cmf   #our user defined functions (should be located at the folder where the current script is running in)
    import calc_magnetic_field_theo as cmft

#*****************************    
    period = 40     # this is the number of periods for which wiggler will be desinged and simualtion to be calculated
#    size = 10       # twice the size of window which B field will be calculated: [-size, size]
#*****************************    
    Gap = 8.71/2    # The Gap is middle plane (between upper and lower arms of wiggler) for which the B fields will be calculated
    
    j=0
    
    # loading the 'm_results.txt' data file:
    M0_arr = np.empty([period*4,1], float)
    M0_arr = np.zeros([period*4,1], float)
    
    fin = open('m_results.txt', 'r')
    for line in range(period*4):
        M0_arr[line,0] = float(fin.readline())
    fin.close()
    
    
    Xb=30/2
    Yb=5/2
    Zb=15/2

      
    M0=970*(10**3)
    
    wiggler_size = 900 #it is 800mm but will add [size] mm at begining and [size] mm at the end (to let field decay properly at the edges).
    # This variablier is overwriiting the second since this one is adaptive to number of magnet periods and add the size from stgart and at the end:
    wiggler_size = period*4*5+size*2
    
    By = np.empty([wiggler_size,1], float)
    By = np.zeros([wiggler_size,1], float)
    Bz = np.empty([wiggler_size,1], float)
    Bz = np.zeros([wiggler_size,1], float)
    
    
    
    
    for Ti in range(0,period,1):
        
        A,B = cmf.calc_magnetic_field_along_Z(size, -1, j*5, Gap, Xb, Yb, Zb, M0 )
        Grid_start = j*5    #updating Grid
        Grid_stop = size*2 + Grid_start
        By[Grid_start:Grid_stop,0] = By[Grid_start:Grid_stop,0] + A
        Bz[Grid_start:Grid_stop,0] = Bz[Grid_start:Grid_stop,0] + B       
        A,B = cmf.calc_magnetic_field_along_Z(size, 1, j*5, Gap, Xb, Yb, Zb, M0)
        By[Grid_start:Grid_stop,0] = By[Grid_start:Grid_stop,0] + A
        Bz[Grid_start:Grid_stop,0] = Bz[Grid_start:Grid_stop,0] + B
        if M0_arr[j,0] > 0:
            A,B = cmft.calc_magnetic_field_along_Z(size, 1, j*5, 0 , 1, 1, 1, M0_arr[j,0]) #contribution of the small magnet
        else:
            A,B = cmft.calc_magnetic_field_along_opsZ(size, 1, j*5,0, 1, 1, 1, -M0_arr[j,0]) ##contribution of the small magnet
        By[Grid_start:Grid_stop,0] = By[Grid_start:Grid_stop,0] + A
        Bz[Grid_start:Grid_stop,0] = Bz[Grid_start:Grid_stop,0] + B     
        j = j + 1           #updating Grid
        Grid_start = j*5
        Grid_stop = size*2 + Grid_start
        
        A,B = cmf.calc_magnetic_field_along_Y(size,-1, j*5, Gap, Xb, Yb, Zb, M0)
        By[Grid_start:Grid_stop,0] = By[Grid_start:Grid_stop,0] + A
        Bz[Grid_start:Grid_stop,0] = Bz[Grid_start:Grid_stop,0] + B     
        A,B = cmf.calc_magnetic_field_along_opsY(size,1, j*5, Gap, Xb, Yb, Zb, M0)
        By[Grid_start:Grid_stop,0] = By[Grid_start:Grid_stop,0] + A
        Bz[Grid_start:Grid_stop,0] = Bz[Grid_start:Grid_stop,0] + B
        if M0_arr[j,0] < 0:
            A,B = cmft.calc_magnetic_field_along_opsY(size, 1, j*5, 0, 1, 1, 1, -M0_arr[j,0]) ##contribution of the small magnet
        else:
            A,B = cmft.calc_magnetic_field_along_Y(size, 1, j*5, 0 , 1, 1, 1, M0_arr[j,0]) #contribution of the small magnet
        By[Grid_start:Grid_stop,0] = By[Grid_start:Grid_stop,0] + A
        Bz[Grid_start:Grid_stop,0] = Bz[Grid_start:Grid_stop,0] + B    
        j = j + 1           #updating Grid
        Grid_start = j*5
        Grid_stop = size*2 + Grid_start
        
        A,B = cmf.calc_magnetic_field_along_opsZ(size, -1, j*5, Gap , Xb, Yb, Zb, M0)
        By[Grid_start:Grid_stop,0] = By[Grid_start:Grid_stop,0] + A
        Bz[Grid_start:Grid_stop,0] = Bz[Grid_start:Grid_stop,0] + B      
        A,B = cmf.calc_magnetic_field_along_opsZ(size, 1, j*5, Gap , Xb, Yb, Zb, M0)
        By[Grid_start:Grid_stop,0] = By[Grid_start:Grid_stop,0] + A
        Bz[Grid_start:Grid_stop,0] = Bz[Grid_start:Grid_stop,0] + B
        if M0_arr[j,0] < 0:
            A,B = cmft.calc_magnetic_field_along_opsZ(size, 1, j*5 , 0 , 1, 1, 1, -M0_arr[j,0]) ##contribution of the small magnet
        else:
            A,B = cmft.calc_magnetic_field_along_Z(size, 1, j*5, 0 , 1, 1, 1, M0_arr[j,0]) #contribution of the small magnet
        By[Grid_start:Grid_stop,0] = By[Grid_start:Grid_stop,0] + A
        Bz[Grid_start:Grid_stop,0] = Bz[Grid_start:Grid_stop,0] + B
        j = j + 1           #updating Grid
        Grid_start = j*5
        Grid_stop = size*2 + Grid_start
        
        A, B = cmf.calc_magnetic_field_along_opsY(size, -1, j*5, Gap, Xb, Yb, Zb, M0)
        By[Grid_start:Grid_stop,0] = By[Grid_start:Grid_stop,0] + A
        Bz[Grid_start:Grid_stop,0] = Bz[Grid_start:Grid_stop,0] + B 
        A, B = cmf.calc_magnetic_field_along_Y(size, 1, j*5, Gap, Xb, Yb, Zb, M0)
        By[Grid_start:Grid_stop,0] = By[Grid_start:Grid_stop,0] + A
        Bz[Grid_start:Grid_stop,0] = Bz[Grid_start:Grid_stop,0] + B
        if M0_arr[j,0] > 0:
            A, B = cmft.calc_magnetic_field_along_Y(size, 1, j*5, 0, 1, 1, 1, -M0_arr[j,0]) ##contribution of the small magnet
        else:
            A, B = cmft.calc_magnetic_field_along_opsY(size, 1, j*5, 0, 1, 1, 1, M0_arr[j,0]) #contribution of the small magnet            
        By[Grid_start:Grid_stop,0] = By[Grid_start:Grid_stop,0] + A
        Bz[Grid_start:Grid_stop,0] = Bz[Grid_start:Grid_stop,0] + B
        j = j + 1       
    
    #save results in a file on the disk:
    fout = open('Bz.txt', 'w')
    for line in range(wiggler_size):
        fout.write(str(line) +', ' + str(Bz[line,0])+'\n')
    fout.close()
    
    Bz_before = Bz
    
    #plotting the results:
    
    #plt.plot(By, label='By')    
    #plt.subplot(2,1,2)
    #plt.figure(2)
    #plt.plot(Bz, label='Bz After fix')
    #plt.title('noise generated')
    #plt.legend()
    #plt.grid(1)
    #plt.show()
    # Generating the B array which is the B field obtained but in every 5mm (sample it every 5mm to be used with the fixinf algortihm)
    B_array = Bz[range(size,period*5*4+size,5),0]
    #save results in a file on the disk:
    fout = open('B_array.txt', 'w')
    for line in range(period*4):
        fout.write(str(B_array[line])+'\n')
    fout.close()
    
    #plt.figure(2) 
    #plt.plot(B_array, label='Bz_array - in 5 mm jumps starting from z=2mm')
    #plt.title('with noise generated')
    #plt.legend()
    #plt.grid(1)
    return Bz
    
