import json

from data.cities import*
import _json
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



print(cities_list)

#with open("cities.json", "w", encoding="utf-8") as file:
#    json.dump(cities_list, file, ensure_ascii=False, indent=4)

#with open("cities.json", "r", encoding="utf-8") as file:
#    cities_list = json.load(file)

cities_set = {city['name'] for city in cities_list}
print(cities_set)

#while True:
    #Ход человека
    #Ввод города
    #human_city = input("Введите город:")