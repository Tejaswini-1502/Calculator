
from art import logo

#add
def add(n1,n2):
  return n1+n2

#subtract
def sub(n1,n2):
  return n1-n2

#multiply
def mul(n1,n2):
  return n1*n2

#divide
def div(n1,n2):
  return n1/n2

operations ={
  '+': add,
  '-': sub,
  '*': mul,
  '/': div,
}

def calculator():
  print(logo)
  cont_calc = True
  num1 = float(input("What's the first number?: "))
  
  for key in operations:
    print(key)
  
  while cont_calc:
    selected_op = input("Select the operation you want to perform: ")
    num2 = float(input("What's the next number?: "))
    calc_func = operations[selected_op]
    answer = calc_func(num1,num2)
    print(f"{num1} {selected_op} {num2} = {answer}")
    inp = input(f"Type:\n'y': to continue calculating with {answer}\n'n': to start a new calculation\n'e': to exit\n")
    if inp=='y':
      num1 = answer
    elif inp=='n':
      cont_calc = False
      calculator()
    else:
      cont_calc = False

calculator()