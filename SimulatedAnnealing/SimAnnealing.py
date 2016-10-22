class SimulatedAnnealing(object):

    def __init__(self,low,high,min_energy,max_energy,epsilon):
        self.low = low
        self.high = high
        self.min_energy = min_energy
        self.max_energy = max_energy
        self.epsilon = epsilon

    def f1(self,x):
        return x ** 2

    def f2(self,x):
        return (x-2) ** 2

    def get_energy(self,x):
        return self.f1(x) + self.f2(x)


