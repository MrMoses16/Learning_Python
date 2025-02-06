# sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print("A:", A)
print("B:", B)

# Join A and B
C = A.union(B)
print(C)

# Find A intersection B
intersect_A_B = A.intersection(B)
print(intersect_A_B)

# Is A subset of B
print("Is A subset of B:", end = ' ')
if A.issubset(B):
    print("True")
else:
    print("False")

# Are A and B disjoint sets
print("Are A and B disjoint sets:", end = ' ')
if A.isdisjoint(B):
    print("True")
else:
    print("False")

# Join A with B and B with A
A_join_B = A.union(B)
B_join_A = B.update(A)

# What is the symmetric difference between A and B
print("What is the symmetric difference between A and B: {}" .format(A.symmetric_difference(B)))

# Delete the sets completely
del A
del B