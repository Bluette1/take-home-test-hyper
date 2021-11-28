'''
Please develop a calculator that meets the following requirements:
● We expect the calculator to evaluate the following expressions. You can use
the examples of input -> output for testing.
○ Value, e.g. “3.2” -> “3.2”
○ Factorial, e.g. “factorial 5” -> “120”
○ Highest prime number under a given value, e.g. “prime 10” -> “7”
○ Highest Fibonacci number under a given value, e.g. “fibonacci 12” ->
“8”
○ Addition, e.g. “+ 12.5 12.5” -> “25”
○ Subtraction, e.g. “- 43.7 50” -> “-6.3”
○ Multiplication, e.g. “* 6 -12” -> “-72”
○ Division, e.g. “/ 20 10” -> “2”
○ Long arithmetic expressions, e.g. “+ 2 3 4 10” -> “19”
○ Nested expressions where parentheses surround subexpressions,
e.g. “/ (factorial (* 2 2 5)) 600” -> “12096”
○ Expressions with contiguous whitespace, e.g. “\t 3.22 “ -> “3.22”
● The input is a string and the output is a string.
● Operators prefix their operands in expressions.
● It handles integers, floating-point numbers and negative numbers.
● It removes the fractional part of the result if the said fractional part is
equivalent to 0, e.g. 4.0 becomes 4.
● It gracefully handles overflows.
'''
def string_calc(expression):
  
  # Retrieve the operator and numbers
  expression_arr = expression.split(' ')
  if len(expression_arr) == 1: 
    return expression_arr[0]
  op_stack = []
  value_stack = []
  
  last_index = -1
  
  result = expression
  
  for idx in range(len(expression)):
    if expression[idx] == '(':
      op_stack.append(idx)
    elif expression[idx] == ')' and len(op_stack) > 0:
      # evaluate expression
      start = op_stack.pop()
      space_idx = expression[start + 1: ].index(' ')
      if (len(value_stack) == 0):
        value = calculate(expression[start + 1: start + 1 + space_idx], expression[start + 1 + space_idx + 1:idx].split(' '))
        value_stack.append(value)
        last_index = idx
      else:
        statement = [value_stack.pop()] + expression[last_index + space_idx + 1:idx].split(' ')
        value = calculate(expression[start + 1: start + 1 + space_idx], statement)
        value_stack.append(value)
        last_index = idx

      while(len(op_stack) > 0 and expression[last_index + 1] == ')'):
        last_index += 1
        start = op_stack.pop()
        space_idx = expression[start + 1: ].index(' ')
        print('value: ', value)
        value = calculate(expression[start + 1: start + 1 + space_idx], [value])
      result = result[0:start] + value + expression[last_index + 1:]

  result = result.split(' ')
  if len(result) == 1: 
    return result[0]
  else:
    return calculate(result[0], result[1:])
  
def calculate(operator, expression):  
  if operator == 'factorial':
    return str(factorial(int(expression[0])))
  elif operator == 'fibonacci':
    return str(fibonacci(int(expression[0])))
  elif operator == '+':
    return str(add(expression))
  elif operator == '-':
    return str(subtract(expression))
  elif operator == '*':
      return str(multiply(expression))
  elif operator == '/':
    return str(divide(expression))
  elif operator == '\t':
    return str(remove_whitespace(expression[0]))

def factorial(num):
  fact = 1
  for i in range(1, num + 1):
    fact *= i
  return fact

def fibonacci(num):
  past = prev = 1
  while prev < num:
    curr = past + prev
    past = prev
    prev = curr
    
  return past
    
def add(numbers):
  sum = 0
  # Keep track of the highest number of decimal places
  n_decimal_places = 0 
  for i in range(len(numbers)):
    n_decimal_places = max(n_decimal_places, decimal_places(numbers[i]))
    sum += number(numbers[i])
  return truncate(sum, n_decimal_places)

def subtract(numbers):
  # Get the highest number of decimal places
  n_decimal_places = max(decimal_places(numbers[0]), decimal_places(numbers[1]))
  diff = number(numbers[0]) - number(numbers[1])
  return truncate(diff, n_decimal_places)

def divide(numbers):
  # Get the highest number of decimal places
  n_decimal_places = max(decimal_places(numbers[0]), decimal_places(numbers[1]))
  quotient = number(numbers[0]) / number(numbers[1])
  return truncate(quotient, n_decimal_places + 1)

def multiply(numbers):
  product = 1
  # Keep track of the number of decimal places
  n_decimal_places = 0 
  for i in range(len(numbers)):
    n_decimal_places += decimal_places(numbers[i])
    
    product *= number(numbers[i])
  return truncate(product, n_decimal_places)

def remove_whitespace(num):
  return num.strip()


def truncate(num, decimal_places):
  if (int(num) == num):
    return int(num)
  return round(num, decimal_places)

def number(num):
  try:
    return int(num)
  except:
    return float(num)
  
def decimal_places(num):
  parts = num.split(".")
  if len(parts) == 1:
    return 0
  return len(parts[1])
  
print(string_calc('3.2'))
print(string_calc('factorial 5'))
print(string_calc('fibonacci 12'))
print(string_calc('+ 12.5 12.6'))
print(string_calc('+ 3.22 3.22'))
print(string_calc('+ 3.22239 3.22239'))
print(string_calc('+ 3.22235 3.22235'))
print(string_calc('- 43.7 50'))
print(string_calc('* 6 -12'))
print(string_calc('* 6 12'))
print(string_calc('* 0.1 0.1'))
print(string_calc('* -0.1 -0.1'))
print(string_calc('* 0.1 -0.1'))
print(string_calc('* -0.1 0.1'))
print(string_calc('/ 20 10'))
print(string_calc('/ 5 2'))
print(string_calc('/ 0.5 2'))
print(string_calc('/ 0.05 2'))
print(string_calc('/ 0.05 0.02'))
print(string_calc('/ 0.5 0.2'))
print(string_calc('/ 0.05 0.2'))
print(string_calc('/ 2 10'))
print(string_calc('\t 3.22  '))
print(string_calc('/ (factorial (* 2 2 5)) 600'))
print(string_calc('* (* 2 2 5) 4'))
print(string_calc('* (* 2 2 5) 4 3 2'))
print(string_calc('/ (* (* 2 2 5) 4 3 2) 3'))
print(string_calc('* (/ (* (* 2 2 5) 4 3 2) 3) 5'))
print(string_calc('* (/ (* (* 2 2 5) 4 3 2) 3) 5 10 2'))
print(string_calc('/ (* (/ (* (* 2 2 5) 4 3 2) 3) 5 10 2) 2'))