class MalType:
    type = ""

    def __init__(self, content):
        self.content = content


class MalList(MalType):
    type = "list"

    def __init__(self, content):
        self.content = content


class MalNum(MalType):
    type = "number"

    def __init__(self, num):
        self.content = num


class MalSymbol(MalType):
    type = "symbol"

    def __init__(self, val):
        self.content = val


class MalString(MalType):
    type = "string"

    def __init__(self, string):
        self.content = string


class MalKeyword(MalType):
    type = "keyword"

    def __init__(self, name):
        self.content = name


class MalVector(MalType):
    type = "vector"

    def __init__(self, content):
        self.content = content


class MalBool(MalType):
    type = "bool"

    def __init__(self, content):
        self.content = content


class MalNil(MalType):
    type = "nil"

    def __init__(self):
        self.content = None
