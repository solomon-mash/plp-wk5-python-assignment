class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.__storage = storage  # Encapsulated attribute
        self.battery_life = battery_life
    
    def get_storage(self):
        return self.__storage

    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage = new_storage
        else:
            print("Storage must be positive!")

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self):
        print(f"{self.brand} {self.model} is charging...")

    def __str__(self):
        return f"{self.brand} {self.model} | Storage: {self.__storage}GB | Battery: {self.battery_life}mAh"

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, gpu):
        super().__init__(brand, model, storage, battery_life)
        self.gpu = gpu

    def play_game(self, game_name):
        print(f"{self.brand} {self.model} with {self.gpu} is playing {game_name}!")

    def charge(self):  # Polymorphism: overriding the charge method
        print(f"{self.brand} {self.model} uses fast charging...")

# Implementation
phone1 = Smartphone("Samsung", "Galaxy S21", 128, 4000)
phone2 = GamingSmartphone("Asus", "ROG Phone 5", 256, 6000, "Adreno 660")

print(phone1)
phone1.make_call("2547-456-7890")
phone1.charge()

print("\n" + "-"*30 + "\n")

print(phone2)
phone2.make_call("2547-654-3210")
phone2.play_game("PUBG Mobile")
phone2.charge()
