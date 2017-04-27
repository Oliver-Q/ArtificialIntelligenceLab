from lab3.search import *
import numpy as np

def sa_value(state):
    N=len(state)
    smt = np.zeros((N,N))
    mvalue1 = 0
    mvalue2 = 0
    mvalue3 = 0
    fac = lambda x: x*fac(x-1) if x > 1 else 1
    for i in range(N):
        smt[state[i],i]=1

    rows = smt.sum(1)
    for i in range(len(rows)):
        if rows[i]>1:
            mvalue1 = mvalue1+fac(rows[i])/fac(rows[i]-2)/2
            
    diag1=[0 for i in range(N+N)]
    for i in range(N):
        for j in range(N-i):
            diag1[i]=diag1[i]+smt[i+j,j]
        for j in range(i+1):
            diag1[i+N]=diag1[i+N]+smt[i-j,j]

    diag2=[0 for i in range(N+N-2)]
    for j in range(1,N):
        for i in range(N-j):
            diag2[j-1]=diag2[j-1]+smt[i,j+i]
            #print(i,j+i)
        for i in range(N-j):
            diag2[j-1+N-1]=diag2[j-1+N-1]+smt[N-1-i,j+i]

    for i in range(len(diag1)):
        if diag1[i]>1:
            mvalue2 = mvalue2+fac(diag1[i])/fac(diag1[i]-2)/2

    for i in range(len(diag2)):
        if diag2[i]>1:
            mvalue3 = mvalue3+fac(diag2[i])/fac(diag2[i]-2)/2
        
    return mvalue1+mvalue2+mvalue3














