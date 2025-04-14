def check_arg(expected_types=None):
    def dec(func):
        def wrap(*args, **kwargs):
            for i, arg in enumerate(args):
                if arg is None:
                    raise ValueError(f"Аргумент №{i+1} равен None")
            return func(*args, **kwargs)
        return wrap
    return dec

@check_arg(expected_types=(int, int))
def add(a, b):
    return a + b

print(add(5, 3))
print(add(5, None))
