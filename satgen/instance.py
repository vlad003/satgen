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
                clause[i] = var * ((-1) ** random.randint(0, 1))

            self.clauses[m] = clause

class PowerInstance(Instance):
    def __init__(self, beta=0.75, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.beta = beta

    def generate(self):
        for m in range(self.num_clauses):
            samples = set()
            while len(samples) < self.k:
                sample = numpy.random.power(self.beta)
                var = self.__sample_to_var(sample, self.num_vars)
                samples.add(var)

            clause = sorted(samples)
            for i, var in enumerate(clause):
                clause[i] = var * ((-1) ** numpy.random.randint(2))

            self.clauses[m] = clause

    def __sample_to_var(self, sample, num_vars, interval=(0.0, 1.0)):
        """
        Associates the samples in the interval with a variable from 1 to n
        """
        start, end = interval
        bucket_size = (end-start)/num_vars

        return math.ceil(sample / bucket_size)
