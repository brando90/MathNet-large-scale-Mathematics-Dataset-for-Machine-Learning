class DataflowFunctionCall:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    @staticmethod
    def _execute_arg(arg, assignments={}):
        if isinstance(arg, DataflowFunctionCall):
            return arg.execute(assignments)
        elif isinstance(arg, Variable):
            return assignments[arg]
        return arg

    def execute(self, assigments={}):
        args = [DataflowFunctionCall._execute_arg(arg, assigments) for arg in self.args]
        return self.func(*args)
        # args = []
        # for arg in self.args:
        #     args.append( DataflowFunctionCall._execute_arg(arg, assigments) )
        # return self.func(*args)

class DataflowFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return DataflowFunctionCall(self.func, *args)

def dataflow(func):
    return DataflowFunction(func)

# def dataflow2(func):
#     def wrapper(func):
#         return DataflowFunction(func)
#     return wrapper

class Variable:
    def __hash__(self):
        return hash(id(self))

@dataflow
def f(x, y):
    return x**2 % y
# f = dataflow(f)
# f = DataflowFunction(f)

@dataflow
def g(a, b, c):
    return a * b + c
# g = dataflow(g)

@dataflow
def h(i, j):
    return i / j
# h = dataflow(h)

seed = Variable()

# ---

# setting up the execution / dataflow
graph = f(g(1, 2, h(3, 4)), seed)
# no addition or multiplication has happened yet

# executing the dataflow
print(graph.execute({seed: 5}))

print(graph.execute({seed: 7}))

##
seed = Variable()
a = Variable()
graph = f(g(1, a, h(a, 4)), seed)
print(graph.execute({seed: 7,a: 10}))
