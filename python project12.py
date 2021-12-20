#linear search
a=[]
noofstud=int(input("Enter the number of students "))
for i in range(0,noofstud):
  a.append(int(input("Enter the roll numbers ")))
print(a)
lsearch=int(input("Enter the roll number to be searched "))
count=0
for i in range(noofstud):
  if(a[i]==lsearch):
    count=1
    break
  else:
    count=0
if(count==1):
  print(f"Roll number found at position {i}")
else:
  print("Not found")

#sentinel search
b=[]
noofstud=int(input("Enter the number of students "))
for i in range(0,noofstud):
  b.append(int(input("Enter the roll numbers ")))
print(b)
ssearch=int(input("Enter the roll number to be searched "))
if (ssearch==b[noofstud-1]):
  print(f"found at position {noofstud-1}")
else:
  b[noofstud-1]=ssearch
  print(b)
  for i in range(0,len(b)-2):
    if(i==b[noofstud-1]):
      print(f"Found at position {i}")

#Binary search
def Binarysearch(c,bsearch):
  first=0
  last=noofstud-1
  mid=0
  while first<=last:
    middle=((first+(last))//2)
    if bsearch not in c:
      return -1
    elif(c[middle]==bsearch):
      return middle
    elif(c[middle]<bsearch):
      first=middle
    elif(c[middle]>bsearch):
      last=middle
    if bsearch not in c:
      return -1
c=[]
noofstud=int(input("Enter the number of students "))
for i in range(0,noofstud):
  c.append(int(input("Enter the roll numbers in sorted order ")))
print(c)
bsearch=int(input("Enter the roll number to be searched "))



a=Binarysearch(c,bsearch)
if a==-1:
  print("Not found")
else:
  print(f"{bsearch} is present at {a}")

