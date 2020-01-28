import re
import MalTypes


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
    return MalTypes.MalList(_list)


def read_atom(reader):
    token = reader.next()
    if token[0] == "-":  # negative number
        if token[1:].isnumeric():
            return MalTypes.MalNum(int(token))
    if token.isnumeric():
        return MalTypes.MalNum(int(token))
    elif token == "true":
        return MalTypes.MalBool(True)
    elif token == "false":
        return MalTypes.MalBool(False)
    elif token[0] == '"':
        return MalTypes.MalString(token)
    elif token == "nil":
        return MalTypes.MalNil()
    else:
        return MalTypes.MalSymbol(token)
