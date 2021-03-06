def _resolve(arg, assignments={}):
    if isinstance(arg, DataflowFunctionCall):
        return arg.execute(assignments)
    elif isinstance(arg, Variable):
        return assignments[arg]
    return arg

class DataflowFunctionCall:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def execute(self, assigments={}):
        # step 1: resolve inputs
        args = [_resolve(arg, assigments) for arg in self.args]
        kwargs = {k: _resolve(v, assigments) for k, v in self.kwargs.items()}

        # step 2: resolve function call
        return self.func(*args, **kwargs)

def dataflow(func):
    '''
    decorates func, now when the original func is called, it returns an object
    storing the delayed execution of func (and its arguments).
    '''
    def wrapper(*args, **kwargs):
        return DataflowFunctionCall(func, *args, **kwargs)
    return wrapper

class Variable:
    def __hash__(self):
        return id(self)
