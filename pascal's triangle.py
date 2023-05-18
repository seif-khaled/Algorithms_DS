import math 
import random 

def genrate_nth_pascal_triangle(N):
    x=[]
    for i in range(N):
        x.append([])
    column=1
    for i in range(N):
        for j in range(column):
            if j==0 or i==j:
                x[i].append(1)
                
            else:
                x[i].append(x[i-1][j-1]+x[i-1][j])
        column+=1
    return x
        
print(genrate_nth_pascal_triangle(3))    



    