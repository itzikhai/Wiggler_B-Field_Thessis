# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 21:27:16 2017

This is the therotical and most accirate wiggler results of the B-field (no devaitons of the magnets)
@author: CHAIMOVS
"""
import numpy as np
import math

pi = 3.141592653589793
#M0=870*(10**3)

def read_rand_files():
    rand1 = np.empty([160,2],float)
    rand1 = np.zeros([160,2],float)
    
    rand2 = np.empty([160,2],float)
    rand2 = np.zeros([160,2],float)
    
    
    fin = open('rand_0_05_dev.txt', 'r')
    rand1_str = fin.read()
    rand1_list = rand1_str.split('\n')
    for line in range(160):
        rand1[line,0] = float(rand1_list[line].split(',')[0])
        rand1[line,1] = float(rand1_list[line].split(',')[1])
        
    fin = open('rand_0_025_dev.txt', 'r')
    rand2_str = fin.read()
    rand2_list = rand2_str.split('\n')
    for line in range(160):
        rand2[line,0] = float(rand2_list[line].split(',')[0])
        rand2[line,1] = float(rand2_list[line].split(',')[1])
    return rand1, rand2

rand1, rand2 = read_rand_files()
rand = np.zeros([160,2], float)
# selecting the 5% (rand1) or 2.5% (rand2) devation:
rand[:,0] = rand1[:,0]
rand[:,1] = rand1[:,1]
#overwritting random values with ones:
rand = np.ones([160,2],float)

def calc_magnetic_field_along_Y(size, sign, offset, Gap, Xb, Yb, Zb, M0):
    
    if (sign==1):
        upDn=0
    if (sign==-1):
        upDn=1
     
    Bx = np.empty([2*size,2], float)
    Bx = np.zeros([2*size,2], float)
    By = np.empty([2*size,2], float)
    By = np.zeros([2*size,2], float)
    Bz = np.empty([2*size,2], float)
    Bz = np.zeros([2*size,2], float)
    B = np.empty([2*size,2], float)
    B = np.zeros([2*size,2], float)

    mue = 12.5663*10**(-7)
    x=0
    z=sign*(Zb+Gap) # at CST its is curve #3 (aka #2)
    #z=Zb+1 # at CST it is curve #1
    eps = 0.0000001
    yy = 0
    for y in range(-size,size,1):
        Hx=0
        Hy=0
        Hz=0
        for k in range(1,3,1):
            for l in range(1,3,1):
                for m in range(1,3,1):
                    d1= (y+((-1)**l)*(Yb) + eps)
                    d2= (x+((-1)**k)*Xb)
                    d3= abs(y+((-1)**l)*(Yb) + eps)
                    d4= abs(x+((-1)**k)*Xb+ eps)
                    d5= abs(x+((-1)**k)*Xb+ eps)
                    d6= (z+((-1)**m)*Zb)
                    d7= abs(y+((-1)**l)*(Yb) + eps)
                    d8= d2
                    d9= d1
                    d10= d6
                    Hx=Hx + (-1)**(k+l+m)*np.log(d6+np.sqrt(np.power(d2,2)+np.power(d1,2)+np.power(d6,2)))
                    aa= math.atan((d5*d6)/(d7*np.sqrt(np.power(d8,2)+np.power(d9,2)+np.power(d10,2))))
                    Hy = Hy + ((-1)**(k+l+m)*(d1*d2)/(d3*d4))*aa       
                    Hz = Hz + (-1)**(k+l+m)*np.log(d2+np.sqrt(np.power(d2,2)+np.power(d1,2)+np.power(d6,2)))
                    
        Bx[yy,1] = (mue*Hx*M0*rand[offset/5,upDn])/(4*pi)
        By[yy,1] = mue*(-1)*Hy*M0*rand[offset/5,upDn]/(4*pi)
        Bz[yy,1] = mue*Hz*M0*rand[offset/5,upDn]/(4*pi)
       
        
        B[yy,0]= Bx[yy, 0] = By[yy,0] = Bz[yy, 0] = yy
        B[yy,1]= np.sqrt(np.power(Bx[yy,1],2) + np.power(By[yy,1],2) + np.power(Bz[yy,1],2))
        
        yy = yy +1
    
    return By[:,1], Bz[:,1]

def calc_magnetic_field_along_opsY(size, sign, offset, Gap, Xb, Yb, Zb, M0):
    
    if (sign==1):
        upDn=0
    if (sign==-1):
        upDn=1

    Bx = np.empty([2*size,2], float)
    Bx = np.zeros([2*size,2], float)
    By = np.empty([2*size,2], float)
    By = np.zeros([2*size,2], float)
    Bz = np.empty([2*size,2], float)
    Bz = np.zeros([2*size,2], float)
    B = np.empty([2*size,2], float)
    B = np.zeros([2*size,2], float)
    
    mue = 12.5663*10**(-7)
    x=0
    z=sign*(Zb+Gap) # at CST its is curve #3 (aka #2)
    #z=Zb+1 # at CST it is curve #1
    eps = 0.0000001
    yy = 0
    for y in range(-size,size,1):
        Hx=0
        Hy=0
        Hz=0
        for k in range(1,3,1):
            for l in range(1,3,1):
                for m in range(1,3,1):
                    d1= (-y+((-1)**l)*(Yb) + eps)
                    d2= (x+((-1)**k)*Xb)
                    d3= abs(-y+((-1)**l)*(Yb) + eps)
                    d4= abs(x+((-1)**k)*Xb+ eps)
                    d5= abs(x+((-1)**k)*Xb+ eps)
                    d6= (-z+((-1)**m)*Zb)
                    d7= abs(-y+((-1)**l)*(Yb) + eps)
                    d8= d2
                    d9= d1
                    d10= d6
                    Hx=Hx + (-1)**(k+l+m)*np.log(d6+np.sqrt(np.power(d2,2)+np.power(d1,2)+np.power(d6,2)))
                    aa= math.atan((d5*d6)/(d7*np.sqrt(np.power(d8,2)+np.power(d9,2)+np.power(d10,2))))
                    Hy = Hy + ((-1)**(k+l+m)*(d1*d2)/(d3*d4))*aa       
                    Hz = Hz + (-1)**(k+l+m)*np.log(d2+np.sqrt(np.power(d2,2)+np.power(d1,2)+np.power(d6,2)))

        Bx[yy,1] = (mue*Hx*M0*rand[offset/5,upDn])/(4*pi)
        By[yy,1] = mue*(-1)*Hy*M0*rand[offset/5,upDn]/(4*pi)
        Bz[yy,1] = mue*Hz*M0*rand[offset/5,upDn]/(4*pi)
       
        
        B[yy,0]= Bx[yy, 0] = By[yy,0] = Bz[yy, 0] = yy
        B[yy,1]= np.sqrt(np.power(Bx[yy,1],2) + np.power(By[yy,1],2) + np.power(Bz[yy,1],2))
        
        yy = yy +1
    
    return -By[:,1], -Bz[:,1]

def calc_magnetic_field_along_Z(size, sign, offset, Gap, Xb, Yb, Zb, M0):
    if (sign==1):
        upDn=0
    if (sign==-1):
        upDn=1

    Bx = np.empty([2*size,2], float)
    Bx = np.zeros([2*size,2], float)
    By = np.empty([2*size,2], float)
    By = np.zeros([2*size,2], float)
    Bz = np.empty([2*size,2], float)
    Bz = np.zeros([2*size,2], float)
    B = np.empty([2*size,2], float)
    B = np.zeros([2*size,2], float)
    
    mue = 12.5663*10**(-7)
    x=0
    z=sign*(Zb+Gap) # at CST its is curve #3 (aka #2)
    #z=Zb+1 # at CST it is curve #1
    eps = 0.0000001
    yy = 0
    for y in range(-size,size,1):
        Hx=0
        Hy=0
        Hz=0
        for k in range(1,3,1):
            for l in range(1,3,1):
                for m in range(1,3,1):
                    d1= (z+((-1)**l)*(Zb) + eps)
                    d2= (x+((-1)**k)*Xb)
                    d3= abs(z+((-1)**l)*(Zb) + eps)
                    d4= abs(x+((-1)**k)*Xb+ eps)
                    d5= abs(x+((-1)**k)*Xb+ eps)
                    d6= (-y+((-1)**m)*Yb)
                    d7= abs(z+((-1)**l)*(Zb) + eps)
                    d8= d2
                    d9= d1
                    d10= d6
                    Hx=Hx + (-1)**(k+l+m)*np.log(d6+np.sqrt(np.power(d2,2)+np.power(d1,2)+np.power(d6,2)))
                    aa= math.atan((d5*d6)/(d7*np.sqrt(np.power(d8,2)+np.power(d9,2)+np.power(d10,2))))
                    Hy = Hy + ((-1)**(k+l+m)*(d1*d2)/(d3*d4))*aa       
                    Hz = Hz + (-1)**(k+l+m)*np.log(d2+np.sqrt(np.power(d2,2)+np.power(d1,2)+np.power(d6,2)))
                    
       
        Bx[yy,1] = (mue*Hx*M0*rand[offset/5,upDn])/(4*pi)
        By[yy,1] = mue*(-1)*Hy*M0*rand[offset/5,upDn]/(4*pi)
        Bz[yy,1] = mue*Hz*M0*rand[offset/5,upDn]/(4*pi)
        
        
        B[yy,0]= Bx[yy, 0] = By[yy,0] = Bz[yy, 0] = yy
        B[yy,1]= np.sqrt(np.power(Bx[yy,1],2) + np.power(By[yy,1],2) + np.power(Bz[yy,1],2))
        
        yy = yy +1
    
    return -Bz[:,1], By[:,1]

def calc_magnetic_field_along_opsZ(size, sign, offset, Gap, Xb, Yb, Zb, M0):
    if (sign==1):
        upDn=0
    if (sign==-1):
        upDn=1
        
    Bx = np.empty([2*size,2], float)
    Bx = np.zeros([2*size,2], float)
    By = np.empty([2*size,2], float)
    By = np.zeros([2*size,2], float)
    Bz = np.empty([2*size,2], float)
    Bz = np.zeros([2*size,2], float)
    B = np.empty([2*size,2], float)
    B = np.zeros([2*size,2], float)
    
    mue = 12.5663*10**(-7)
    x=0
    z=sign*(Zb+Gap) # at CST its is curve #3 (aka #2)
    #z=Zb+1 # at CST it is curve #1
    eps = 0.0000001
    yy = 0
    for y in range(-size,size,1):
        Hx=0
        Hy=0
        Hz=0
        for k in range(1,3,1):
            for l in range(1,3,1):
                for m in range(1,3,1):
                    d1= (-z+((-1)**l)*(Zb) + eps)
                    d2= (x+((-1)**k)*Xb)
                    d3= abs(-z+((-1)**l)*(Zb) + eps)
                    d4= abs(x+((-1)**k)*Xb+ eps)
                    d5= abs(x+((-1)**k)*Xb+ eps)
                    d6= (y+((-1)**m)*Yb)
                    d7= abs(-z+((-1)**l)*(Zb) + eps)
                    d8= d2
                    d9= d1
                    d10= d6
                    Hx=Hx + (-1)**(k+l+m)*np.log(d6+np.sqrt(np.power(d2,2)+np.power(d1,2)+np.power(d6,2)))
                    aa= math.atan((d5*d6)/(d7*np.sqrt(np.power(d8,2)+np.power(d9,2)+np.power(d10,2))))
                    Hy = Hy + ((-1)**(k+l+m)*(d1*d2)/(d3*d4))*aa       
                    Hz = Hz + (-1)**(k+l+m)*np.log(d2+np.sqrt(np.power(d2,2)+np.power(d1,2)+np.power(d6,2)))

        Bx[yy,1] = (mue*Hx*M0*rand[offset/5,upDn])/(4*pi)
        By[yy,1] = mue*(-1)*Hy*M0*rand[offset/5,upDn]/(4*pi)
        Bz[yy,1] = mue*Hz*M0*rand[offset/5,upDn]/(4*pi)
        
        
        B[yy,0]= Bx[yy, 0] = By[yy,0] = Bz[yy, 0] = yy
        B[yy,1]= np.sqrt(np.power(Bx[yy,1],2) + np.power(By[yy,1],2) + np.power(Bz[yy,1],2))
        
        yy = yy +1
       
    return Bz[:,1], -By[:,1]