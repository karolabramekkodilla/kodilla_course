item_1 = "roquefort"
price_1 = 12.5
quantity_1 = 2
item_2 = "stilton"
price_2 = 11.24
quantity_2 = 1
item_3 = "brie"
price_3 = 9.30
quantity_3 = 1
item_4 = "gouda"
price_4 = 8.55
quantity_4 = 1
item_5 = "edam"
price_5 = 11
quantity_5 = 1
item_6 = "parmezan"
price_6 = 11
quantity_6 = 3.5
item_7 = "mozzarella"
price_7 = 14
quantity_7 = 0.13
item_8 = "czechosłowacki ser z owczego mleka"
price_8 = 122.32
quantity_8 = 0.22
item_9 = "listek miętowy"
price_9 = 20
quantity_9 = 0.2
total = price_1 + price_2 + price_3 + price_4 + price_5 + price_6 + price_7 + price_8 + price_9
print (f"====================================================")
print (f"===================Lista zakupów====================")
print (f"{'Item':<40}{'Price   *   Quantity  =  Total':>30}")
print (f"{item_1:<40}{price_1:.2f}   *\t{quantity_1:.2f}   = {price_1*quantity_1:>6.2f} zł")
print (f"{item_2:<40}{price_2:>8.2f} zł")
print (f"{item_3:<40}{price_3:>8.2f} zł")
print (f"{item_4:<40}{price_4:>8.2f} zł")
print (f"{item_5:<40}{price_5:>8.2f} zł")
print (f"{item_6:<40}{price_6:>8.2f} zł")
print (f"{item_7:<40}{price_7:>8.2f} zł")
print (f"{item_8:<40}{price_8:>8.2f} zł")
print (f"====================================================")
print (f"===================Podsumowanie=====================")
print (f"{'':<40}{'Total':>8}")
print (f"{'':<40}{total:>8} zł")


