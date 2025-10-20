"""
# a -> min
# b -> between
# c -> max
"""

a = 2
b = 0
c = 1

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(a, b, c)



