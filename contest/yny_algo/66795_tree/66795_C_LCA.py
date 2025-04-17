import sys
sys.setrecursionlimit(100000)


def make_path(root: str, person_childs: list, path: list, res: dict):
    path.append(root)
    for person in person_childs[root]:
        make_path(person, person_childs, path, res)
        res.update({person: list(path)})
        path.pop()


def find_path(n: int, data: list):
    # data = data.strip()
    # data = list(data.split('\n'))
    questions = data[-(len(data) - n + 1):]
    data = data[: n - 1]
    person_anc = dict()
    person_childs = dict()
    childs = set()
    parents = set()
    ans = {}
    for pair in data:
        child, ancestor = pair.split()
        person_childs.setdefault(child, [])
        parent = person_childs.setdefault(ancestor, [])
        parent.append(child)
        childs.add(child)
        parents.add(ancestor)

        person_anc.setdefault(child, [])
        child = person_anc.setdefault(child, [])
        child.append(ancestor)
    root = parents.difference(childs).pop()
    ans.setdefault(root, [root,])
    path = []
    make_path(root, person_childs, path, ans)
    for pair in questions:
        p1, p2 = pair.split()
        i = 0
        while i < len(ans[p1]) and i < len(ans[p2]):
            if ans[p1][i] == ans[p2][i]:
                if (i == len(ans[p1]) - 1) or (i == len(ans[p2]) - 1):
                    print(ans[p1][i])
                i += 1
                continue
            print(ans[p1][i - 1])
            break


with open('input.txt') as f:
    n = int(f.readline())
    data = f.read().splitlines()
find_path(n, data)


# n = 9
# data = """Alexei Peter_I
# Anna Peter_I
# Elizabeth Peter_I
# Peter_II Alexei
# Peter_III Anna
# Paul_I Peter_III
# Alexander_I Paul_I
# Nicholaus_I Paul_I
# Alexander_I Nicholaus_I
# Peter_II Paul_I
# Alexander_I Anna"""

# find_path(n, data)
