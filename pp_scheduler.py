def pp_scheduler(pp, mbs):
    pp_sc = [[] for _ in range(pp)]

    def insert_to_empty(p, s, elem):
        q = pp_sc[p]
        while s < len(q):
            if q[s] is None:
                q[s] = elem
                return s
            s += 1
        q.extend([None] * (s - len(q)))
        q.append(elem)
        return len(q) - 1

    for b in range(mbs):
        s = 0
        for p in range(pp):
            s = insert_to_empty(p, s, ('F', b)) + 1
        for p in range(pp - 1, -1, -1):
            s = insert_to_empty(p, s, ('B', b)) + 1
    return pp_sc


if __name__ == '__main__':
    pp = 4
    mbs = 4
    sche = pp_scheduler(pp, mbs)
    for r in sche:
        print(r)
