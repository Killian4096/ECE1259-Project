from include.Pipeutils import calculate_outfile,get_independent_var,get_dependent_var

def dummy_func(pipe):
    result = pipe
    result[get_dependent_var(pipe)] = result[get_independent_var(pipe)]
    return result


def main():
    user_input = {'u': '1,\n', 'v': '2,3,,,,,,4,2', 'w': ''}
    print(calculate_outfile(user_input, dummy_func))




main()
