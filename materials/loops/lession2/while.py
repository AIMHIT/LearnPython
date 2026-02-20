"""
Если цикл for хотя бы как-то отличался синтаксисом от аналогичных циклов на
других языках программирования, то цикл while не отличается ничем кроме уже пройденной констркции
else вместе с циклом.

Обычный while

    while {условие, тут может быть truthy или falsy значение}:
        ...

while с else
    while {условие, тут может быть truthy или falsy значение}:
        ...
    else:
        ...
"""

def standard_while():
    """
    >>> standard_while() # doctest: +NORMALIZE_WHITESPACE
    0 1 2 3 4
    """
    i = 0
    while i < 5:
        print(i, end=' ')
        i += 1

def while_with_if():
    """
    >>> while_with_if() # doctest: +NORMALIZE_WHITESPACE
    0 1 2 3 4
    """
    i = 0
    condition = True
    while condition:
        print(i, end=' ')
        i += 1
        if i == 5:
            condition = False

def while_with_break():
    """
    >>> while_with_break() # doctest: +NORMALIZE_WHITESPACE
    0 1 2 3 4 5
    """
    i = 0
    while i < 10:
        print(i, end=' ')
        i += 1
        if i == 6:
            break

def while_with_continue():
    """
    >>> while_with_continue() # doctest: +NORMALIZE_WHITESPACE
    1 3 4 5
    """
    i = 0
    while i < 5:
        i += 1
        if i == 2:
            continue
        print(i, end=' ')

def while_with_else():
    """
    >>> while_with_else() # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    0 1 2 3 4 5 6 7 8 9 else
    """
    i = 0
    while i < 10:
        print(i, end=' ')
        i += 1
    else:
        print("else")

def while_with_else_break():
    """
    >>> while_with_break() # doctest: +NORMALIZE_WHITESPACE
    0 1 2 3 4 5
    """
    i = 0
    while i < 10:
        print(i, end=' ')
        i += 1
        if i == 6:
            break
    else:
        print("else")
