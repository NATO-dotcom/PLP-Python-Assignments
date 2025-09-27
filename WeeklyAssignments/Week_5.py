# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.__battery = 100  # private attribute (encapsulation)

    def call(self, number):
        print(f"sCalling {number} from {self.model}...")

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        print(f"{self.model} charged to {self.__battery}%")

    def get_battery(self):
        return self.__battery  # controlled access to private attribute


# Child class (inheritance)
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model, storage)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"📸 Taking a {self.camera_megapixels}MP photo with {self.model}!")


# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S21", "128GB")
phone2 = SmartphonePro("Apple", "iPhone 15 Pro", "256GB", 48)

# Testing methods
phone1.call("0723456789")
phone1.charge(20)
print("Battery level:", phone1.get_battery())

phone2.take_photo()
phone2.call("0112233445")
