n = 5

for i in range (1, n):
    for j in range(n+1,i,-1):
        print(' ',end='')    
    for k in range(1 , i+1):    
        print('*',end=' ')
    print('')


for i in range (n, 1-1,-1):
    for j in range(n+1,i,-1):
        print(' ',end='') 
    for k in range(1,i+1):  
        print('*',end = ' ')
    print(' ')
