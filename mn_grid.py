# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 17:40:16 2018

@author: cecil
"""

import numpy as np

n=7
m=10
d = n+m

if ((n+m) % 2) == 1:
    eps = 1
else: 
    eps = 0
if int(2*(n+m)/3)%2==0:
    k = int(2*(n+m)/3)
else:
    k = int(2*(n+m)/3)-1
    
print('m={}, n={}, k={}'.format(m,n,k))
mat = np.zeros((n+1,m+1))

#for cross
for x in range(0,int(n/2)):
    mat[int(n/2),int(n/2)-x-1]= 2*(x+1)
    mat[int(n/2)-1-x,int(n/2)]= 2*(x+1)
    mat[int(n/2),int(n/2)+2+x-1]= 2*(x+1)
    mat[int(n/2)+1+x,int(n/2)]= 2*(x+1)

#for those that appear 3 times
for x in range(0,int((k-n)/2)+1):
    a = 2*int((n-1)/2)+2+2*x
    mat[0,int(a/2)] = a
    mat[int(a/2),0] = a
    mat[n,int(a/2)+(a-n)]=a

#largest numbers 
for x in range(int((n+m-k)/2)):
    mat[0+x,m] = d-2*x
    mat[n,0+x] = d-2*x  
    mat[0,0+x] = d-1-2*x
    mat[n-1-x,m] = d-1-2*x

if int(n/2)-1> int((n+m-k)/2):
    for x in range(int((n+m-k)/2),(int(n/2)-1)):
        if eps==0:
            mat[0,0+x] = d-1-2*x
            mat[n-1-x,m] = d-1-2*x
        else:
            mat[0+x,m] = d-2*x
            mat[n,0+x] = d-2*x  
            
mat[n*eps,int(n/2)-1] = d-2*(int(n/2)-1)-1+eps
mat[(int(n/2)-1)+2-2*eps,m-1+eps] = d-2*(int(n/2)-1)-1+eps


for x in range(0,int(n/2)):
    mat[n*eps+x*(-1)**eps+1*(-1)**eps,int(n/2)-1] = d-2*(int(n/2)-1)-1+eps-2-2*x
    mat[(int(n/2)-1)+2-2*eps,m-2+eps-x] = d-2*(int(n/2)-1)-1+eps-2-2*x 

small_nums = (d-2*(int(n/2)-1)-1+eps-2-2*(int(n/2)-1))
for x in range(1,small_nums,2):
    mat[1,int(n/2)+1+int(x/2)] = small_nums-x-1
    mat[1,int(n/2)+1+int(small_nums/2)+int((x-1)/2)] = x


#print('The following numbers were missed: ',list(set(np.unique(mat).astype(int))-set(range(0,n+m+1))))

for p in range(len(np.flip(mat.astype(int),0))):
    print(np.flip(mat.astype(int),0)[p])
#np.savetxt("mat4.csv", np.flip(mat.astype(int),0), delimiter=",")

#pd.DataFrame(np.flip(mat.astype(int),0)).to_csv('mat4.csv',sep=',', index=False, header=False)
