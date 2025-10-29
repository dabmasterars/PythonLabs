n = int(input("Введите кол-во заказов: "))
orders = {}
#структура: {имя покупателя: {название пиццы: количество, ...}, ...}
for i in range(1, n + 1):
    line = input(f"{i} заказ: ").split()
    customer = line[0]
    pizza_name = line[1]
    quantity = int(line[2])
    if customer not in orders:
        orders[customer] = {}
    if pizza_name in orders[customer]:
        orders[customer][pizza_name] += quantity
    else:
        orders[customer][pizza_name] = quantity

for customer in sorted(orders):
    print(customer,":")
    for pizza, total_qty in orders[customer].items():
        print(pizza,":",total_qty)