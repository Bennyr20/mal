import MalTypes


def print_str(data):
    if data is None:
        return ""
    if data.type == "number":
        return str(data.content)
    elif data.type == "symbol":
        return data.content
    elif data.type == "string":
        return data.content
    elif data.type == "keyword":
        return data.content
    elif data.type == "bool":
        return str(data.content)
    elif data.type == "nil":
        return "nil"
    elif data.type == "list":
        retVal = []
        for item in data.content:
            itemStr = print_str(item)
            if itemStr is None:
                retVal.append("nil")
            else:
                retVal.append(print_str(item))
        return "(" + " ".join(retVal) + ")"

