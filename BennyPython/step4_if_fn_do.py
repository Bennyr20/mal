import Reader
import printer
import env
import core

repl_env = env.Env(None, None, None)
for key, value in core.ns.items():
    repl_env.set(key, value)


# evaluate abstract syntax tree, mal data type
def eval_ast(ast, env):
    _type = Reader.getType(ast)
    if _type == "symbol":
        return env.get(ast)
    if _type == "list":  # call eval on all using list comprehension
        return [EVAL(element, env) for element in ast]
    else:
        return ast


def READ(arg):
    return Reader.read_str(arg)


def EVAL(ast, _env):
    if type(ast) is not list:
        return eval_ast(ast, _env)
    elif len(ast) == 0:  # empty list just return it
        return ast
    else:  # list, evaluate elements
        func = ast[0]

        if func == "def!":  # define a new symbol in environment
            return _env.set(ast[1], EVAL(ast[2], _env))

        elif func == "let*":
            newEnv = env.Env(_env, None, None)
            bindings, val = ast[1], ast[2]
            for i in range(0, len(bindings), 2):
                newEnv.set(
                    bindings[i], EVAL(bindings[i + 1], newEnv),
                )
            retVal = EVAL(val, newEnv)
            return retVal

        elif func == "do":  # evaluate each element of ast (besides the first one)
            ast = ast[1:]
            evaluated = eval_ast(ast, _env)
            return evaluated[-1]

        elif func == "if":
            ast = ast[1:]
            _bool = EVAL(ast[0], _env)
            if (
                _bool == None or _bool == False
            ):  # if it's false or none evaluate third element or return None if it doesn't exist
                if len(ast) < 3:  # no third parameter to evaluate
                    return None
                return EVAL(ast[2], _env)
            else:  # if it's true or anything else, evaluate second element
                return EVAL(ast[1], _env)

        elif func == "fn*":
            ast = ast[1:]

            def funcClosure(
                *args,
            ):  # return a new function closure. It creates an environment with the inputs as binds to the argument
                newEnv = env.Env(_env, ast[0], args)
                return EVAL(ast[1], newEnv)

            return funcClosure
        else:  # if it's a symbol
            ast = eval_ast(ast, _env)
            func = ast[0]
            ast = ast[1:]
            values = [value for value in ast]
            return func(
                *values
            )  # calls the function with the rest of the list as function arguments


def PRINT(arg):
    return printer.print_str(arg, True)


# read, evaluate, print
def rep(arg):
    return PRINT(EVAL(READ(arg), repl_env))


# read, evaluate, print, loop
def repl():
    commandHistory = []
    while True:
        try:
            rep("(def! not (fn* (a) (if a false true)))")  # define a not function
            inp = input("user> ")
            commandHistory.append(inp)
            if inp == "history":  # if the user types history, show commands
                print(commandHistory)
            else:
                print(rep(inp))

        except (KeyboardInterrupt, EOFError):  # Break on Ctrl-D or Ctrl-C
            break


repl()
