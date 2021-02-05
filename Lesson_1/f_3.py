try:
    word_1 = b"attribute"
    print(word_1)
    print(type(word_1))
except SyntaxError as error:
    print(error)
try:
    word_2 = b"класс"
    print(word_2)
    print(type(word_2))
except SyntaxError as error:
    print(error)
try:
    word_3 = b"функция"
    print(word_3)
    print(type(word_3))
except SyntaxError as error:
    print(error)
try:
    word_4 = b"type"
    print(word_4)
    print(type(word_4))
except SyntaxError as error:
    print(error)

"""
Вылетает синтаксическая ошибка при попытки работы с не латинскими буквами:
SyntaxError: bytes can only contain ASCII literal characters.
"""