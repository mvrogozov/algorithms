def get_anagrams2(strings):
    result = []
    has_pair = set()
    for index, value in enumerate(strings):
        if index in has_pair:
            continue
        pair = (index,)
        word_1 = list(value)
        word_1.sort()
        for sub_index in range(index + 1, len(strings)):
            if (
                len(value) != len(strings[sub_index])
                ) or (
                    sub_index in has_pair
            ):
                continue
            word_2 = list(strings[sub_index])
            word_2.sort()
            #print(word_1, word_2)
            found = word_1 == word_2
            if found:
                pair += (sub_index,)
                has_pair.add(index)
                has_pair.add(sub_index)
        '''if len(pair) > 1:
            result.append(pair)
        if index not in has_pair:'''
        result.append(pair)
    return result


def get_anagrams(strings):
    result = {}
    has_pair = set()
    for index, value in enumerate(strings):
        if index in has_pair:
            continue
        word_1 = list(value)
        word_1.sort()
        word_1 = ''.join(word_1)
        if result.get(word_1) is None:
            result.setdefault(word_1, (index,))
        else:
            result[word_1] += (index,)
    return result.values()



def main():
    input()
    text = input().split()
    result = get_anagrams(text)
    for item in result:
        print(*item)


def main1():
    #text = ['ate', 'pol', 'tea', 'lop', 'zztop', 'eta']
    text = 'uz zx mc fi vj az uw ky fz jk yp wc tp av ga yq vo ct yy lr ux uy fe le xu ss xg pj gg rv yi ly mm sh nc ae ak at db sn co no is nz dk bh hy uc tf vn gh nn mq bp nt dg sq yv mw gx as lf lg ju rb bl ud vz rd fe gt ha zj vu kg cn jl vw zu zu uz zu zu uz uz zu uz zu zu uz uz uz uz zu uz zu uz uz zu uz zu uz zu zu uz zu zu zu zu zu zu zu zu zu zu uz zu'
    #text = 'mc mm'
    text = 'eat tea ate nat bat'
    #text = 'rama ramm amar'
    text = text.split()
    result = get_anagrams(text)
    for item in result:
        print(*item)




if __name__ == '__main__':
    main()
