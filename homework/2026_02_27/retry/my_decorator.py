def retry(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(count):
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    print(f"Попытка {attempt + 1}: ValueError, пробуем снова...")
                    continue
                except OSError:
                    print(f"{func.__name__} raise OSError exception.")
                    continue
                except Exception as e:
                    print(f"Неожиданное исключение: {e}")
                    raise

            print(f"Все {count} попыток исчерпаны. Возвращаем None")
            return None
        return wrapper
    return decorator
