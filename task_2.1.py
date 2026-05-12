class dog():
    def __init__(self,name):
        self.name = name
    
    def hau(self):
        print("hau !!!!")
        return "pies zaszczekał"
Dog = dog("Pluto")

my_list = [1,"mielonka",None,dog,"ok"]

for item in my_list:
    print(item)

my_list = [1,"mielonka",None,Dog,"ok"]

for item in my_list:
    print(item)

my_list = [1,"mielonka",None,Dog.name,"ok"]

for item in my_list:
    print(item)

my_list = [1,"mielonka",None,Dog.hau(),"ok"]

for item in my_list:
    print(item)