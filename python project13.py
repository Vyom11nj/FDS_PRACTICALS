#bubble sort
numofstud=int(input("Enter the number of students "))
perc=[]
for i in range(0,numofstud):
  perc.append(int(input("Enter the percentages of students ")))
print(perc)

#sort
for i in range(0,numofstud-1):
  for j in range(0,numofstud-1):
    if perc[j]>perc[j+1]:
      perc[j+1],perc[j]=perc[j],perc[j+1]
    else:
      continue
print(perc)
for i in range(numofstud-1,numofstud-6,-1):
  print(perc[i])

#selection sort
numofstud1=int(input("Enter the number of students "))
perce=[]
for i in range(0,numofstud1):
  perce.append(int(input("Enter the percentages of students ")))
print(perce)
#selection sort
for i in range(numofstud1-1):
  min=perce[i]
  for j in range(i+1,numofstud1):
    if perce[j]<min:
      min=perce[j]
      perce[i],perce[j]=perce[j],perce[i]

print(perce)

#insert sort
def Insertionsort(perce):
    for i in range(1, len(perce)):
        temp = perce[i]
        j = i - 1
        while j > 0 and temp < perce[j]:
            perce[j + 1] = perce[j]
            j = j - 1
        perce[j + 1] = temp

numofstud1=int(input("Enter the number of students "))
perce=[]
for i in range(0,numofstud1):
  perce.append(int(input("Enter the percentages of students ")))
print(perce)
Insertionsort(perce)
print(perce)


# merge sort

def merge(arr):
    if len(arr) > 1:
        mid = (len(arr)) // 2
        lower = arr[:mid]
        upper = arr[mid:]
        print(lower)
        print(upper)
        merge(lower)
        merge(upper)

        i, j, k = 0, 0, 0
        while i < len(lower) and j < len(upper):
            print(lower)
            if lower[i] < upper[j]:
                arr[k] = lower[i]
                i = i + 1
            else:
                arr[k] = upper[j]
                j = j + 1
            k = k + 1

        while j < len(upper):
            arr[k] = upper[j]
            j = j + 1
            k = k + 1
            print(arr)

        while i < len(lower):
            arr[k] = lower[i]
            i = i + 1
            k = k + 1
            print(arr)

        return arr


num = int(input("Enter the number of entries "))
arr = []
for i in range(num):
    a = int(input("Enter the numbers "))
    arr.append(a)
newlist = merge(arr)
print(newlist)