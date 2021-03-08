from collections.abc import Callable

def InputFunction(InputString, InputOrder, EnsureFunction):
    InputNotCorrect = True
    while InputNotCorrect:
        InputNotCorrect = False
        Input = input(InputString)
        if not EnsureFunction(Input):
            InputNotCorrect = True
    return Input
