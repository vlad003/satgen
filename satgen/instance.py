import random
import math
import bisect
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
    def __init__(self, beta=0.5, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.beta = beta

    def generate(self):

        norm = sum(i**(-self.beta) for i in range(1, self.num_vars+1))
        prob_i = lambda i: i**(-self.beta) / norm

        cumulative_probs = [0] * (self.num_vars+1)
        for var in range(1, self.num_vars+1):
            cumulative_probs[var] = cumulative_probs[var-1] + prob_i(var)

        # remove the initial 0 since that was just for the computation above
        cumulative_probs.pop(0)

        for m in range(self.num_clauses):
            samples = set()
            while len(samples) < self.k:
                sample = numpy.random.uniform()
                var = bisect.bisect_left(cumulative_probs, sample) + 1
                if var is not None:
                    samples.add(var)

            clause = sorted(samples)
            for i, var in enumerate(clause):
                clause[i] = var * ((-1) ** numpy.random.randint(2))

            self.clauses[m] = clause
