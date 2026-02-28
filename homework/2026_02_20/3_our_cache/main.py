def cache(func):
    cached_results = {}
    
    def wrapper(*args):
        norm_args = tuple(sorted(args))

        if norm_args in cached_results:
            print("Беру из кеша")
            return cached_results[norm_args]

        result = func(*args)
        cached_results[norm_args] = result
        print("Вычисляю и кеширую...")
        return result
    return wrapper

@cache
def my_sum(*numbers):
    return sum(numbers)

def main():
    print(my_sum(16, 26))
    print(my_sum(26, 16))
    print(my_sum(20, 16, 6))

if __name__ == '__main__':
    main()
