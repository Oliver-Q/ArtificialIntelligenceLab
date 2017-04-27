from lab3.sa_function import *
from lab3.search import *

class NQueensProblem(Problem):

    """The problem of placing N queens on an NxN board with none attacking
    each other.  A state is represented as an N-element array, where
    a value of r in the c-th entry means there is a queen at column c,
    row r, and a value of None means that the c-th column has not been
    filled in yet.  We fill in columns left to right.
    >>> depth_first_tree_search(NQueensProblem(8))
    <Node [7, 3, 0, 2, 5, 1, 6, 4]>
    """

    def __init__(self, N):
        self.N = N
        "initial state is randomly generated"
        self.initial = random.sample(range(N), N)

    def actions(self, state):
        "gengerate actions actd which contains all possible moves of each queen"
        actm=[[0] * (self.N-1)] * (self.N)
        for i in range(self.N):
            seq8=list(range(self.N))
            seq8.remove(state[i])
            actm[i]=seq8

        actd=[[0] * 2] * (self.N*(self.N-1))
        k=0
        for i in range(self.N):
            for j in range(self.N-1):
                actd[k]=[i,actm[i][j]]
                k+=1

        return actd

    def result(self, state, actd):
        "move the queen in i_th col"
        new = state[:]
        for i in range(self.N):
            if actd[0]==i:
                new[i]=actd[1]

        return new
   
    def value(self, state):
        "return 20 minus the number of pairs of attacking queen"
        return -sa_value(state)+20







