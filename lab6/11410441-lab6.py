from agents import *
from logic import *
from myKnowBase import OriKnowBase

class PropKB(KB):

    "A KB for propositional logic. Inefficient, with no indexing."

    def __init__(self, sentence=None):
        self.clauses = [[]]
        self.oriKn = OriKnowBase()
        self.clauses[0].extend(conjuncts(to_cnf(self.oriKn)))

        if sentence:
            self.tell(sentence)

    def tell(self, sentence):
        "Add the sentence's clauses to the KB."
        self.clauses.append([])
        self.clauses[sentence[1]+1].extend(conjuncts(to_cnf(self.oriKn)))
        self.clauses[sentence[1]+1].extend(conjuncts(to_cnf(sentence[0])))

    def ask_generator(self, query):
        "Yield the empty substitution {} if KB entails query; else no results."
        t=query
        kb=Expr('&', *self.clauses[t+1])
        act='Climb'
        if tt_entails(kb, expr('G1')):
            act='GoL'
        elif tt_entails(kb, expr('G2')):
            act='GoR'
        elif tt_entails(kb, expr('G3')):
            act = 'GoU'
        elif tt_entails(kb, expr('G4')):
            act = 'GoD'
        elif tt_entails(kb, expr('G5')):
            act = 'Climb'

        yield (act)

def KB_AgentProgram(KB):
        """A generic logical knowledge-based agent program. [Figure 7.1]"""
        steps = itertools.count()

        def program(percept):
            t = next(steps)

            mps=make_percept_sentence(percept, t)
            print('Percept *****:', mps)
            KB.tell(mps)

            action = KB.ask(make_action_query(t))
            print('Action *****:', action)

            #KB.tell(make_action_sentence(action, t))

            return action

        def make_percept_sentence(percept, t):
            mps=[]
            for ip in range(len(percept)):
                if (len(percept[ip])==1) and (percept[ip][0]==None):
                    symb='N'+str(ip+1)
                    mps.append(symb)
                for iip in percept[ip]:
                    if isinstance(iip, Bump):
                        symb='BU'+str(ip+1)
                        mps.append(symb)
                    elif isinstance(iip, Breeze):
                        symb='BR'+str(ip+1)
                        mps.append(symb)
                    elif isinstance(iip, Stench):
                        symb='S'+str(ip+1)
                        mps.append(symb)
                    elif isinstance(iip, Wumpus):
                        symb='W'+str(ip+1)
                        mps.append(symb)
                mps1=''
                for ip in mps:
                    mps1 += (ip+'&')
                mps1=mps1[:-1]
                return [expr(mps1),t]

        def make_action_query(t):
            return t

        def make_action_sentence(action, t):
            return [Expr("Did:")(action),t]

        return program


class WumpusEnvironment_my(WumpusEnvironment):

    def execute_action(self, agent, action):
        '''Modify the state of the environment based on the agent's actions
            Performance score taken directly out of the book'''

        if isinstance(agent, Explorer) and self.in_danger(agent):
            return

        agent.bump = False

        if action == 'GoL':
            x0, y0 = agent.location
            agent.bump = self.move_to(agent, (x0-1, y0))
            agent.performance -= 1
        elif action == 'GoR':
            x0, y0 = agent.location
            agent.bump = self.move_to(agent, (x0 + 1, y0))
            agent.performance -= 1
        elif action == 'GoU':
            x0, y0 = agent.location
            agent.bump = self.move_to(agent, (x0, y0-1))
            agent.performance -= 1
        elif action == 'GoD':
            x0, y0 = agent.location
            agent.bump = self.ove_to(agent, (x0, y0+1))
            agent.performance -= 1

        elif action == 'Grab':
           things = [thing for thing in self.list_things_at(agent.location)]


def plot_world(wd):
    print('-----------------------------')
    for i in range(1,5):
        for j in range(1,5):
            pth=wd[j][i]
            if pth:
                nth=''
                for thk in pth:
                    nthk = thk.__repr__()
                    if nthk[1]=='E':
                         nth +='e'
                    else:
                         nth += nthk[1]
                print('%-7s' % nth, end='')

            else:
                print('%-7s' % '[]', end="")
        print('')
    print('-----------------------------')

kb=PropKB()
ag_p=KB_AgentProgram(kb)
en=WumpusEnvironment_my(ag_p)

print('e<Explorer> G<Gold> B<Breeze> P<Pit> S<Stench> W<Wumpus>')
print('Left 1 Right 2 Up 3 Down 4 Center 5')

print('Initial world +++++++++++++++++++++')
wd=en.get_world()
plot_world(wd)

for i in range(2):
    en.run(1)
    wd=en.get_world()
    plot_world(wd)

print('Final world +++++++++++++++++++++++')
print("I am alive: {}".format(en.agents[-1].alive))