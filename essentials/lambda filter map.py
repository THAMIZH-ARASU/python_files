def triplet(x):
    return x * x * x


num = [0, 1, 2, 3, 4, 8, 6, 5]
txt = map(triplet, num)
print(list(txt))
