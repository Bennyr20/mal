def print_str(data, print_readably=False):
    if data is None:
        return "nil"
    elif type(data) is list:
        retVal = []
        for item in data:
            itemStr = print_str(item)
            if itemStr is None:
                retVal.append("nil")
            else:
                retVal.append(print_str(item))
        return "(" + " ".join(retVal) + ")"
    elif callable(data):
        return "#" + str(data)
    else:
        if data is None:
            return "nil"
        if type(data) == str:
            if data[0] == '"':
                data = data[1 : len(data) - 1]
            if print_readably:
                data = (
                    data.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
                )
                data = '"' + data + '"'
        elif type(data) == bool:  # if it's a boolean mal wants lowercase
            if data:
                return "true"
            return "false"

        return str(data)

