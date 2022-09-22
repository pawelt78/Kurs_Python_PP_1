import velocity_calculation


distance = float(input("Hello, tell me your distance in kilometers: "))
time = float(input("And now, tell me your time in hours: "))

velocity = velocity_calculation.f_velocity_calculation(distance, time)

print("")
print("Your average velocity: ", velocity, " km/h")
