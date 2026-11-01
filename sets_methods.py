A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print('A=', A)
print('B=', B)

A.add(9)
print('After A.add(9):', A)

A_copy = A.copy()
print('A_copy=', A_copy)

print('A.difference(B):', A.difference(B))

A_diff = A.copy()
A_diff.difference_update(B)
print('After difference update, A_diff:', A_diff)

A.discard(2)
A.discard(100)
print('After discard:', A)

print('A.intersection(B):', A.intersection(B))

A_int = A.copy()
A_int.intersection_update(B)
print('After intersection_update', A_int)

C = {10, 11}
print('A.isdisjoint(C):', A.isdisjoint(C))
print('A.is disjoint(B):', A.isdisjoint(B))

print('{4, 5}.issubset(B):', {4, 5}.issubset(B))
print('A.issubset(B)', A.issubset(B))

print('B.issuperset({4,5}):', B.issuperset({4, 5}))

popped = A.pop()
print('popped element:', popped)
print('After pop:', A)

A.remove(3)
try:
    A.remove(100)
except KeyError as e:
    print('Remove (100) raised KeyError as expected')

print('A^B:', A.symmetric_difference(B))

A_sym = A.copy()
A_sym.symmetric_difference_update(B)
print('After symmetric_difference_update:', A_sym)

print('A | B:', A.union(B))

A_upd = A.copy()
A_upd.update({10, 11})
print('After update ({10, 11}):', A_upd)

temp = {1, 2, 3}
temp.clear()
print('After clear:', temp)









