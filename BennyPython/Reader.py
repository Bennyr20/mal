import re


class Reader:
    def __init__(self, tokens):
        self.pos = 0
        self.tokens = tokens

    # just returns token at current position
    def peek(self):
        return self.tokens[self.pos]

    # returns the token at the current position and increments the position
    def next(self):
        token = self.tokens[self.pos]
        self.pos += 1
        return token


# turns the string into tokens
def tokenize(string):
    tokens = re.split(
        r"[\s,]*(~@|[\[\]{}()'`~^@]|\"(?:\\.|[^\\\"])*\"?|;.*|[^\s\[\]{}('\"`,;)]*)",
        string,
    )
    for token in tokens:
        if token == "":
            tokens.remove(token)
    while "" in tokens:
        tokens.remove("")
    return tokens


def read_str(tokens):
    return read_form(Reader(tokenize(tokens)))


# if it's an open paren, calls read_list, else it calls read_atom
def read_form(reader):
    firstChar = reader.peek()[0]
    if firstChar == "(":
        return read_list(reader)
    else:
        return read_atom(reader)


# tokenizes a list
def read_list(reader):
    # TODO if reaches EOF, throw error
    # Or list error
    _list = []

    reader.next()  # increment so it passes open paren
    while True:
        token = reader.peek()
        if token == ")":
            break
        retVal = read_form(reader)
        _list.append(retVal)
    reader.next()  # increment so it passes close paren
    return _list


def read_atom(reader):
    token = reader.next()
    if token[0] == "-":  # negative number
        if token[1:].isnumeric():
            return int(token)
    if token.isnumeric():
        return int(token)
    elif token == "true":
        return True
    elif token == "false":
        return False
    elif token[0] == '"':
        return '"' + token + '"'
    elif token == "nil":
        return None
    else:  # it is a symbol
        return token


# return the type of the value
def getType(val):
    if val is None:
        return "None"
    if type(val) is list:
        return "list"
    if type(val) is int:
        return "num"
    elif type(val) is bool:
        return "bool"
    elif val[0] == '"':
        return "string"
    else:
        return "symbol"
