## Fuzzy Sets
The values in fuzzy sets are unclear, like normal set the value
are either present or absent, but in fuzzy sets the value can have 
some percent value ranging from (0 -> 1) closer to 0 denotes absent,
closer to 1 denotes present.


## Usage

```python
# delcare a set
A = FuzzySet( [ ('a', 1), ('b', 0.5), ('c', 0.6) ] )

# or with dictionary
B = FuzzySet( {'d': 0.8, 'e': 0.01, 'f': 0.4})

# set operations
# union
out = A.union(B)

# intersection
out = A.inter(B)

# complement
out = A.comp()

# difference
out = A.diff(B)

# cartesian product (out type is FuzzyRel)
out = A.cartesian(B)

# relations
# declare a relation
R = FuzzyRel([ [1, 0.8, 0.1], [ 0.8, 0.6, 0.3], [0.6, 0.3, 0.1]])

# declare a set
A = FuzzySet({"a": 0.9, "b": 0.4, "C": 1})

# min-max composition
out = A.min_max_com(R)

# resultant fuzzy set
@fuzzy
{'a': 0.9, 'b': 0.8, 'c': 0.3}

```

# TODO
* Relations
