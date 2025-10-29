k = int(input("Кол-во стран:"))
countries = {}

for i in range(k):
    line = input(f"{i+1} название страны и города через пробел:").split()
    country_name = line[0]
    cities = line[1:]
    countries[country_name] = cities

print("\nПоиск городов")
cities_to_find = []
for _ in range(3):
    city_name = input(f"Введите город {len(cities_to_find)+1}:")
    cities_to_find.append(city_name)
for city in cities_to_find:
    found = False
    for country, city_list in countries.items():
        if city in city_list:
            print("Город",city,"расположен в стране",country)
            found = True
            break
    if not found:
        print("По городу",city,"данных нет")