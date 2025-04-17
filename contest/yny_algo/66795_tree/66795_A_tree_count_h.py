#n = int(input())
n = 9
data = """Alexei Peter_I
Anna Peter_I
Elizabeth Peter_I
Peter_II Alexei
Peter_III Anna
Paul_I Peter_III
Alexander_I Paul_I
Nicholaus_I Paul_I"""

n = 10
data = """AQHFYP MKFXCLZBT
AYKOTYQ QIUKGHWCDC
IWCGKHMFM WPLHJL
MJVAURUDN QIUKGHWCDC
MKFXCLZBT IWCGKHMFM
PUTRIPYHNQ UQNGAXNP
QIUKGHWCDC WPLHJL
UQNGAXNP WPLHJL
YURTPJNR QIUKGHWCDC"""


n = 10
data = """BFNRMLH CSZMPFXBZ
CSZMPFXBZ IHWBQDJ
FMVQTU FUXATQUGIG
FUXATQUGIG IRVAVMQKN
GNVIZ IQGIGUJZ
IHWBQDJ LACXYFQHSQ
IQGIGUJZ JMUPNYRQD
IRVAVMQKN GNVIZ
JMUPNYRQD BFNRMLH"""


def count_h(n: int, data: str):
    data = data.strip()
    data = list(data.split('\n'))
    persons = dict()
    ans = []
    for pos, pair in enumerate(data):
        p1, p2 = pair.split()
        child = persons.setdefault(p1, [len(persons), None])
        parent = persons.setdefault(p2, [len(persons), None])
        child[1] = p2
    for name, info in persons.items():
        parent = info[1]
        cnt = 0
        while parent:
            cnt += 1
            parent = persons[parent][1]
        ans.append((name, cnt))
    ans.sort()
    for item in ans:
        print(*item)


n = int(input())
data = ''
for i in range(n - 1):
    data += input() + '\n'
count_h(n, data)
