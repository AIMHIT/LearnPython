import json
import os

def cache(filename="cache.json", key_type="args"):
    def decorator(func):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                cache_dict = json.load(f)
            print(f"Загрузили кеш из {filename}")
        else:
            cache_dict = {}

        def wrapper(*args, **kwargs):
            if key_type == "args":
                key = str(sorted(args))
            elif key_type == "kwargs":
                key = str(sorted(kwargs.items()))
            else:
                key = str(args) + str(sorted(kwargs.items()))

            if key in cache_dict:
                print(f"Взяли из кеша:")
                return cache_dict[key]

            result = func(*args, **kwargs)
            cache_dict[key] = result

            with open(filename, 'w') as f:
                json.dump(cache_dict, f)

            print(f"Вычислили и сохранили:")
            return result
        return wrapper
    return decorator

@cache(filename="sum_cache.json", key_type="args")
def my_sum(*numbers):
    return sum(numbers)

@cache(filename="greet_cache.json", key_type="kwargs")
def greet(**info):
    return f"Привет, {info.get('name', 'друг')}!"


print(my_sum(23, 20, -1))
print(greet(name="Мир"))
print(greet())
