tempt = eval(input("Enter temperature in Celsius: "))
if tempt < -273.15:
    print("the temperature is invalid because it is below absolute zero")
elif tempt == -273.15:
    print("the temperature is absolute 0")
elif -273.15 < tempt < 0:
    print("the temperature is below freezing")
elif tempt == 0:
    print("the temperature is at the freezing point")
elif 0 < tempt < 100:
    print("the temperature is in the normal range")
elif tempt == 100:
    print("the temperature is at the boiling point.")
elif tempt > 100:
    print("the temperature is above the boiling point")

