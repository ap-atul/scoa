class FuzzyRel:
    def __init__(self, mat):
        self._mat = mat

    def __repr__(self):
        string = ["@relation\n"]
        for i in range(len(self._mat)):
            string.append("|")
            for j in range(len(self._mat[0])):
                string.append(str(self._mat[i][j]))
            string.append("|\n")
        return '  '.join(string)

    @property
    def mat(self):
        return self._mat

class FuzzySet:
    def __init__(self, data):
        self._set = dict()

        if isinstance(data, dict):
            self._set = data
            return

        if not isinstance(data, (list, set)):
            raise Exception("Data should be type of list or set")

        if not isinstance(data[0], (tuple, list, set)):
            raise Exception("Each element in the data should be set, tuple or list")

        for item, val in data:
            if item in self._set:
                raise Exception("Sets cannot have duplicate values")
            self._set[item] = val

    def __getitem__(self, key):
        return self._set[key]

    def __repr__(self):
        return "@fuzzy\n" + str(self._set)

    def union(self, other):  # max(deg(A), deg(B))
        ret = dict()

        for akey, bkey in zip(self._set, other._set):
            aval , bval = self[akey], other[bkey]

            key, val = (akey, aval) if (aval > bval) else (bkey, bval)
            ret[key] = val

        return FuzzySet(ret)

    def inter(self, other):  # min(deg(A), deg(B))
        ret = dict()

        for akey, bkey in zip(self._set, other._set):
            aval , bval = self[akey], other[bkey]

            key, val = (akey, aval) if (aval < bval) else (bkey, bval)
            ret[key] = val

        return FuzzySet(ret)

    def comp(self):  # 1 - deg(A)
        ret = dict()
        for key in self._set:
            ret[key] = 1 - self._set[key]

        return FuzzySet(ret)

    def diff(self, other):  # min(deg(A), 1 - deg(B))
        return self.inter(other.comp())

    def cartesian(self, other):  # min(deg(Ax), deg(By))
        ret = list()

        for _, aval in self._set.items():
            ret.append([min(aval, bval) for _, bval in other._set.items()])

        return FuzzyRel(ret)

    def min_max_com(self, rel):   # B(x, z) = max( min(A(x, y), min(R(y, z)))
        if not isinstance(rel, FuzzyRel):
            raise Exception("FuzzyRel type is required for the composition.")

        ret, vec = list(), list(self._set.values())

        for c in range(len(rel.mat)):
            col = [x[c] for x in rel.mat]
            mins = [min(val) for val in zip(vec, col)]
            ret.append(max(mins))

        return FuzzySet(dict(zip(self._set.keys(), ret)))
