import Reader
import printer
import env
import core


# evaluate abstract syntax tree, mal data type
def eval_ast(ast, env_):
    if callable(ast):  # if it's a function just return it
        return ast
    _type = Reader.getType(ast)
    if _type == "symbol":
        return env_.get(ast)
    if _type == "list":  # call eval on all using list comprehension
        return [EVAL(element, env_) for element in ast]
    else:
        return ast  # literal value


def READ(arg):
    return Reader.read_str(arg)


def EVAL(ast, _env):
    while True:
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
                _env = newEnv
                ast = ast[2]  # for tail call optimization, continue through loop.

            elif func == "do":  # evaluate each element of ast (besides the first one)
                ast = ast[1:]
                evaluated = eval_ast(ast[:-1], _env)
                ast = ast[-1]  # tail call optimization, continue through loop.

            elif func == "if":
                ast = ast[1:]
                _bool = EVAL(ast[0], _env)
                if (
                    _bool == None or _bool == False
                ):  # if it's false or none evaluate third element or return None if it doesn't exist
                    if len(ast) < 3:  # no third parameter to evaluate
                        ast = None
                    ast = ast[2]
                else:  # if it's true or anything else, evaluate second element
                    ast = ast[1]

            elif func == "fn*":
                ast = ast[1:]

                def funcClosure(
                    *args,
                ):  # return a new function closure. It creates an environment with the inputs as binds to the argument
                    newEnv = env.Env(_env, ast[0], args)
                    return EVAL(ast[1], newEnv)

                funcClosure.ast_ = ast[1]
                funcClosure.create_env = lambda args: env.Env(_env, ast[0], args)

                return funcClosure
            else:  # if it's a symbol
                ast_ = eval_ast(
                    ast, _env
                )  # changed name of ast because the other one will be used for TCO
                func = ast_[0]
                ast_ = ast_[1:]
                values = [value for value in ast_]
                if hasattr(
                    func, "ast_"
                ):  # if it's a function defined with fn* now it can use recursion
                    ast = func.ast_  # this is the ast that will be used for TCO
                    _env = func.create_env(ast_)
                else:
                    return func(
                        *values
                    )  # calls the function with the rest of the list as function arguments


repl_env = env.Env(None, None, None)
for key, value in core.ns.items():
    repl_env.set(key, value)
repl_env.set("eval", lambda ast: EVAL(ast, repl_env))


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
            rep(
                '(def! load-file (fn* (f) (eval (read-string (str "(do " (slurp f) "\nnil)")))))'
            )
            inp = input("user> ")
            commandHistory.append(inp)
            if inp == "history":  # if the user types history, show commands
                print(commandHistory)
            else:
                print(rep(inp))

        except (KeyboardInterrupt, EOFError):  # Break on Ctrl-D or Ctrl-C
            break


repl()
