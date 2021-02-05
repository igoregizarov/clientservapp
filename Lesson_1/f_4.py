word_1 = "разработка"
word_2 = "администрирование"
word_3 = "protocol"
word_4 = "standart"


def code(word):
    print(type(word))
    print(word)
    enc_word = word.encode('utf-8')
    print(type(enc_word))
    print(enc_word)
    dec_word = enc_word.decode('utf-8')
    print(type(dec_word))
    print(dec_word, end='\n\n')


code(word_1)
code(word_2)
code(word_3)
code(word_4)