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
        return str(self._set)

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
        for key in self._set:
            self._set[key] = 1 - self._set[key]

        return self

    def diff(self, other):  # min(deg(A), 1 - deg(B))
        return self.inter(other.comp())

    def cartesian(self, other):  # min(deg(Ax), deg(By))
        ret = dict()

        for akey, aval in self._set.items():
            min_ele = (akey, aval)
            for bkey, bval in other._set.items():
                min_ele  = min(min_ele, (akey, aval), (bkey, bval), key= lambda x: x[1])

            if min_ele[0] in ret:
                ret[str(min_ele[0]) + "_"] = min_ele[1]
            else:
                ret[min_ele[0]] = min_ele[1]

        return FuzzySet(ret)






