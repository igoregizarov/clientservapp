word_1 = "разработка"
word_2 = "сокет"
word_3 = "декоратор"

print(type(word_1))
print(type(word_2))
print(type(word_3))
print(word_1, word_2, word_3)

enc_word_1 = word_1.encode('utf-8')
print(type(enc_word_1))
print(enc_word_1)
enc_word_2 = word_2.encode('utf-8')
print(type(enc_word_2))
print(enc_word_2)
enc_word_3 = word_3.encode('utf-8')
print(type(enc_word_3))
print(enc_word_3)