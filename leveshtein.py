import requests

from utils import elapsed_time

def classic_levenshtein(word1: str, len1: str, word2: str, len2: str) -> int:
    if len1 == 0:
        return len2
    if len2 == 0:
        return len1
    custo = 0 if (word1[len1 - 1] == word2[len2 - 1]) else 1
    return min(
        classic_levenshtein(word1, len1 - 1, word2, len2) + 1,
        classic_levenshtein(word1, len1, word2, len2 - 1) + 1,
        classic_levenshtein(word1, len1 - 1, word2, len2 - 1) + custo)


def dynamic_levenshtein(X, Y):
    (m, n) = (len(X), len(Y))
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]

    for i in range(1, m + 1):
        T[i][0] = i

    for j in range(1, n + 1):
        T[0][j] = j

    for i in range(1, m + 1):

        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                cost = 0
            else:
                cost = 1

            T[i][j] = min(T[i - 1][j] + 1,
                          T[i][j - 1] + 1,
                          T[i - 1][j - 1] + cost)

    return T[m][n]


def run_leveshtein():
    results_classic_lev = []
    results_dyn_lev = []

    for n in range(1, 16):
        X, Y = eval(requests.get(f"https://random-word-api.herokuapp.com/word?length={n}&lang=it&number=2").content)
        
        r = elapsed_time(classic_levenshtein, X, len(X), Y, len(Y), text=f"Classic leven with {X} and {Y} size={n}")
        results_classic_lev.append(r)

        r = elapsed_time(dynamic_levenshtein, X,Y, text=f"Dynamic Leven with {X} and {Y} size={n}")
        results_dyn_lev.append(r)

    return (results_classic_lev, results_dyn_lev)