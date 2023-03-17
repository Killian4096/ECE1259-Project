from include.Pipeutils import calculate_outfile,get_independent_var,get_dependent_var

def dummy_func(**kwargs):
    result = kwargs
    result[get_dependent_var(**kwargs)] = result[get_independent_var(**kwargs)]
    return result


def main():
    user_input = {'u': '1,\n', 'v': '2,3,,,,,,4,2', 'w': ''}
    print(calculate_outfile(dummy_func, **user_input))




main()
