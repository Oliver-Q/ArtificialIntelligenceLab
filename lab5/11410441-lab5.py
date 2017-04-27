from csp import (MapColoringCSP, min_conflicts, backtracking_search, mrv, forward_checking, mac)
import time
import networkx as nx
import matplotlib.pyplot as plt


france = MapColoringCSP(list('RGBYK'),"""AL: LO FC; AQ: MP LI PC; AU: LI CE BO RA LR MP; BO: CE IF CA FC RA
        AU; BR: NB PL; CA: IF PI LO FC BO; CE: PL NB NH IF BO AU LI PC; FC: BO
        CA LO AL RA; IF: NH PI CA BO CE; LI: PC CE AU MP AQ; LO: CA AL FC; LR:
        MP AU RA PA; MP: AQ LI AU LR; NB: NH CE PL BR; NH: PI IF CE NB; NO:
        PI; PA: LR RA; PC: PL CE LI AQ; PI: NH NO CA IF; PL: BR NB CE PC; RA:
        AU BO FC PA LR""")

pstart = time.clock()

mymap=france
for itm in range(10):
    #mysol=min_conflicts(mymap)
    #mysol=backtracking_search(mymap)
     mysol=backtracking_search(mymap,select_unassigned_variable=mrv)
    # mysol=backtracking_search(mymap, inference=forward_checking)
    #mysol = backtracking_search(mymap,inference=mac)
    # mysol = backtracking_search(mymap,select_unassigned_variable=mrv,inference=forward_checking)

pend = time.clock()
pstime=(pend-pstart)/10
print("The running time: %s" %(pstime))
print(mysol)

mystr=list(mymap.neighbors.items())

G = nx.Graph()
for i in range(len(mysol)):
    myloc=mystr[i][0]
    mynb=mystr[i][1]
    for j in range(len(mynb)):
        G.add_edge(myloc,mynb[j])

node_colors=[]
for i in G.node:
    node_colors.append(mysol[i])

nx.draw_spectral(G,with_labels=True,font_size=14,node_size=900,font_color='w',node_color=node_colors)
plt.show()