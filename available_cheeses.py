available_cheese = ""
if available_cheese == 'edam':
    print("Kupuję edam")

available_cheeses = ("Roquefort","Stilton","Brie","Gouda","Edam","Parmezan"
                     ,"Mozzarella","Czechosłowacki ser z owczego mleka","Listek miętowy")
check_item = "Roquefort"
if available_cheeses.__contains__(check_item):
    print(f"Kupuje {check_item}")
else:
    print("Nie ma takiego artykułu")
