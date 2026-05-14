direction_list = ["Pn","Pd"]
direction_list.append("Wsch")
print(direction_list)
direction_list.append("Zach")
print(direction_list)
del direction_list[0:2]
print(direction_list)
direction_list.remove("Zach")
print(direction_list)

# lista 
my_list = [3,6,17,4,0,-20,20,100]
print(my_list)
my_list.sort()
print(my_list)
my_list = my_list.sort()
print(my_list)

my_list = [3,6,17,4,0,-20,20,100]
my_list = sorted(my_list)
print(my_list)

# update cwiczenie
my_set = {'pon', 'wto', 'sro', 'pia', 'sob', 'nie'}
my_set.update({"czw"})
print(my_set)
# 
salads = {
    "owocowa": ["ananas", "truskawka", "jagody"],
    "moja_buraczana": ["buraki", "ser kozi", "rukola"],
    "mamina": ["groszek", "kukurydza", "majonez", "ziemniaki"]
}

print(salads["owocowa"])