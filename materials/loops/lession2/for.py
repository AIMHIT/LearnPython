"""
Один из основных циклов, которые встречаются во всех или почти
во всех языках программирования, это - цикл for.

Вам может быть привычние ситаксис на подобие
    for i = 1; i > 10; i++
или что-нибудь подобное, но в python эту конструкцию решили упросить:
    for i in {что-то итерируемое}:
        {Тело цикла}

Чаще всего под чем то итерируемым вы будете использовать специальный объект range.
Также это могут быть списки, словари, строки и тд.

Как и в других языках в python есть операторы break и continue.
    break - досрочно завершает цикл.
    continue - переход на следующую итерацию цикла.

Также в python циклы имеют дополнительную конструкцию else, которая записывается после цикла.
Эта конутрукция позволяет выполнять определенный блок кода при условии, что цикл досрочно не завершил свою работу
с помощью оператора break

    for i in range(10):
        ...
    else:
        ...
"""

def loop():
    """
    >>> loop() # doctest: +NORMALIZE_WHITESPACE
    0 1 2 3 4 5 6 7 8 9
    """
    for i in range(10):
        print(i, end=' ')

def loop_with_break():
    """
    >>> loop_with_break() # doctest: +NORMALIZE_WHITESPACE
    0 1 2 3 4
    """
    for i in range(10):
        if i == 5:
            break
        print(i, end=' ')

def loop_with_continue():
    """
    >>> loop_with_continue() # doctest: +NORMALIZE_WHITESPACE
    0 1 2 3 4 6 7 8 9
    """
    for i in range(10):
        if i == 5:
            continue
        print(i, end=' ')

def loop_with_else():
    """
    >>> loop_with_else() # doctest: +NORMALIZE_WHITESPACE
    0 1 2 3 4 5 6 7 8 9 else
    """
    for i in range(10):
        print(i, end=' ')
    else:
        print("else")

def loop_with_else_and_break():
    """
    >>> loop_with_else_and_break() # doctest: +NORMALIZE_WHITESPACE
    0 1 2 3 4
    """
    for i in range(10):
        if i == 5:
            break
        print(i, end=' ')
    else:
        print("else")

def loop_iterable():
    """
    >>> loop_iterable() # doctest: +NORMALIZE_WHITESPACE
    a
    b
    c
    """
    for i in ["a", "b", "c"]:
        print(i)