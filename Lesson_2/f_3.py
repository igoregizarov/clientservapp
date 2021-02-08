import yaml


dict_yaml = {
    'first': [],
    'second': 2,
    'fird': {
        1: 'U+20AC',
        2: 'U+0507'
    }
}

print(dict_yaml)

with open('my_first.yaml', 'w') as f:
    yaml.dump(dict_yaml, f, default_flow_style=False, allow_unicode=True)


with open('my_first.yaml') as f_n:
    f_n_content = yaml.load(f_n)
print(f_n_content)