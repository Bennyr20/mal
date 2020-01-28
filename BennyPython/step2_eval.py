import Reader
import printer
import MalTypes

repl_env = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: int(a / b),
}

# evaluate abstract syntax tree, mal data type
def eval_ast(ast):
    if ast.type == "symbol":
        return repl_env[ast.content]
    if ast.type == "list":  # call eval on all using list comprehension
        return MalTypes.MalList([EVAL(element, repl_env) for element in ast.content])
    else:
        return ast


def READ(arg):
    return Reader.read_str(arg)


def EVAL(ast, env):
    if ast.type != "list":
        return eval_ast(ast)
    elif len(ast.content) == 0:
        return ast
    else:  # list, evaluate elements
        ast = eval_ast(ast).content
        func = ast[0]
        ast = ast[1:]
        values = [value.content for value in ast]
        return MalTypes.MalNum(
            func(*values)
        )  # calls the function with the rest of the list as function arguments


def PRINT(arg):
    return printer.print_str(arg)


# read, evaluate, print
def rep(arg):
    return PRINT(EVAL(READ(arg), repl_env))


# read, evaluate, print, loop
def repl():
    commandHistory = []
    while True:
        try:
            inp = input("user> ")
            commandHistory.append(inp)
            if inp == "history":  # if the user types history, show commands
                print(commandHistory)
            else:
                print(rep(inp))

        except (KeyboardInterrupt, EOFError):  # Break on Ctrl-D or Ctrl-C
            break


repl()
