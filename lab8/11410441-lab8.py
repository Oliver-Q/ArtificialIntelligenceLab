from planning import *
from utils import *
import copy

airc=air_cargo()
aira=airc.actions

cset=['C1','C2']
pset=['P1','P2']
lset=['SFO','JFK']

aload=[]
for c in cset:
    for p in pset:
        for loc in lset:
            aload.append(expr('Load'+'('+c+','+p+','+loc+')'))

aunload=[]
for c in cset:
    for p in pset:
        for loc in lset:
            aunload.append(expr('Unload'+'('+c+','+p+','+loc+')'))

afly=[]
for p in pset:
    for loc1 in lset:
        for loc2 in lset:
            afly.append(expr('Fly'+'('+p+','+loc1+','+loc2+')'))

myacts= aload[:]
myacts.extend(aunload[:])
myacts.extend(afly[:])


def plan_search(pdllp,myacts,frontier):

    frontier.append(pdllp)
    explored = []

    for i in range(124):
        print(i)

        node=frontier.pop()
        if node.goal_test():
            print('Succeed')
            return node

        def pexpand(prob,myacts):
            cnodes=[]
            for ia in myacts:
                try:
                    ipro=copy.deepcopy(prob)
                    ipro.act(ia)
                except:
                    print('*',end='')
                else:
                    cnodes.append(ipro)
                    print(ia)
            return cnodes
        childnode=pexpand(node,myacts)

        for cnode in childnode:
            dlen=0
            for ekb in explored:
                if list (set(cnode.kb.clauses).difference(set(ekb)))!=[]:
                    dlen=dlen+1
            if dlen == len(explored) and cnode not in frontier:
                explored.append(cnode.kb.clauses)
                frontier.append(cnode)
    return node

mysol=plan_search(airc,myacts,FIFOQueue())
print("Action sequence:")
print("Final states:")
print(mysol.kb.clauses)