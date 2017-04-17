

class FuncCall:
    def __init__(self,name, func, *args ):
        self.args = args

    def apply(self):
        args = []
        # before applying function call, function call inputs need to be resolved
        for arg in self.args:
            if isinstance(arg, FuncCall):
                args.append( arg.apply() )
            else:
                args.append(arg)
        # now ready to apply the function call
        return self.func(*args)

class FunctionCall:
    def __init__(self, name, func, *args):
        # store everything needed for computation and any other metadata
        self.name = name # example of metadata
        self.func = func # function we would like to call later
        self.args = args # arguments we will later pass to the function

    def apply(self):
        # before applying function call, function call inputs need to be resolved
        args = [arg.apply() if isinstance(arg, FunctionCall) else arg for arg in self.args]
        # now ready to apply the function call
        return self.func(*args)

# setting up the execution / dataflow
f = FunctionCall('multiply', lambda x, y: x * y, 3, 4) # f = 3 * 4
g = FunctionCall('add', lambda x, y: x + y, f, 2) # g = f + 2
# no addition or multiplication has happened yet

# executing the dataflow
print(g.apply())
