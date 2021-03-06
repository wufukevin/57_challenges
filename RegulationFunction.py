def InputFunction(InputString, InputOrder, EnsureFunction):

    InputCorrect = True
    while InputCorrect:
        Input = input(InputString)
        if not EnsureFunction(Input):
            InputCorrect = False
        if InputCorrect:
            break
    return Input