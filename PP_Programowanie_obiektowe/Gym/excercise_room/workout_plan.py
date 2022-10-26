import random
from PP_Programowanie_obiektowe.Gym.excercise_room.excercise import Excercise
from PP_Programowanie_obiektowe.Gym.excercise_room.excercise_element import WorkoutElement

class WorkoutPlan:
    def __init__(self, first_name, last_name, workout_elements=None):
        self.first_name = first_name
        self.last_name = last_name
        if workout_elements is None:
            workout_elements = []
        self.workout_elements = workout_elements
        self.total_time = self.calculate_total_time()

    def calculate_total_time(self):
        total_time = 0
        for element in self.workout_elements:
            total_time += element.calculate_time()
        return total_time

    def __str__(self):
        mark_line = "-" * 20
        order_details = f"Trening przygotowany dla: {self.first_name} {self.last_name}"
        value_details = f"O łącznej długości: {(self.total_time/60):,.2f} min "
        product_details = "Przygotowane ćwiczenia:\n"
        for element in self.workout_elements:
            product_details += f"\t{element}\n"

        result = "\n".join([mark_line, order_details, value_details, product_details, mark_line])
        return result

    @classmethod
    def generate_workout(cls, number_of_excercises):
        workout_elements = []
        for excercise_number in range(number_of_excercises):
            excercise_name = f"Cwiczenie-{excercise_number+1}"
            excercise_weight = random.randint(1, 100)
            excercise_time = random.randint(30, 120)
            excercise = Excercise(excercise_name, excercise_weight, excercise_time)
            number_of_series = random.randint(1, 4)
            workout_elements.append(WorkoutElement(excercise, number_of_series))

        workout_plan = WorkoutPlan(first_name="Paweł", last_name="Tatar", workout_elements= workout_elements)
        return workout_plan
