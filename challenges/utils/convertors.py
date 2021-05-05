def to_enum(input_content, enum):
    input_in_lower_case = input_content.lower()
    for unit in enum:
        value_in_lower_case = unit.value.lower()
        if input_in_lower_case == value_in_lower_case or value_in_lower_case.startswith(input_in_lower_case, 0, 1):
            return unit
    raise Exception


def to_float(input_content):
    return float(input_content)


def to_int(input_content):
    return int(input_content)


def to_lower(input_content):
    return input_content.lower()


def to_state(input_content):
    input_in_lower = input_content.lower()
    if input_in_lower == 'wisconsin' or input_in_lower == 'wi':
        return 'Wisconsin'
    elif input_in_lower == 'illinois' or input_in_lower == 'il':
        return 'Illinos'
    return input_content
