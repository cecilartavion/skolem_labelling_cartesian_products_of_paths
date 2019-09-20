'''
The following program is provided to make a construction easier to understand 
in Section 3 of the paper titled "Skolem Number of Cycles and Grid Graphs" by 
John Asplund and Braxton Carrigan. 

For simplicity, the only labels provided are those that appear more than once.
All comments that use unfamiliar terminology is explained in the paper for 
which this program assists. See the companion paper for more details.

Note that mat[value1,value2] is located at the coordinate (value2,value1) 
according to what is written in the companion paper.
'''

import sys
import numpy as np
from ast import literal_eval

def main():
    def topleft_blue(x):
        if x>a+b-2*int((a-1)/2)-2:
            return a-1,int((a+b-2)/2)-int(x/2)
        elif x>a+b-2*int((a-1)/2)-3-((a+b)%2)*2:
            return a-1+int(x/2)-int((a+b-2*int((a-1)/2))/2),int((a-1)/2)-1
        
    def bottomright_blue(x):
        if x>a+b-2*int((a-1)/2):
            return int((a+b-2)/2)-int(x/2),b-1
        else:
            return int((a-1)/2)-1,b-1-int((a+b-2*int((a-1)/2))/2)+int(x/2)
        
    def bottomleft_orange(x):
        if x>a+b-2*int((a-1)/2)-3:
            return 0,int((a+b-2)/2)-int((x+1)/2)
        elif x>a+b-2*int((a-1)/2)-4:
            return int((a+b-2*int((a-1)/2))/2)-int((x+1)/2),int((a-1)/2)-1
        
    def topright_orange(x):
        if x>a+b-2*int((a-1)/2):
            return a-2-int((a+b-2)/2)+int((x+1)/2),b-1
        else:
            return int((a-1)/2)+1,b-1-int((a+b-2*int((a-1)/2))/2)+int((x+1)/2)-1+((a-1)%2)
    
    def top_red(x):
        return a-1,int(3*x/2-a+1)
    
    def bottom_red(x):
        return 0,int(x/2)
    
    def topleft_red(x):
        return int(x/2),0
    
    def leftsmall_blue(x):
        return int((a-1)/2)-1,-2+int((a+b-2*int((a-1)/2)-1)/2)-int(x/2)-((a+b)%2)*((a-1)%2)
    
    def leftsmall_orange(x):
        return int((a-1)/2)+1,-2+int((a+b-2*int((a-1)/2)-1)/2)-int(x/2)
    
    if b<=2*a:
        k = 2*int((a+b-2)/3)
    else:
        k=2*a-2
    
    print('a={}, b={}, k={}'.format(a,b,k))
    
    #Create a matrix of only 0's.
    mat = np.zeros((a,b))
    
    #Create the numbers that appear 4 times in the grid.
    for t in range(int((a-1)/2)):
        mat[int((a-1)/2),int((a-1)/2)-t-1]= 2*(t+1)
        mat[int((a-1)/2)-1-t,int((a-1)/2)]= 2*(t+1)
        mat[int((a-1)/2),int((a-1)/2)+2+t-1]= 2*(t+1)
        mat[int((a-1)/2)+1+t,int((a-1)/2)]= 2*(t+1)
       
    #For the odd numbers less than a+b-2*int((a-1)/2)-2 that appear twice, we place them as follows:
    for t in range(1,(a+b-2*int((a-1)/2)-2),2):
        if ((a+b)%2)==1:
            if int((a-1)/2)==leftsmall_blue(t)[1]:
                mat[tuple(leftsmall_blue(t)+np.array((-1,1)))]=t
            else:
                mat[leftsmall_blue(t)]=t
        #If a+b is even enter this else statement.
        else:
            if int((a-1)/2)==leftsmall_orange(t)[1]:
                mat[tuple(leftsmall_orange(t)+np.array((1,1)))]=t
            elif leftsmall_orange(t)[1]==0:
                mat[tuple(leftsmall_orange(t)+np.array((1,1)))] = t
            else:
                mat[leftsmall_orange(t)]=t
        
    #If the largest number in the grid is odd, put the odd numbers that appear 
    # three times on the blue lines and the even numbers that appear twice on the 
    # orange lines. Note that a+b-2 is the largest integer in the grid that 
    # appears more than once. 
    #if ((a+b-2)%2)==1:
    #For the numbers that appear twice.
    for t in range(1-((a+b-1)%2),a+b-1,2):
        if t>a+b-2*int((a-1)/2)-3-((a+b)%2)*2*((a-1)%2):
            if ((a+b)%2)==1:
                mat[topleft_blue(t)] = t
            if ((a+b)%2)==0:
                mat[bottomleft_orange(t-1)]=t-1
        #If there is an overlap with the cross, make the appropriate adjustment.
    #    print(int((a-1)/2)==bottomright_blue(t)[1],int((a-1)/2)==bottomright_blue(t)[1]-((a+b)%2)*(a-1%2),t,bottomright_blue(t),tuple(bottomright_blue(t)+np.array((-1,-1))))
        if int((a-1)/2)==bottomright_blue(t)[1] and ((a+b)%2)==1:
            print(bottomright_blue(t),t)
            mat[tuple(bottomright_blue(t)+np.array((-1,-1)))] = t
        elif int((a-1)/2)==topright_orange(t)[1]-((a+b)%2)*(a%2) and ((a+b)%2)==0:
            mat[tuple(topright_orange(t)+np.array((1,-1)))] = t-1
        else:
            if ((a+b)%2)==1:
                mat[bottomright_blue(t)] = t
            if ((a+b)%2)==0 and t>0:
                mat[topright_orange(t-1)] = t-1
            
        if t-1>k:
            if ((a+b)%2)==1:
                mat[bottomleft_orange(t-1)]=t-1
                mat[topright_orange(t-1)]=t-1
            if ((a+b)%2)==0:
                mat[topleft_blue(t)] = t
                mat[bottomright_blue(t)] = t
      
    #Run the following for loop to construct the even number that appear three times.          
    for t in range(a+(a%2),k+1,2):
        mat[top_red(t)]=t
        mat[bottom_red(t)]=t
        mat[topleft_red(t)]=t
                    
    
    
    #The following line of code will flip the matrix to the correct orientation.
    num_digits = len(str(int(mat.max())))
    for p in range(len(np.flip(mat.astype(int),0))):
        print('['+' '.join('%0*s' % (num_digits,i) for i in np.flip(mat.astype(int),0)[p].astype(str))+']')
    
    #The following for loop is for checking to make sure the correct number of 
    # numbers appears in the matrix
    for i in range(1,a+b-1):
        if (i%2)==1:
            if list(mat.flatten()).count(i)!=2:
                print('The number',i,'does not appear 2 times in matrix.')
        if (i%2)==0 and i<a-1:
            if list(mat.flatten()).count(i)!=4:
                print('The number',i,'does not appear 4 times in matrix.')
        if (i%2)==0 and i>=a and i<=k:
            if list(mat.flatten()).count(i)!=3:
                print('The number',i,'does not appear 3 times in matrix.')    
        if (i%2)==0 and i>k:
            if list(mat.flatten()).count(i)!=2:
                print('The number',i,'does not appear 2 times in matrix.')    
        
        row,col = np.where(mat==i)
        row = list(row)
        col = list(col)
        for j in range(len(row)):
            for l in range(len(row)):
                if j!=l:
                    if i!=abs(row[j]-row[l])+abs(col[j]-col[l]):
                        print('The distance between two value numbered',i,'are not',i,'apart from each other.',abs(row[j]-row[l])+abs(col[j]-col[l]),(row[j],col[j]),(row[l],col[l]))
     
if __name__== "__main__":
    try:
        a=literal_eval(sys.argv[1])
        b=literal_eval(sys.argv[2])
        if isinstance(a,int) and isinstance(b,int) and a>0 and b>0:
            main()
        else:
            print('You need two arguments in the script that are both positive integers.',
              "An example could be the script 'run ab_grid.py 9 12' without quotes.")
    except: 
        print('You need two arguments in the script that are both positive integers.',
              "An example could be the script 'run ab_grid.py 9 12' without quotes.")
