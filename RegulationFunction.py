from collections.abc import Callable

def presetEnsureFunction(everyThing):
    return True


def InputFunction(InputString, InputOrder = '1', EnsureFunction = presetEnsureFunction):
    InputNotCorrect = True
    while InputNotCorrect:
        InputNotCorrect = False
        Input = input(InputString)
        if not EnsureFunction(Input):
            InputNotCorrect = True
    return Input
