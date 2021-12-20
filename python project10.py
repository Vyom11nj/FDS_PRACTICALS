BUBBLESORT

  l=[]
  n=int(input("enter the no. of element of list="))

  for item in range(n):
    a=int(input(" "))
    l.append(a)

  print('list is: ', l)

  for i in range(len(l)):
    for j in range(i+1 ,len(l)):
      if (l[i]>l[j]):
        temp=l[i]
        l[i]=l[j]
        l[j]=temp

  print("sorted list is:", l)