def delivery_cost(street, price):
    if "Аль-Фараби" in street or "Саина" in street or "Ташенова" in street or "Достык" in street:
        if price < 10000:
            return 500
        else:
            return 0
    else:
        if price < 10000:
            return 1000
        else:
            return 1000


print(delivery_cost(' 36', 1000))