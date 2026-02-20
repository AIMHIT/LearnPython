start = 0
end = 10
step = 2

# if start > end:
#     step = -step
# step = -step if start > end else step
#
# last_i = None
#
# for i in range(start, end):
#     if i == 5:
#         last_i = i
#         break
#     print(i)
# print("end ", last_i)


condition = True

# while start != end:
#     print(start)
#     start += 1
#     if start == 8:
#         start += 10

my_list = [1 for i in range(5)]

# print(my_list)

my_tuple = tuple(1 for _ in range(5))

# print(my_tuple)

my_set = set(i if i != 4 else 1 for i in range(5))
# print(my_set)

my_dict = {str(i): i if i % 2 else None for i in range(5)}

# print(my_dict)

"""
Дано
Кол-во 26
Макс кол-во процессов 10
Макс кол-во потоков 10

[10, 10, ..., 10]
[10, 10, 6]

"""

MyVar = 1

mySecondVar = 3

python_language = "python"

