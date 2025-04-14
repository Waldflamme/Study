def validate(default_value, invalid_values=(None, '', 0, [], {}, False)):
    def dec(func):
        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            if result in invalid_values:
                print(f"Значение некорректно: {result}. Замена: {default_value}")
                return default_value
            return result
        return wrap
    return dec

@validate(default_value="No data")
def get_name(user_id):
    users = {1: "Dave", 2: "Lenny"}
    return users.get(user_id)

print(get_name(1))
print(get_name(3))