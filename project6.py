bal = 0
opr = input("d for deposit, w for withdraw\nwhich operation do ou want to perform?")
if opr == "d":
  d=int(input("enter the amount you want to deposit: "))
  bal +=d
  print(f"acount balance after depositing {d}={bal}")
elif opr == "w":
  w=int(input("enter the amount you want to withdraw: "))
  if w>=bal:
    bal-=w
    print(f"account balance after withdrawing {w}={bal}")
  else:
    print("invalid input")