# Basic Temp Converter v.1.0.0

def question():
    global convert
    convert = input ("What would you like to convert? \n A. Celcius-Farenheit \n B. Farenheit-Celcius \n Select option A or B: ")
question()


def celcius():
    celcius = input ("Temperature? (°C): ")
    cel_to_float = float(celcius)
    temp  = ((cel_to_float * 9 / 5) + 32)
    temp_to_str = str(temp)
    print(celcius + "°C is " + temp_to_str + "°F")


def farenheit():
    farenheit = input ("Temperature? (°F): ")
    far_to_float = float(farenheit)
    temp = ((far_to_float - 32) * 5 / 9)
    temp_to_str = str(temp)
    print(farenheit + "°F is " + temp_to_str + "°C")

if convert == 'a':
    celcius()
elif convert == 'A':
    celcius()
elif convert == 'b':
    farenheit()
elif convert == 'B':
    farenheit()
else:
    print("Error, please select either option A or B")

