def READ(arg):
    return arg


def EVAL(arg):
    return arg


def PRINT(arg):
    return arg


# read, evaluate, print
def rep(arg):
    return PRINT(EVAL(READ(arg)))


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
