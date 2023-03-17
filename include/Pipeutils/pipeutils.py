import numpy as np

#Text Cleanup
def text_cleaner(seperator=' ', **kwargs):
    result = kwargs
    for key, value in kwargs.items():
        value = value.replace(',', ' ')
        value = value.replace('\n', ' ')
        while True:
            new_input = value.replace('  ', seperator)
            if new_input == value:
                break
            value = new_input
        result[key] = value
    return result

#Convert strings to arrays
def array_convert(**kwargs):
    result = kwargs
    for key, value in kwargs.items():
        value = np.fromstring(value, dtype=int, sep=' ')
        result[key] = value
    return result

#Check for correct format
def array_check(**kwargs):
    arrays = 0
    blanks = 0
    for key, value in kwargs.items():
        if len(value.shape) > 1:
            raise Exception("Keyword {key} has one or more dimensions".format(key))
        if value.shape[0] > 1:
            arrays += 1
        elif value.shape[0] == 0:
            blanks += 1
    if(arrays > 1):
        raise Exception("More than one independent variable")
    if(arrays == 0):
        raise Exception("No independent variable")
    if(blanks > 1):
        raise Exception("More than one dependent variable")
    if(blanks == 0):
        raise Exception("No dependent variable")

def get_independent_var(**kwargs):
    array_check(**kwargs)
    for key, value in kwargs.items():
        if(value.shape[0] > 1):
            return key

def get_dependent_var(**kwargs):
    array_check(**kwargs)
    for key, value in kwargs.items():
        if(value.shape[0] == 0):
            return key
        



def calculate_outfile(calc_func, **kwargs):
    kwargs = text_cleaner(**kwargs)
    kwargs = array_convert(**kwargs)
    kwargs = calc_func(**kwargs)
    return kwargs
