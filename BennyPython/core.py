import printer

# calls pr_str on each argument with print_readably set to true, joins the results with " ", prints the string to the screen and then returns nil.
def funcPrn(*arg):
    output = []
    for val in arg:
        output.append(printer.print_str(val, True))
    results = " ".join(output)
    print(results)
    return None


# calls pr_str on each argument with print_readably set to false, joins the results with " ", prints the string to the screen and then returns nil.
def funcPrintline(*arg):
    output = []
    for val in arg:
        output.append(printer.print_str(val, False))
    results = " ".join(output)
    print(results)
    return None


# calls pr_str on each argument with print_readably set to true, joins the results with " " and returns the new string.
def funcPrn_str(*arg):
    output = []
    for val in arg:
        output.append(printer.print_str(val, True))
    return " ".join(output)


# calls pr_str on each argument with print_readably set to false, concatenates the results together ("" separator), and returns the new string.
def funcStr(*arg):
    output = []
    for val in arg:
        output.append(printer.print_str(val, False))
    return "".join(output)


def funcList(*arg):
    return list(arg)


def funcIsList(arg):
    return type(arg) == list


def funcIsEmpty(arg):
    return len(arg) == 0


def funcCount(*arg):
    if not (type(arg[0]) == list):
        return None
    return len(arg[0])


def funcIsEqual(arg1, arg2):
    if not (type(arg1) == type(arg2)):  # if they're not the same type return false
        return False
    if type(arg1) == list:  # if they're lists compared each element
        if not (len(arg1) == len(arg2)):  # make sure they're the same length
            return False
        # lists that are the same length
        for i in range(len(arg1)):
            val = funcIsEqual(arg1[i], arg2[i])
            if val == False:
                return False
    return arg1 == arg2


# mapping of symbols to functions
ns = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: int(a / b),
    "prn": funcPrn,
    "pr-str": funcPrn_str,
    "str": funcStr,
    "println": funcPrintline,
    "list": funcList,
    "list?": funcIsList,
    "empty?": funcIsEmpty,
    "count": funcCount,
    "=": funcIsEqual,
    "<": lambda a, b: a < b,
    "<=": lambda a, b: a <= b,
    ">": lambda a, b: a > b,
    ">=": lambda a, b: a >= b,
}
