marksinsub=[]

numberofstudents=int(input("Enter total number of students : "))

for i in range(numberofstudents):
   marks=int(input("Enter marks of student "+str(i+1)+" : "))
   marksinsub.append(marks)

def average(marks):
    sum=0
    count=0
    for i in range(len(marks)):
        sum+=marks[i]
        count+=1
    average=sum/count
    print("Total marks :", sum)
    print("Average marks :", average)
average(marksinsub)
