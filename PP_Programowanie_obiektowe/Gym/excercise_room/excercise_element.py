class WorkoutElement:
    def __init__(self, excercise, number_of_series):
        self.excercise = excercise
        self.number_of_series = number_of_series

    def calculate_time(self):
        return self.excercise.excercise_time * self.number_of_series

    def __str__(self):
        if self.number_of_series == 1:
            return f"{self.excercise} x {self.number_of_series} seria"
        elif self.number_of_series > 1 and self.number_of_series < 5:
            return f"{self.excercise} x {self.number_of_series} serie"
        elif self.number_of_series > 4:
            return f"{self.excercise} x {self.number_of_series} serii"
