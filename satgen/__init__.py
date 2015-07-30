from enum import Enum
import random
import numpy

class Distribution(Enum):
    uniform = 0
    powerlaw = 1

class Instance:
    def __init__(self, num_vars, num_clauses, k,
            distribution=Distribution.uniform, beta=0.75):
        self.num_vars = num_vars
        self.num_clauses = num_clauses
        self.k = k
        self.distribution = distribution
        self.beta = beta

        self.variables = range(1, num_vars+1)
        self.clauses = {}

    def generate(self):
        if self.distribution is Distribution.uniform:
            for m in range(self.num_clauses):
                clause = random.sample(self.variables, self.k)
                for i, var in enumerate(clause):
                    clause[i] = var * ((-1) ** random.randint(0, 1))

                self.clauses[m] = clause
        elif self.distribution is Distribution.powerlaw:
            for m in range(self.num_clauses):
                probs = numpy.random.power(self.beta, self.num_vars)
                combined = zip(range(1, self.num_vars+1), probs)
                ordered = sorted(combined, key=lambda x: x[1])
                clause = list(map(lambda x: x[0], ordered[:self.k]))

                for i, var in enumerate(clause):
                    clause[i] = var * ((-1) ** numpy.random.randint(2))

                self.clauses[m] = clause

        else:
            # TODO
            pass

    def __str__(self):
        text = "p cnf {} {}\n".format(self.num_vars, self.num_clauses)
        def list_join(l):
            return " ".join(map(str, l)) + " 0"

        text += "\n".join(map(list_join, self.clauses.values()))
        return text
