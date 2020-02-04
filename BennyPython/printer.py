def print_str(data):
    if data is None:
        return ""
    elif type(data) is list:
        retVal = []
        for item in data:
            itemStr = print_str(item)
            if itemStr is None:
                retVal.append("nil")
            else:
                retVal.append(print_str(item))
        return "(" + " ".join(retVal) + ")"
    else:
        if data is None:
            return "nil"
        return str(data)

