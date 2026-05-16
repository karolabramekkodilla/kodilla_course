# Zadanie 1
# Użyj listy składanej, aby stworzyć listę sześcianów (potęgi trzeciej) liczb z zakresu od 1 do 10. 
# Następnie użyj pętli for in, aby zwrócić w konsoli liczby niepodzielne przez 2.

ten_list = [i**3 for i in range(1,11) if i % 2 != 0]
print(ten_list)

# Zadanie 2
# Dana jest lista: [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]. Zadeklaruj ją w Pythonie, a następnie użyj slicingu, 
# by otrzymać listę, która zawiera tylko zera z tej kolekcji. Potem użyj tej samej techniki do zwrócenia listy, 
# która zawiera wszystkie inne liczby tylko nie zera z tej kolekcji.

task_list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
zeros_list = task_list[1:4]+task_list[5:10]+task_list[-2:]
non_zero_list = task_list[0:1]+task_list[4:5]+task_list[-4:-2]
# Całkiem spoko ćwiczenie bo wyszły tutaj problemy z ostatnim elementem listy, z tym jak działa slicing przy ujemnym indeksowaniu,
#  i co właściwie zwraca np. task_list[0] :)
print(zeros_list)
print(non_zero_list)