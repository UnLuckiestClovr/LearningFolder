# Putting ": <object type>" inside the function variables makes sure that variable is of that type.
# Putting "->str" ensures the returned value is a String
def StringFunctions(s: str)->str:
    print(f"Starting String : {s}")

    # Reversing Strings is easy
    s = s[::-1]
    print(f"Reversed String : {s}")

    # Getting Strings from one character to another is easy as well. using the same setup as the last function.
    s = s[1:] # Gets index 1 onwards
    print(f"First Letter Onwards : {s}")

    s = s[:3] # Gets all letters to the third letter
    print(f"Up to Third Letter : {s}")

    return s