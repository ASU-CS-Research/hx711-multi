#!/usr/bin/env python3
"""
This file holds general utilities used elsewhere in the code
"""


def convert_to_list(_input=None, _type=int, _default_output=None):
    """
    Converts the input to a list if not already.
    Also performs checks for type of list items and will set output to the default value if type criteria isn't met

    Args:
        _input: input that you are analyzing to convert to list of type
        _type (optional): type of items in list to confirm. Defaults to int. A value of None results in no type checking
        _default_output (optional): value to pass if no other criteria is used. Defaults to None.
    """
    output = _default_output
    if type(_input) is list:
        if _type is not None:
            if all([(type(x) is _type) for x in _input]):
                # set to output if is list and all instances match type
                output = _input
        else:
            # set to output if is list (no type specified)
            output = _input
    elif ((type(_input) is _type) and (_type is not None)) or ((_input is not None) and (_type is None)):
        # set to output as a single element list if is type match, or no type was specified and input is not None
        output = [_input]
    return output
