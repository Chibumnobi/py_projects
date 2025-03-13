6
print("Welcome to Nobi's Calculator")
num1 = float(input('Pls enter a number '))
n = True
while n == True:
  num2 = float(input('The second number '))
  def add(num1, num2):
    print(f'{num1} + {num2} = {num1 + num2}')
  def subtract(num1, num2):
    print(f'{num1} - {num2} = {num1 - num2}')
  def multiply(num1, num2):
    print(f'{num1} x {num2} = {num1 * num2}')
  def divide(num1, num2):
    print(f'{num1} ÷ {num2} = {num1 / num2}')
  operator = int(input('''What operator do you want to use?
  Press 1 for add
  Press 2 for subtract
  Press 3 for multiply
  Press 4 for divide '''))
  if operator == 1 :
    add(num1, num2)
    output = num1 + num2
  elif operator == 2 :
    subtract(num1, num2)
    output = num1 - num2
  elif operator == 3 :
    multiply(num1, num2)
    output = num1 * num2
  elif operator == 4 :
    divide(num1, num2)
    output = num1 / num2
  leave = int(input('''Do you want to do another calculation?
  press 1 for yes or 2 for no'''))
  if leave == 2 :
    print('Thanks for using Nobi\'s Calculator')
    n = False
  elif leave == 1:
    w = int(input('With your output or refresh press 1 for with output or 2 for refresh'))
    if w == 1:
      num1 = output
      n = True
    elif w == 2:
      num1 = float(input('Pls enter a number '))
      n = True