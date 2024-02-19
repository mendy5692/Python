class Bartender():
    def __init__(self, name, alcohol_percentage, price, component):
        self.name = name
        self.alcohol_percentage = alcohol_percentage
        self.price = price
        self.component = component


    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_alcohol_percentage(self):
        return self.alcohol_percentage

    def set_alcohol_percentage(self, alcohol_percentage):
        if 0 <= alcohol_percentage <= 100:
            self.alcohol_percentage = alcohol_percentage
        else:
            raise ValueError("alcohol percentage must be a positive number and lass then 100 percentage.")

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_component(self):
        return self.component

    def set_component(self, component):
        self.component = component

    def get_drink(self):
        print(f"drink details:\n"
              f"\tname: {self.get_name()}."
              f"\talcohol percentage: {self.get_alcohol_percentage()}."
              f"\tprice: {self.get_price()}."
              f"\tcomponent:\n\t\t{self.get_component()}")

def stronger_drink(drink_a, drink_b):
    if drink_a.get_alcohol_percentage() > drink_b.get_alcohol_percentage():
        print(f"{drink_a.get_name} is stronger.")
    elif drink_a.get_alcohol_percentage() == drink_b.get_alcohol_percentage():
        print(f"{drink_a.get_name} and {drink_b.get_name} is the same strongst.")
    else:
        print(f"{drink_b.get_name} is stronger.")

def price_increase_for_alcohol_free(drink):
    if drink.get_alcohol_percentage() == 0:
        drink.set_price(drink.get_price() * 1.05)

def show_components(drink):
    for i in drink.get_component().split(","):
        print(i)


bladi_mary = Bartender("Bladi Mary", 40, 53, "vodka,lemon juice,Tomato juice,sugar water,Tabasco,Salt,pepper,Celery blossom,Lemon wedge")
aperol_spritz = Bartender("Aperol Spritz", 0, 100, "Aperol,Prosecco,soda,Orange wheel")

show_components(aperol_spritz)
