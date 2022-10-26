#analogiczny przykład jak podczas kursu

from PP_Programowanie_obiektowe.Gym.excercise_room.workout_plan import WorkoutPlan


def run_program():
    first_workout = WorkoutPlan.generate_workout(9)
    print(first_workout)
    # second_workout = WorkoutPlan.generate_workout(10)
    # print(second_workout)



if __name__ == '__main__':
    run_program()
