convert = input ("What would you like to convert? \n A. C-F \n B. F-C \n Select option A or B: ")

if convert == 'a' or 'A':
    celcius = input ("Temperature? (C): ")
    cel_to_float = float(celcius)

    temp = ((cel_to_float * 9 / 5) + 32)
    temp_to_str = str(temp)

    print(temp_to_str + "°F")
elif convert == 'b' or 'B':
    farenheit = input ("Temperature? (F): ")
    far_to_float = float(farenheit)

    temp = ((far_to_float - 32) * 5 / 9)
    temp_to_str = str(temp)

    print(temp_to_str + "°C")
else:
    print("Error 100: Please select option A or B")
