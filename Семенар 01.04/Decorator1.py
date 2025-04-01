def print_res(func):
    def wrapp(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapp

# Пример использования
@print_res
def add(a, b):
    return a + b

@print_res
def multiply(a, b):
    return a * b

@print_res
def name_out(name):
    return name


add(3, 5)
multiply(4, 6)
name_out("Анна")
