def to_enum(input_content, enum):
    input_in_lower_case = input_content.lower()
    for unit in enum:
        value_in_lower_case = unit.value.lower()
        if input_in_lower_case == value_in_lower_case or value_in_lower_case.startswith(input_in_lower_case, 0, 1):
            return unit
    raise Exception


def to_float(input_content):
    return float(input_content)
