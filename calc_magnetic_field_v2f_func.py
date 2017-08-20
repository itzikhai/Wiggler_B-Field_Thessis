# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 01:05:20 2016

@author: CHAIMOVS
"""

#**********************    
period = 40     # this is the number of periods for which wiggler will be desinged and simualtion to be calculated
#size = 10       # twice the size of window which B field will be calculated: [-size, size]
#**********************

def calc_field(size):
    import numpy as np
    import calc_magnetic_field as cmf   #our user defined functions (should be located at the folder where the current script is running in)
    Gap = 8.71/2    # The Gap is middle plane (between upper and lower arms of wiggler) for which the B fields will be calculated   
    j=0
    
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
        
        A,B = cmf.calc_magnetic_field_along_Z(size, -1, j*5, Gap, Xb, Yb, Zb, M0)
        Grid_start = j*5    #updating Grid
        Grid_stop = size*2 + Grid_start
        By[Grid_start:Grid_stop,0] = By[Grid_start:Grid_stop,0] + A
        Bz[Grid_start:Grid_stop,0] = Bz[Grid_start:Grid_stop,0] + B
        
        A,B = cmf.calc_magnetic_field_along_Z(size, 1, j*5, Gap, Xb, Yb, Zb, M0)
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
        j = j + 1           #updating Grid
        Grid_start = j*5
        Grid_stop = size*2 + Grid_start
        
        A,B = cmf.calc_magnetic_field_along_opsZ(size, -1, j*5, Gap, Xb, Yb, Zb, M0)
        By[Grid_start:Grid_stop,0] = By[Grid_start:Grid_stop,0] + A
        Bz[Grid_start:Grid_stop,0] = Bz[Grid_start:Grid_stop,0] + B
        
        A,B = cmf.calc_magnetic_field_along_opsZ(size, 1, j*5, Gap, Xb, Yb, Zb, M0)
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
    #plt.plot(Bz, label='Bz Before fix')
    #plt.title('noise generated')
    #plt.legend()
    #plt.grid(1) 
    # Generating the B array which is the B field obtained but in every 5mm (sample it every 5mm to be used with the fixinf algortihm)
    B_array = Bz[range(size,wiggler_size-2*size+size,5),0]
    #save results in a file on the disk:
    fout = open('B_array.txt', 'w')
    for line in range(period*4):
        fout.write(str(B_array[line])+'\n')
    fout.close()
    
    return Bz
    #plt.figure(2) 
    #plt.plot(B_array, label='Bz_array - in 5 mm jumps starting from z=2mm')
    #plt.title('with noise generated')
    #plt.legend()
    #plt.grid(1)
    
    
def calc_field_theo(size):
    import numpy as np
    import calc_magnetic_field_theo as cmf   #our user defined functions (should be located at the folder where the current script is running in)
    
    Gap = 8.71/2    # The Gap is middle plane (between upper and lower arms of wiggler) for which the B fields will be calculated   
    j=0
    
    Xb=20/2
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
        
        A,B = cmf.calc_magnetic_field_along_Z(size, -1, j*5, Gap, Xb, Yb, Zb, M0)
        Grid_start = j*5    #updating Grid
        Grid_stop = size*2 + Grid_start
        By[Grid_start:Grid_stop,0] = By[Grid_start:Grid_stop,0] + A
        Bz[Grid_start:Grid_stop,0] = Bz[Grid_start:Grid_stop,0] + B
        
        A,B = cmf.calc_magnetic_field_along_Z(size, 1, j*5, Gap, Xb, Yb, Zb, M0)
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
        j = j + 1           #updating Grid
        Grid_start = j*5
        Grid_stop = size*2 + Grid_start
        
        A,B = cmf.calc_magnetic_field_along_opsZ(size, -1, j*5, Gap, Xb, Yb, Zb, M0)
        By[Grid_start:Grid_stop,0] = By[Grid_start:Grid_stop,0] + A
        Bz[Grid_start:Grid_stop,0] = Bz[Grid_start:Grid_stop,0] + B
        
        A,B = cmf.calc_magnetic_field_along_opsZ(size, 1, j*5, Gap, Xb, Yb, Zb, M0)
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
    #plt.plot(Bz, label='Bz Before fix')
    #plt.title('noise generated')
    #plt.legend()
    #plt.grid(1) 
    # Generating the B array which is the B field obtained but in every 5mm (sample it every 5mm to be used with the fixinf algortihm)
    B_array = Bz[range(size,wiggler_size-size,5),0]
    #save results in a file on the disk:
    fout = open('B_array.txt', 'w')
    for line in range(period*4):
        fout.write(str(B_array[line])+'\n')
    fout.close()
    
    return Bz
    #plt.figure(2) 
    #plt.plot(B_array, label='Bz_array - in 5 mm jumps starting from z=2mm')
    #plt.title('with noise generated')
    #plt.legend()
    #plt.grid(1)