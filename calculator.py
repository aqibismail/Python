n1 = input ("Number 1: ")
o = input ("Select Operator: \n A. + \n B. - \n C. * \n D. / \n Operator: ")
n2 = input ("Number 2: ")

num1 = float(n1)
num2 = float(n2)

def plus():
    print(num1 + num2)

def minus():
    print(num1 - num2)

def times():
    print(num1 * num2)

def divide():
    print(num1 / num2)

if o == 'A':
    plus()
elif o == 'B':
    minus()
elif o == 'C':
    times()
elif o == 'D':
    divide()
else:
    print('Unknown error, please try again.')