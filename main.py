import json

from data.cities import *
import _json

#with open("cities.json", "w", encoding="utf-8") as file:
#    json.dump(cities_list, file, ensure_ascii=False, indent=4)

#with open("cities.json", "r", encoding="utf-8") as file:
#    cities_list = json.load(file)

#print(cities_list)

cities_set = {city['name'] for city in cities_list}
print(cities_set)

computer_city = ''

while True:
    #Ход человека

    #Ввод города
    human_city = input("Введите город:")

    #проверка наличия города в списке

    if human_city.lower() in {city.lower() for city in cities_set}:
        print(f"Город {human_city} есть в списке.")
    else:
        print(f"Города {human_city} нет в списке. Человек проиграл")
        break

    #проверка, а бы ход компьютеру

    if computer_city:
        if human_city[0].lower() == computer_city[-1].lower():
            print("Условия выполнены, ход компьютеру.")

        else:
            print(f"Условия не выполнены, город должен начинаться с {computer_city[-1].upper()}")
            break

    #ход компьютеру

    #перебор сета с городами, подбор подходящего города по первой букве

    for city in cities_set:
        if human_city[-1].lower() == city[0].lower():
            computer_city = city
            print(f"Компьютер выбрал город {computer_city}")
            break
    else:
         #если в цикле не сработал break мы попадем сюда
        print("Компьютер не смог выбрать город")
        break

