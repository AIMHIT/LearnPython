def bread(func):
    def wrapper():
        result = func()
        return f"Bread\n{result}Bread"
    return wrapper

def salat(func):
    def wrapper():
        result = func()
        return f"Salat\n{result}"
    return wrapper

def tomato(func):
    def wrapper():
        result = func()
        return f"Tomato\n{result}"
    return wrapper

def meat(func):
    def wrapper():
        result = func()
        return f"Meat\n{result}"
    return wrapper

@bread
@salat
@tomato
@meat
def make_sandwich():
    return ''

def main():
    print(make_sandwich())

if __name__ == '__main__':
    main()
