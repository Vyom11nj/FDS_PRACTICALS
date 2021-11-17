def sum_of_list(l):
    sum = 0
    for i in l:
        if i == -1:
            continue
        sum = sum + i
    return sum

def find_highest(l):
    highest = -1
    for i in l:
        if i > highest:
            highest = i
    return highest

def find_lowest(l):
    lowest = 999
    for i in l:
        if i < lowest:
            if i == -1:
                continue
            lowest = i
    return lowest

def count_frequency(l, mark):
    count = 0
    for i in l:
        if i == mark:
            count = count + 1
    return count

def find_highest_frequency(marks):
    frequency = 0
    highest_frequency = 0
    for i in marks:
        count = count_frequency(marks, i)
        if count > frequency:
            highest_frequency = i
            frequency = count
    return highest_frequency

if __name__ == "__main__":
    marks = []
    for i in range(int(input("Total number of students: "))):
        mark = int(input(f"Score of student no {i + 1} in subject: "))
        marks.append(mark)

    print(f"maximum marks: {find_highest(marks)}")
    print(f"minimum marks: {find_lowest(marks)}")
    print(f"Average marks: {sum_of_list(marks) / (len(marks) - count_frequency(marks, -999))}")
    print(f"Absent students: {count_frequency(marks, -1)}")