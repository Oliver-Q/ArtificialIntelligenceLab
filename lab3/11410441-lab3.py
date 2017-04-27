from qnproblem import *

def exp_schedule(k=0.2, lam=0.005, limit=100):
    "One possible schedule function for simulated annealing"
    return lambda t: (k * math.exp(-lam * t) if t < limit else 0)


def simulated_annealing(problem, schedule=exp_schedule()):
    "[Figure 4.5]"
    current = Node(problem.initial)
    for t in range(sys.maxsize):
        T = schedule(t)
        if T == 0:
            return current
        neighbors = current.expand(problem)
        if not neighbors:
            return current
        next = random.choice(neighbors)
        delta_e = problem.value(next.state) - problem.value(current.state)
        if delta_e > 0 or probability(math.exp(delta_e / T)):
            current = next

q8problem = NQueensProblem(8)
myag = simulated_annealing(q8problem)
print(myag.state)
print(q8problem.value(myag.state))

def genetic_search(problem, ngen=100, pmut=0.5, n=4):
    """
    Call genetic_algorithm on the appropriate parts of a problem.
    This requires the problem to have states that can mate and mutate,
    plus a value method that scores states."""
    s = problem.initial

    states = [problem.result(s, a) for a in problem.actions(s)]
    random.shuffle(states)
    return genetic_algorithm(states[:n], problem.value, ngen, pmut)


def genetic_algorithm(population, fitness_fn, ngen=100, pmut=0):
    "[Figure 4.8]"
    for i in range(ngen):
        new_population = []
        for i in range(len(population)):
            fitnesses = map(fitness_fn, population)
            p1, p2 = weighted_sample_with_replacement(population, fitnesses, 2)

            p1 = GAState(p1)
            p2 = GAState(p2)

            child = p1.mate(p2)

            if random.uniform(0, 1) < pmut:
                child.mutate()
            new_population.append(child.genes)
        population = new_population
    return argmax(population, key=fitness_fn)

class GAState:

    "Abstract class for individuals in a genetic search."

    def __init__(self, genes):
        self.genes = genes

    def mate(self, other):
        "Return a new individual crossing self and other."
        c = random.randrange(len(self.genes))
        return self.__class__(self.genes[:c] + other.genes[c:])

    def mutate(self):
        "Change a few of my genes."
        ind_mute = random.randrange(len(self.genes))
        self.genes[ind_mute] = random.randrange(len(self.genes))

q8problem = NQueensProblem(8)
myag = genetic_search(q8problem)
print(myag)
print(q8problem.value(myag))
