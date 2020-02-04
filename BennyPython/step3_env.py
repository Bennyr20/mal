import Reader
import printer
import MalTypes
import env

# operators
repl_env_op = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: int(a / b),
}

repl_env = env.Env(MalTypes.MalNil)
for key, value in repl_env_op.items():
    repl_env.set(key, value)

# evaluate abstract syntax tree, mal data type
def eval_ast(ast, env):
    if ast.type == "symbol":
        return env.get(ast.content)
    if ast.type == "list":  # call eval on all using list comprehension
        return MalTypes.MalList([EVAL(element, repl_env) for element in ast.content])
    else:
        return ast


def READ(arg):
    return Reader.read_str(arg)


def EVAL(ast, _env):
    if ast.type != "list":
        return eval_ast(ast, _env)
    elif len(ast.content) == 0:
        return ast
    else:  # list, evaluate elements
        func = ast.content[0].content

        if func == "def!":  # define a new symbol in environment
            return _env.set(ast.content[1].content, EVAL(ast.content[2], _env))

        elif func == "let*":
            newEnv = env.Env(_env)
            bindings, val = ast.content[1], ast.content[2]
            for i in range(0, len(bindings.content), 2):
                newEnv.set(
                    bindings.content[i].content,
                    EVAL(bindings.content[i + 1], newEnv).content,
                )
            retVal = EVAL(val, newEnv)
            if isinstance(
                retVal, MalTypes.MalType
            ):  # If it's already a maltype just return it, if not make it so
                return retVal
            return MalTypes.MalNum(retVal)
        else:  # if it's a symbol
            ast = eval_ast(ast, _env).content
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
