class Auto:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

    def show_auto(self):
        return f"Автомобиль: {self.mark} {self.model}, Год выпуска: {self.year}"


car = Auto("Toyota", "Camry", 2022)
print(car.show_auto())
