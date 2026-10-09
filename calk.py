num1=int(input())
op=input()
num2=int(input())
if op=="+":
  print(num1+num2)
elif op=="-":
  print(num1-num2)
elif op=="*":
  print(num1*num2)
elif op=="/":
  if num2!=0:
    print(int(num1/num2))
  else:
    print("Ошибка: деление на ноль!")
else:
    print("Ошибка: неверная операция!")