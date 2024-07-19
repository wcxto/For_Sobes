# Напишите программу для подсчета количества правок, которые нужно выполнить, чтобы преобразовать строку S1 в строку S2. 
# Например, для преобразования слова «лимузин» в «лимонад» нужно сделать 4 правки, а для приведения слова «кошка» к слову «кофта» достаточно 2 изменений.

#       | к | о | ф | т | а |
#   --------------------------
#   | 0 | 1 | 2 | 3 | 4 | 5 |
#-----------------------------
# к | 1 | 0 | 1 | 2 | 3 | 4 |
#-----------------------------
# о | 2 | 1 | 0 | 1 | 2 | 3 |
#-----------------------------
# ш | 3 | 2 | 1 | 1 | 2 | 3 |
#-----------------------------
# к | 4 | 3 | 2 | 2 | 2 | 3 |
#-----------------------------
# а | 5 | 4 | 3 | 3 | 3 | 2 |
#-----------------------------


def levenshtein_distance(S1, S2):
    def fill_matrix(S1_idx, S2_idx):
        if S1_idx < 0:
            return S2_idx + 1
        elif S2_idx < 0:
            return S1_idx + 1
        if M[S1_idx][S2_idx] == -1:
            if S1[S1_idx] == S2[S2_idx]:
                M[S1_idx][S2_idx] = (fill_matrix(S1_idx - 1, S2_idx - 1))
            else:
                substitute_last = fill_matrix(S1_idx - 1, S2_idx - 1)
                add_last = fill_matrix(S1_idx - 1, S2_idx)
                delete_last = fill_matrix(S1_idx, S2_idx - 1)
                M[S1_idx][S2_idx] = (1 + min(substitute_last, add_last, delete_last))
        return M[S1_idx][S2_idx ]
    M = [[-1] * len(S2) for _ in S1]
    return fill_matrix(len(S1) - 1, len(S2) - 1)
print(levenshtein_distance('кошка', 'кофта'))
