# Python Switch Statement
def switchStatement(input):
    match input:
        case 'a':
            return "Input == A"
        case 'b':
            return "Input == B"
        case 'c':
            return "Input == C"
        case 'd':
            return "Input == D"
        case 'e':
            return "Input == E"
        case _:
            return None # None is Python's version of 'null'