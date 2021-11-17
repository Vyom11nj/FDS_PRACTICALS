students = []
a = int(input("Enter total number of students: "))
for i in range(a):
    print("Enter name of student", i)
    num = input()
    students.append(num)

cricket = []
b = int(input("Enter total number of students who play cricket: "))
for i in range(b):
    print("enter name of student who play's cricket", i)
    num1 = input()
    cricket.append(num1)

badminton = []
c = int(input("Enter total number of students who play badminton: "))
for i in range(c):
    print("enter name of student who play's badminton", i)
    num2 = input()
    badminton.append(num2)

football = []
d = int(input("Enter total number of students who play football: "))
for i in range(d):
    print("enter name of student who play's football", i)
    num3 = input()
    football.append(num3)

cricket.sort()
badminton.sort()
football.sort()

print("\nlist of students who play cricket:", cricket)
print("list of students who play badminton:", badminton)
print("list of students who play football:", football)

# BOTH CRICKET AND BADMINTON
cnb = []
for i in cricket:
    for j in badminton:
        if i == j:
            cnb.append(i)

print(f"\nList of students who play both cricket and badmintion are: {cnb}")

# EITHR CRICKET OR BADMINTON BUT NOT BOTH
cub = []
cub = []
for i in cricket:
    cub.append(i)

for i in badminton:
    for j in cub:
        if i != j:
            cub.append(i)
            break

for i in cub:
    p = cub.count(i)
    if p > 1:
        cub.remove(i)
        cub.remove(i)

cub.sort()
print(f"List of students who play either cricket or badminton but not both:{cub}")

# NEITHER CRICKET NOR BADMINTON

ncnb = []
for i in football:
    ncnb.append(i)

a = []
for k in football:
    for l in cub:
        if l == k:
            a.append(l)
for v in a:
    ncnb.remove(v)

count1 = 0
t = 0
for i in ncnb:
    if t == 0:
        count1 += 1
print(f"Number of students who play neither cricket nor badminton are:{count1}")

# CRICKET AND FOOTBALL BUT NOT BADMINTON

cnf = []
for i in cricket:
    for j in football:
        if i == j:
            cnf.append(i)

for m in cnf:
    for n in badminton:
        if m == n:
            cnf.remove(m)

count = 0
for d in cnf:
    if 1 > 0:
        count += 1
print(f"Number of students who play cricket and football but not badminton are:{count}")

