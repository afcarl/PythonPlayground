import random
import math


class Decision(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high


class Model(object):
    def __init__(self, objectives, constraints, decisions):
        self.objectives = objectives
        self.constraints = constraints
        self.decisions = decisions

    def evaluate(self, solution, total = 0):
        """
		Calculates the score for a given solution using all objectives
		"""
        for objective in self.objectives:
            total = total + objective(solution)
        return total

    def ok(self, solution):
        """
		Checks if solution is ok
		"""
        if self.constraints != None:
            for constraint in self.constraints:
                if not constraint(solution):
                    return False
        return True

    def any(self):
        """
		Generates a random solution
		"""
        valid = False
        solution = []
        while not valid:
            soln = []
            for dec in self.decisions:
                soln.append(random.randint(dec.low, dec.high))
            valid = self.ok(soln)
            if valid:
                solution = soln
        return solution


class Osyczka2(Model):
    def __init__(self):
        self.name = "Osyczka"
        objectives = [ob_os_1, ob_os_2]
        constraints = [con_os_1, con_os_2, con_os_3, con_os_4, con_os_5, con_os_6]
        decisions = [Decision(0, 10), Decision(0, 10), Decision(1, 5), Decision(0, 6), Decision(1, 5), Decision(0, 10)]
        Model.__init__(self, objectives, constraints, decisions)


class Schaffer(Model):
    def __init__(self):
        self.name = "Schaffer"
        objectives = [o_sh_1, o_sh_2]
        decisions = [Decision(-10 ** 5, 10 ** 5)]
        Model.__init__(self, objectives, None, decisions)


class Kursawe(Model):
    def __init__(self):
        self.name = "Kursawe"
        objectives = [o_ku_1, o_ku_2]
        decisions = [Decision(-5, 5), Decision(-5, 5), Decision(-5, 5)]
        Model.__init__(self, objectives, None, decisions)


"""
Objectives
"""


def o_ku_1(s):
    total = 0
    for i in xrange(len(s) - 1):
        value = -10 * math.exp((-0.2 * ((s[i]) ** 2) + ((s[i + 1]) ** 2)))
        total += value
    return total


def o_ku_2(s):
    a = 0.8
    b = 1
    total = 0
    for i in xrange(len(s)):
        value = (abs(s[i]) ** a) + (5 * math.sin((s[i]) ** b))
        total += value
    return total


def o_sh_1(sol):
    return sol[0] ** 2


def o_sh_2(sol):
    return (sol[0] - 2) ** 2


def ob_os_1(x):
    f1 = -(25 * (x[0] - 2) ** 2 + (x[1] - 2) ** 2 + ((x[2] - 1) * (x[3] - 4)) ** 2 + (x[4] - 1) ** 2)
    return f1


def ob_os_2(x):
    f2 = x[0] ** 2 + x[1] ** 2 + x[2] ** 2 + x[3] ** 2 + x[4] ** 2
    return f2


"""
Constraints
"""


def con_os_1(x):
    return 0 <= x[0] + x[1] - 2


def con_os_2(x):
    return 0 <= 6 - x[0] - x[1]


def con_os_3(x):
    return 0 <= 2 - x[1] + x[0]


def con_os_4(x):
    return 0 <= 2 - x[0] + 3 * x[1]


def con_os_5(x):
    return 0 <= 4 - (x[2] - 3) ** 2 - x[3]


def con_os_6(x):
    return 0 <= (x[4] - 3) ** 3 + x[5] - 4
