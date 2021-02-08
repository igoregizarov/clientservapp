import json

# with open('Студентам для решения домашнего задания/orders.json') as f:
#     data = json.load(f)
#     print(data)


def write_order_to_json(item, quantity, price, buyer, date):
    data = dict
    with open('Студентам для решения домашнего задания/orders.json') as f:
        data = json.load(f)
    if not 'orders' in data:
        data['orders'] = []
    data['orders'].append({
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    })
    print(data)
    print(type(data))

    with open("Студентам для решения домашнего задания/orders.json", "w") as write_f:
        json.dump(data, write_f, indent=4)


write_order_to_json('Phone', '5', '100', 'User', '21.01.2021')

# {"orders": []}


