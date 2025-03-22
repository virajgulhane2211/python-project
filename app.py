n1==int(input('Enter 1st No'))
n2=int(input('Enter 2nd No'))
try:
  div=n1/n2
  print(div)
except ZeroDivisionError:
  print('We cant divide by zero')
finally:
  print('Thanks for using our Application')
  while True:
    n1=int(input('Enter 1st No'))
    n2=int(input('Enter 2nd No'))
    try:
      div=n1/n2
      print(div)
    except ZeroDivisionError:
      print('We cant divide by zero')
    finally:
      print('Thanks for using our Application')
print('Thanks')
