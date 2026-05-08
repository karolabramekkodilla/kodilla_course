item_1 = "Roquefort"
price_1 = 12.5
quantity_1 = 2
item_2 = "Stilton"
price_2 = 11.24
quantity_2 = 1
item_3 = "Brie"
price_3 = 9.30
quantity_3 = 1
item_4 = "Gouda"
price_4 = 8.55
quantity_4 = 1
item_5 = "Edam"
price_5 = 11
quantity_5 = 1
item_6 = "Parmezan"
price_6 = 11
quantity_6 = 3.5
item_7 = "Mozzarella"
price_7 = 14
quantity_7 = 0.13
item_8 = "Czechosłowacki ser z owczego mleka"
price_8 = 122.32
quantity_8 = 0.22
item_9 = "Listek miętowy"
price_9 = 20
quantity_9 = 0.2
total = (
    price_1 * quantity_1 +
    price_2 * quantity_2 +
    price_3 * quantity_3 +
    price_4 * quantity_4 +
    price_5 * quantity_5 +
    price_6 * quantity_6 +
    price_7 * quantity_7 +
    price_8 * quantity_8 +
    price_9 * quantity_9
)
print (f'='*85)
print (f"===================================Lista zakupów=====================================")
print (f"{'Artykuł':<40}   \t{'Cena':>6}   *\t{'Ilość'}  =   {'Suma'}")
print (f"{item_1:<40}   \t{price_1:>6.2f}   *\t {quantity_1:.2f}  = {price_1*quantity_1:>6.2f} zł")
print (f"{item_2:<40}   \t{price_2:>6.2f}   *\t {quantity_2:.2f}  = {price_2*quantity_2:>6.2f} zł")
print (f"{item_3:<40}   \t{price_3:>6.2f}   *\t {quantity_3:.2f}  = {price_3*quantity_3:>6.2f} zł")
print (f"{item_4:<40}   \t{price_4:>6.2f}   *\t {quantity_4:.2f}  = {price_4*quantity_4:>6.2f} zł")
print (f"{item_5:<40}   \t{price_5:>6.2f}   *\t {quantity_5:.2f}  = {price_5*quantity_5:>6.2f} zł")
print (f"{item_6:<40}   \t{price_6:>6.2f}   *\t {quantity_6:.2f}  = {price_6*quantity_6:>6.2f} zł")
print (f"{item_7:<40}   \t{price_7:>6.2f}   *\t {quantity_7:.2f}  = {price_7*quantity_7:>6.2f} zł")
print (f"{item_8:<40}   \t{price_8:>6.2f}   *\t {quantity_8:.2f}  = {price_8*quantity_8:>6.2f} zł")
print (f"{item_9:<40}   \t{price_9:>6.2f}   *\t {quantity_9:.2f}  = {price_9*quantity_9:>6.2f} zł")
print (f'='*85)
print (f"====================================Podsumowanie=====================================")
print (f"{'':<75}{'Razem':>6}")
print (f"{'':<75}{total:>6.2f} zł")


