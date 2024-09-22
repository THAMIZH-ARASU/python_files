txt = ['ram', 'janu', 'kathick', 'jessi']


def func(x):
    print(x * 3)


def map(test, txt):
    for items in txt:
        test(items)


map(func, txt)
