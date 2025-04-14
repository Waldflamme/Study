import inspect

def smart_arg_replace(arg_name, predic, replacement_fn):
    def dec(func):
        def wrap(*args, **kwargs):
            bound_args = inspect.signature(func).bind(*args, **kwargs)
            bound_args.apply_defaults()

            if arg_name in bound_args.arguments:
                original_value = bound_args.arguments[arg_name]
                if predic(original_value):
                    print(f"[!] Аргумент '{arg_name}' заменён: {original_value} → ", end="")
                    bound_args.arguments[arg_name] = replacement_fn(bound_args.arguments)
                    print(f"{bound_args.arguments[arg_name]}")

            return func(*bound_args.args, **bound_args.kwargs)
        return wrap
    return dec

@smart_arg_replace(
    arg_name="username",
    predic=lambda val: not val,
    replacement_fn=lambda args: args['first_name'].lower() + "." + args['last_name'].lower()
)
def greet(username, first_name, last_name):
    print(f"Привет, {username}!")

greet("", first_name="Анна", last_name="Иванова")

greet("a.ivanova", first_name="Анна", last_name="Иванова")