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
    # when result is called, binds `func` to the inputs by storing in a DataflowFunctionCall
    return lambda *args, **kwargs: DataflowFunctionCall(func, *args, **kwargs)

class Variable:
    def __hash__(self):
        return id(self)
