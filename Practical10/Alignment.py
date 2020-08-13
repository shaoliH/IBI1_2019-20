S = -11
E = -1
MIN = -float("inf")
amino = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z',
         'X', '*']
blosum = [
    [4, -1, -2, -2, 0, -1, -1, 0, -2, -1, -1, -1, -1, -2, -1, 1, 0, -3, -2, 0, -2, -1, 0, -4],
    [-1, 5, 0, -2, -3, 1, 0, -2, 0, -3, -2, 2, -1, -3, -2, -1, -1, -3, -2, -3, -1, 0, -1, -4],
    [-2, 0, 6, 1, -3, 0, 0, 0, 1, -3, -3, 0, -2, -3, -2, 1, 0, -4, -2, -3, 3, 0, -1, -4],
    [-2, -2, 1, 6, -3, 0, 2, -1, -1, -3, -4, -1, -3, -3, -1, 0, -1, -4, -3, -3, 4, 1, -1, -4],
    [0, -3, -3, -3, 9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4],
    [-1, 1, 0, 0, -3, 5, 2, -2, 0, -3, -2, 1, 0, -3, -1, 0, -1, -2, -1, -2, 0, 3, -1, -4],
    [-1, 0, 0, 2, -4, 2, 5, -2, 0, -3, -3, 1, -2, -3, -1, 0, -1, -3, -2, -2, 1, 4, -1, -4],
    [0, -2, 0, -1, -3, -2, -2, 6, -2, -4, -4, -2, -3, -3, -2, 0, -2, -2, -3, -3, -1, -2, -1, -4],
    [-2, 0, 1, -1, -3, 0, 0, -2, 8, -3, -3, -1, -2, -1, -2, -1, -2, -2, 2, -3, 0, 0, -1, -4],
    [-1, -3, -3, -3, -1, -3, -3, -4, -3, 4, 2, -3, 1, 0, -3, -2, -1, -3, -1, 3, -3, -3, -1, -4],
    [-1, -2, -3, -4, -1, -2, -3, -4, -3, 2, 4, -2, 2, 0, -3, -2, -1, -2, -1, 1, -4, -3, -1, -4],
    [-1, 2, 0, -1, -3, 1, 1, -2, -1, -3, -2, 5, -1, -3, -1, 0, -1, -3, -2, -2, 0, 1, -1, -4],
    [-1, -1, -2, -3, -1, 0, -2, -3, -2, 1, 2, -1, 5, 0, -2, -1, -1, -1, -1, 1, -3, -1, -1, -4],
    [-2, -3, -3, -3, -2, -3, -3, -3, -1, 0, 0, -3, 0, 6, -4, -2, -2, 1, 3, -1, -3, -3, -1, -4],
    [-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4, 7, -1, -1, -4, -3, -2, -2, -1, -2, -4],
    [1, -1, 1, 0, -1, 0, 0, 0, -1, -2, -2, 0, -1, -2, -1, 4, 1, -3, -2, -2, 0, 0, 0, -4],
    [0, -1, 0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1, 1, 5, -2, -2, 0, -1, -1, 0, -4],
    [-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1, 1, -4, -3, -2, 11, 2, -3, -4, -3, -2, -4],
    [-2, -2, -2, -3, -2, -1, -2, -3, 2, -1, -1, -2, -1, 3, -3, -2, -2, 2, 7, -1, -3, -2, -1, -4],
    [0, -3, -3, -3, -1, -2, -2, -3, -3, 3, 1, -2, 1, -1, -2, -2, 0, -3, -1, 4, -3, -2, -1, -4],
    [-2, -1, 3, 4, -3, 0, 1, -1, 0, -3, -4, 0, -3, -3, -2, 0, -1, -4, -3, -3, 4, 1, -1, -4],
    [-1, 0, 0, 1, -3, 3, 4, -2, 0, -3, -3, 1, -1, -3, -1, 0, -1, -3, -2, -2, 1, 4, -1, -4],
    [0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2, 0, 0, -2, -1, -1, -1, -1, -1, -4],
    [-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, 1],
]


