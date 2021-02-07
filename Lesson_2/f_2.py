import json


def write_order_to_json(item, quantity, price, buyer, date):

    with open('Студентам для решения домашнего задания\orders.json') as f:
        data = json.load(f)
    data['orders'] = [{item, quantity, price, buyer, date}]
    print(data)
    print(type(data))

    with open("Студентам для решения домашнего задания\orders.json", "w") as write_f:
        json.dump(data, write_f, sort_keys=True, indent=4)


write_order_to_json('Phone', '5', '100', 'User', '21.01.2021')

# {"orders": []}


