# Usual way
x = [1, 2, 3, 4, 5]
for i in x:
    print(i)


# SAME, but now different
x = [1, 2, 3, 4, 5]
y = iter(x)
try:
    while True:
        print(next(y))
except:
    pass