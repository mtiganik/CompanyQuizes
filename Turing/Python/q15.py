def some_func(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True

    return all(first == x for x in iterator)

list = [True, True,True, True]
print(some_func(list))