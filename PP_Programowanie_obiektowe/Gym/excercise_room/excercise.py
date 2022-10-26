class Excercise:
    def __init__(self, name, excercise_weight, excercise_time):
        self.name = name
        self.excercise_weight = excercise_weight
        self.excercise_time = excercise_time

    def __str__(self):
        return f"Nazwa: {self.name} | Obciążenie: {self.excercise_weight} kg | Czas: {self.excercise_time} sek"

