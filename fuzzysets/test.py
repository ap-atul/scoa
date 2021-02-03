from fuzzy import *

a = FuzzySet({"a": 0.5, "b": 0.3})
b = FuzzySet({"c": 0.9, "d": 0.002})

print(a)
print(b)
print()

# Set operations
print(a.comp())
print(a.diff(b))
print(a.inter(b))

# Relations
rel = a.cartesian(b)
print()
print(rel)

m_m = a.min_max_com(rel)
print(m_m)
