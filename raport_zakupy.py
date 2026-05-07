item_1 = "Roquefort"
price_1 = 12.5
item_2 = "Stilton"
price_2 = 11.24
item_3 = "Brie"
price_3 = 9.30
item_4 = "Gouda"
price_4 = 8.55
item_5 = "Edam"
price_5 = 11
item_6 = "Parmezan"
price_6 = 11
item_7 = "Mozzarella"
price_7 = 14
item_8 = "Czechosłowacki ser z owczego mleka"
price_8 = 122.32
total = price_1 + price_2 + price_3 + price_4 + price_5 + price_6 + price_7 + price_8
print (f"====================================================")
print (f"===================Lista zakupów====================")
print (f"{'Towar':<40}{'Cena':>8}")
print (f"{item_1:<40}{price_1:>8.2f} zł")
print (f"{item_2:<40}{price_2:>8.2f} zł")
print (f"{item_3:<40}{price_3:>8.2f} zł")
print (f"{item_4:<40}{price_4:>8.2f} zł")
print (f"{item_5:<40}{price_5:>8.2f} zł")
print (f"{item_6:<40}{price_6:>8.2f} zł")
print (f"{item_7:<40}{price_7:>8.2f} zł")
print (f"{item_8:<40}{price_8:>8.2f} zł")
print (f"====================================================")
print (f"===================Podsumowanie=====================")
print (f"{'':<40}{'Suma':>8}")
print (f"{'':<40}{total:>8.2f} zł")