# return match or mismatch score
def _match(s, t, i):
    index1 = amino.index(t[i - 1])
    index2 = amino.index(s[i - 1])
    return blosum[index1][index2]


# initializers for matrices
def _init_x(i, j):
    if i > 0 and j == 0:
        return MIN
    else:
        if j > 0:
            return S + E * j
        else:
            return 0


def _init_y(i, j):
    if j > 0 and i == 0:
        return MIN
    else:
        if i > 0:
            return S + E * i
        else:
            return 0


def _init_m(i, j):
    if j == 0 and i == 0:
        return 0
    else:
        if j == 0 or i == 0:
            return MIN
        else:
            return 0


def distance_matrix(s, t):
    dim_i = len(t) + 1
    # abuse list comprehensions to create matrices
    X = [[_init_x(i, j) for j in range(0, dim_i)] for i in range(0, dim_i)]
    Y = [[_init_y(i, j) for j in range(0, dim_i)] for i in range(0, dim_i)]
    M = [[_init_m(i, j) for j in range(0, dim_i)] for i in range(0, dim_i)]

    for j in range(1, dim_i):
        for i in range(1, dim_i):
            X[i][j] = max((S + E + M[i][j - 1]), (E + X[i][j - 1]))
            Y[i][j] = max((S + E + M[i - 1][j]), (E + Y[i - 1][j]))
            M[i][j] = max(_match(s, t, i) + M[i - 1][j - 1], X[i][j], Y[i][j])
    return M


def backtrace(s, t, M):
    sequ1 = ''
    sequ2 = ''
    cnt = 0
    for i in range(len(s)):
        cnt += s[i] == t[i]
    i = len(t)
    while (i > 0):
        if (M[i][i] == M[i - 1][i - 1] + _match(s, t, i)):
            sequ1 += s[i - 1]
            sequ2 += t[i - 1]
            i -= 1

    sequ1r = ' '.join([sequ1[j] for j in range(-1, -(len(sequ1) + 1), -1)])
    sequ2r = ' '.join([sequ2[j] for j in range(-1, -(len(sequ2) + 1), -1)])

    return [sequ1r, sequ2r, cnt / len(s)]


HUMAN = "MTGVFDRRVPSIRSGDFQAPFQTSAAMHHPSQESPTLPESSATDSDYYSPTGGAPHGYCSPTSASYGKALNPYQYQYHGVNGSAGSYPAKAYADYSYASSYHQYGGAYNRVPSATNQPEKEVTEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYTSAASSINSHLPPPGSLQHPLALASGTLY"
MOUSE = "MTGVFDRRVPSIRSGDFQAPFPTSAAMHHPSQESPTLPESSATDSDYYSPAGAAPHGYCSPTSASYGKALNPYQYQYHGVNGSAAGYPAKAYADYGYASPYHQYGGAYNRVPSATSQPEKEVAEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYPSAASSINSHLPPPGSLQHPLALASGTLY"
RANDOM = "GWICFCFTTDHEIDENSFCYMDMNIAMVCEDTSCICQGPQQQGLWLFWLLPTWWHLNCPLPVVAWTRHRYWDNRNMVECAGGVGRSKSHRSSHYCEQNSPDVCWMWDSIFTEITWLTQEPERAYDDISVSSSALECILEWRLESEYMTGAVGEVNHCCYQFDQLQCYVSHSIVQLHVGWYTFPTHQHQIHRGFGNDLGRDGELIKWHHLPHTFRIKWLSTQPTFDPWYWYKWTMLDCENFGNLADARMITMVQLSHDCSEMNQWDTKEKMYRYHWNRPDAYKNIAFYPD "

seq1 = HUMAN
seq2 = MOUSE

M = distance_matrix(seq1, seq2)
[str1, str2, rate_identity] = backtrace(seq1, seq2, M)

score = M[len(seq2)][len(seq1)]
print(str1)
print(str2)
print("Alignment Score:" + str(score))
print("Rate identity:" + str(rate_identity))
