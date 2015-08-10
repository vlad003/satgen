import random
import math
import numpy

class Instance:
    def __init__(self, num_vars, num_clauses, k):
        self.num_vars = num_vars
        self.num_clauses = num_clauses
        self.k = k
        self.variables = range(1, num_vars+1)
        self.clauses = {}

    def generate(self):
        raise NotImplementedError()

    def __str__(self):
        text = "p cnf {} {}\n".format(self.num_vars, self.num_clauses)
        def list_join(l):
            return " ".join(map(str, l)) + " 0"

        return text + "\n".join(map(list_join, self.clauses.values()))

class UniformInstance(Instance):
    def generate(self):
        for m in range(self.num_clauses):
            clause = sorted(random.sample(self.variables, self.k))
            for i, var in enumerate(clause):
                clause[i] = var * ((-1) ** numpy.random.randint(2))

            self.clauses[m] = clause

class PowerInstance(Instance):
    def __init__(self, beta=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.beta = beta

    def generate(self):

        def sample_to_var(sample):
            subinterval = (1.0-0.0)/self.num_vars
            # we're using ceil below because our vars are 1..n, not 0..n-1
            return math.ceil(sample / subinterval)

        for m in range(self.num_clauses):
            samples = set()
            while len(samples) < self.k:
                sample = numpy.random.power(self.beta)
                var = sample_to_var(sample)
                samples.add(var)

            clause = sorted(samples)
            for i, var in enumerate(clause):
                clause[i] = var * ((-1) ** numpy.random.randint(2))

            self.clauses[m] = clause
