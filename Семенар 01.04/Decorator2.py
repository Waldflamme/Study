def show_args(func):
    def wrap(*args, **kwargs):
        for i in range(0, len(args)):
            print(args[i], type(args[i]).__name__)

        for key, value in kwargs.items():
            print(key, '=', value, type(value).__name__)

        result = func(*args, **kwargs)
        return result
    return wrap

# Пример использования
@show_args
def example_func(a, b, c=10):
    return a + b + c

@show_args
def name_age(name, age=None):
    return name, age

example_func(5, 3, c=7)
print()
name_age(name="Анна", age=25)
