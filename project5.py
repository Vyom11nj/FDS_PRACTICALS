name = input("Enter your name: ")
post = input("Enter your post: ")
day = int(input("How many days were you present? : "))

x = input("did you do work overtime?: Yes/No")

if x=="yes":
  ovr = int(input("how many days did you work overtime? : "))

if day<=31:
  if post =="manager":
    M = (day + ovr / 2) * 2000
    print(f"your salary for this month is: {M}")

  if post =="team leader":
    T = (day + ovr / 2) * 1800
    print(f"your salary for this month is: {T}")

  if post =="employee":
    E = (day + ovr / 2) * 1500
    print(f"your salary for this month is: {E}")

else:
  print("N\A")