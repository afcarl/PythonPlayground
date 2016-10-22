
# coding: utf-8

# # Modelling Finite State Machines.

# In this this program we code up a small world model in python. This model is called drinking in a bar. The rules are as follows:
# * You start sober.
# * If you are sober you take a drink
# * Once you take a drink, there are three possible scenarios.
#    * If you are drunk and take a drink, there is 80% chance that you will stay drunk.
#    * If you are drunk and take a drink, there is 20% chance that you will pass out.
#    * If you are drunk and you do not drink, there is 50% chance that you will become sober
#    * If you pass out, you don't drink.
#

from __future__ import print_function, division
import random

# Author's name
__name__ = "Tarun Chhabra"

def kv(d):
    """
    Pretty Print the dictionary.
    """
    return '(' + ','.join(['%s: %s'%(k, d[k]) for k in sorted(d.keys()) if k[0] != "_"]) + ')'


def shuffle(lst):
    """
    Shuffle a list and return it.
    """
    random.shuffle(lst)
    return lst

## Function to get the random value between a lower and upper bound.
randint = random.randint

class O(object):
    """
    Basic Class which every other class inherits
    """
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return self.__class__.__name__ + kv(self.__dict__)

print("Hello %s"%__name__)


class State(O):
    """
    State object
    """
    visit_limit = 5
    def __init__(self, name):
        """
        Initialize a state.
        @param name: Name of the state
        @return: State object with
            name: Name of the state
            out: List of transitions
            visits: Number of times the state was visited if not declared as a loop
        """
        O.__init__(self, name=name, out=[], visits = 0)

    def is_stop(self):
        """
        Check if state is a stop state
        """
        return self.name[-1] == "."

    def is_loop(self):
        """
        Check if state is a possible loop state
        """
        return self.name[0] == "#"

    def arrive(self):
        """
        Move to the state if not a loop
        """
        if not self.is_loop():
            self.visits += 1
            assert self.visits <= State.visit_limit, "Loop Encountered"

    def next(self, record):
        """
        Move to next state from a list of possible transitions
        """
        for trans in shuffle(self.out):
            if trans.guard(record, trans):
                return trans.there
        return self



class Trans(O):
    # Transition Class
    def __init__(self, here, guard, there):
        """
        @param here: starting state
        @param guard: transfer function
        @param there: ending state
        """
        O.__init__(self, here = here, guard = guard, there = there)



class Machine(O):
    def __init__(self, label, data=0):
        """
        Create an instance of machine.
        @param label: Label representing the machine
        @param data: Data used to describe the machine. In this case you don't have any data
        """
        O.__init__(self, label = label, # Label of the machine
                   states = {}, # Possible state of the machine
                   here = None, # Current state of the machine
                   data = data) # Data used to describe the machine

    def add_state(self, name):
        # Add a state to the machine.
        # Create an instance of state, add it to the states map. Also if
        # the current state is None, set it to this state.
        # Also return the state
        st = State(name)
        self.states[name] = st
        if self.here is None:
            self.here = st
        return st

    def add_trans(self, *trans):
        # For every transition in the list *trans, add the
        # transition to the "out" list in the "here" state
        for tran in trans:
            tran.here.out.append(tran)

    def step(self):
        # Move the machine to the next state if it is currently not in the stop state.
        if not self.here.is_stop():
            self.here = self.here.next(self)
            self.here.arrive()


class Factory(O):
    """
    Factory that generates machines.
    """
    def __init__(self):
        """
        Initialize the factory.
        """
        O.__init__(self, machines = [])

    def make_machine(self, label, data=0):
        # Create a new machine and add it to
        # the list "machines" and return the machine
        machine = Machine(label=label,data=data)
        self.machines.append(machine)
        return machine

    def run(self, seed=1, ticks=100):
        """
        Run all the machines
        """
        print('Seed : ', seed)
        random.seed(seed)
        for _ in xrange(ticks):
            alive = False
            for machine in shuffle(self.machines):
                if not machine.here.is_stop():
                    alive = True
                    machine.step()
                    self.report(machine.label)
                    break
            if not alive: break

    def report(self, name):
        """
        Report the runs
        """
        max_len = 50
        lst = [0]*(max_len + 1)
        for machine in self.machines:
            lst[machine.data] += machine.label
            print (machine.here)
        show = lambda x: str(x if x else '.')
        print(name, " | ", " ".join(map(show, lst)))



# In[22]:

drunk_chance = 0.8
passout_chance = 0.2
sober_chance = 0.5

def drunk(m, t):
    """
    Transition Function for snow
    @param m: instance of Machine
    @param t: instance of Trans

    """
    # If chance < drunk_chance, reduce the machine's energy
    # by a random integer between [1, 5] and return True. Else return False
    if random.random() < drunk_chance:
        m.data -= randint(1,5)
        return True
    return False

def sober(m, t):
    """
    Transition Function for grass
    @param m: instance of Machine
    @param t: instance of Trans
    """
    # If chance < sober_chance, increase the machine's energy
    # to a random integer between [1, 5] and return True. Else return False
    if random.random() < sober_chance:
        m.data += randint(1,5)
        return True
    return False

def passout(m, t):
    """
    Return if chance < passout_chance.
    """
    return random.random() < passout_chance


def drink(m, t):
    """
    Walk from a state
    :param m: machine
    :param t: trans object
    :return:
    """
    return True

def notdrink(m,t):
    return True


# In[23]:

def fsm(factory, label, data):
    m = factory.make_machine(label, data)
    # Using the functions and classes defined above code up the
    # state machine in the figure at the top of the page.
    sober = m.add_state("sober")
    drunk = m.add_state("#drunk")
    passout = m.add_state("passout.")

    m.add_trans(Trans(sober,drink,drunk),
               Trans(drunk,drink,drunk),
               Trans(drunk,drink,passout),
               Trans(drunk,notdrink,sober),
               Trans(drunk,notdrink,drunk),)

    return m


# In[24]:

f = Factory()
fsm(f, 1, 25)
fsm(f, 2, 25)
fsm(f, 4, 25)
f.run(100)


