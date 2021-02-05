import locale
def_coding = locale.getpreferredencoding()
print(def_coding)

with open('test_file.TXT') as f:
    print(f)
    for line in f:
        print(line)

with open('test_file.TXT', encoding='utf-8') as f:
    print(f)
    for line in f:
        print(line)