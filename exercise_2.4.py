# vegetables

vegetables = ["burak", "ziemniak", "szczypior", "cebula"]
veggie_iterator = iter(vegetables)
# print(veggie_iterator)
# for vegetable in veggie_iterator:
#     print(vegetable)
try:
    for i in range(5):
        print(next(veggie_iterator))
except StopIteration:
    print("za mało obiektów w liscie")

# items with price

shopping = [("buraki", 1.25), ("mleko", 4.0), ("chleb", 3.50), ("wino", 15)]

for product, price in shopping:
    print(product)

shopping_dict = dict(shopping)
print(shopping_dict)
for product in shopping_dict:
    print(product)

# excersise with capitals

capitals = {
    "Niemcy": "Berlin",
    "Czechy": "Praga",
    "Słowacja": "Bratysława",
    "Ukraina": "Kijów",
    "Białoruś": "Mińsk",
    "Litwa": "Wilno",
    "Rosja": "Moskwa"
}

for country in capitals:
    print(f"{country:<10}\t{capitals[country]}")

# Lista składana

numbers = [1, 3, 5, 11, 20]
squares = []
for number in numbers:
    squares.append(number * number)
print(f"Na wstępie mieliśmy taką listę {numbers}")
print(f"A oto jej kwadraty {squares}")

squares = [number * number for number in numbers]
print(f"Te kwadraty {squares} uzyskano dzięki list comprehension")

doubles = [number + number for number in numbers]
print(f"Te duble {doubles} uzyskano dzięki list comprehension")

# filtrowanie w liście składanej
numbers = [1, 2, 0, 3, 0, 0, 0]
squares = []
squares = [number * number for number in numbers if number > 0]
print(squares)
print("Kwadraty poza zerami")
# ćwiczenie lista
fil_list = ['Arystoteles','Platon','Sokrates']
name_length = [len(fil) for fil in fil_list]
print(name_length)