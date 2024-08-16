from data.cities import*
# Собираем set всех городов в нижнем регистре
cities_set = {city["name"].lower() for city in cities_list}

# Цикл в цикле
iter_count = 0
bad_letters = set()
for city in cities_set:
    last_letter = city[-1]
    for city_2 in cities_set:
        first_letter = city_2[0]
        iter_count += 1
        if last_letter == first_letter:
            break
    else:
        bad_letters.add(last_letter)

print(bad_letters)
print(iter_count)

all_letter = set(str(cities_set))
print(all_letter)