import calculations.money_calculation

#def ask_for_int_value(message):
#    input_value = input(message)
#    return int(input_value)

#initial_value = ask_for_int_value("Podaj ile wpłaciłeś na lokatę?: ")
#percentage = ask_for_int_value("Jakie jest oprocentowanie (%) ? ")
#years = ask_for_int_value("Ile lat trwa lokata ? ")




start_value = float(input("Podaj ile wpłaciłeś na lokatę?: "))
percentage = float(input("Na jaki procent jest lokata?: "))
duration = int(input("Na ile lat jest lokata?:"))

finish_value = calculations.money_calculation.locate_calculation(start_value, percentage, duration)

print(f"Końcowa kwota Twojej lokaty to {finish_value:.2f} zł")