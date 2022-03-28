import itertools

# def gen_all_posible(p_char, lenght):
#     posible_table = []
#     for p in p_char:
#         len_cache = 0
#         gen_text = ""
#         gen_text += p
#         while len_cache < lenght - 1:
#             gen_text += p_char[len_cache]
#             len_cache += 1
#         posible_table.append(gen_text)


# gen_all_posible("ATGC", 2)

def gen_all_posible(p_char, lenght):
    x = []
    for output in itertools.product(p_char, repeat=lenght):
        output = list(output)
        x.append(output)
    return x


def Spectrum(seq, l):
    S = []
    for i in range(len(seq) - l + 1):
        S.append(list(seq[i:i+l]))
    S.sort()
    return S


def find_repeat(posible_list, spectrum_list):
    score = [0] * len(posible_list)
    for p_ix in range(len(posible_list)):
        for s_ix in range(len(spectrum_list)):
            if posible_list[p_ix] == spectrum_list[s_ix]:
                score[p_ix] += 1
    return score


def print_repeat(posible_list, repeat_score):
    rp_str = []
    for p_ix in range(len(posible_list)):
        if repeat_score[p_ix] > 0:
            rp_str.append(''.join(posible_list[p_ix]))
    print(rp_str)


p_list = gen_all_posible("ATGC", 2)
s_list = Spectrum("ATCGATCGTACG", 2)
rp_score = find_repeat(p_list, s_list)
print_repeat(p_list, rp_score)
