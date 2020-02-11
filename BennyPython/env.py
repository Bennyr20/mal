class Env:
    def __init__(self, outer, binds, exprs):
        self.outer = outer
        self.data = {}
        if binds is not None and exprs is not None:
            for i in range(len(binds)):
                self.set(binds[i], exprs[i])

    # adds a new symbol to the environment
    def set(self, key, value):
        self.data.update({key: value})
        return value

    # looks for the symbol in the current environment. Check the outer environments until it either finds it or does not exist
    def find(self, symbol):
        if symbol in self.data:
            return self.data  # not sure if to return the environment or data
        if self.outer is not None:  # if outer is not null
            return self.outer.find(symbol)
        else:
            return None

    def get(self, symbol):
        env = self.find(symbol)
        if env is None:
            return None
        return env[symbol]
