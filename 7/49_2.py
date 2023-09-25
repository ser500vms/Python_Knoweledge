# Есть список словарей, нужно спросить как сортирнуть (по цене)
# и сортирнуть лямбдой

# def sort_low_to_up(list):
#     for _ in range(len(products) - 1):
#         for i in range(len(products) - 1):
#             if products[i]["price"] > products[i + 1]["price"]:
#                 temp = products[i + 1]
#                 products[i + 1] = products[i]
#                 products[i] = temp
#     return list

# def sort_up_to_low(list):
#     for _ in range(len(products) - 1):
#         for i in range(len(products) - 1):
#             if products[i]["price"] < products[i + 1]["price"]:
#                 temp = products[i + 1]
#                 products[i + 1] = products[i]
#                 products[i] = temp
#     return list

products = [
    {"name": "Шоколад", "price": 2.5, "quality": 100},
    {"name": "Молоко", "price": 1.0, "quality": 50},
    {"name": "Кофе", "price": 5.0, "quality": 30},
    {"name": "Чай", "price": 3.0, "quality": 80},
]

# how_sort = int(input('Нажми 1 чтобы сортировать по возрастанию или 0 по убыванию: '))
# if how_sort == 1:
#     print(sort_low_to_up(products))
# elif how_sort == 0:
#     print(sort_up_to_low(products))
# else:
#     print('Wrong number ashole!!!')

def sort_prod(products, ascending: bool):
    return sorted(products, key=lambda x: x["price"], reverse=not ascending)


def how_sort(products):
    word = input('Chose asc or desc: ').strip().lower()
    if word == 'asc':
       products = sort_prod(products, True)
    elif word == 'desc':
       products = sort_prod(products, False) 
    else:
        print('You are wrong')
        return 0
    for products in products:
         print(products)

how_sort(products)

 

