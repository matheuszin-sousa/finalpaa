from fibo import run_fibos
from leveshtein import run_leveshtein
from matrix_chain import run_matrix


def write_to_file(*results, file_names: list):
    for l, name in zip(results, range(len(results))):
        with open(file_names[name], 'w') as f:
            f.write(','.join(l))

if "__main__" == __name__:
    classic_fibo, td_fibo, bu_fibo = run_fibos()
    classic_leven, dyn_leven = run_leveshtein()
    classic_matrix, dyn_matrix = run_matrix()

    write_to_file(classic_fibo, td_fibo, bu_fibo,
        classic_leven, dyn_leven,
        classic_matrix, dyn_matrix, file_names=["classic_fibo", "td_fibo", "bu_fibo",
        "classic_leven", "dyn_leven",
        "classic_matrix", "dyn_matrix"])