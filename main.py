from collections import Counter

class Student:
    def __init__(self, data):
        self.data = data.split()

    def detail(self):
        return self.data
        # print(self.data)
    
    def student_name(self):
        name = self.data[0] + ', ' + self.data[1]
        return name

    def cla(self):
        return self.data[2]

    def ola(self):
        return self.data[3]

    def test1(self):
        return self.data[4]

    def test2(self):
        return self.data[5]

    def final(self):
        return self.data[6]

    def average(self):

        record = self.data
        count = 0
        summ = 0
        for i in range(2, len(record)):
            summ += int(record[i])
            count += 1
        self.avg = summ/count
        return self.avg
        # print(avg)

    def grade(self):
        if self.average() >= 90:
            return 'A'
        elif self.average() >= 80:
            return 'B'
        elif self.average() >= 70:
            return 'C'
        elif self.average() >= 60:
            return 'D'
        elif self.average() < 60:
            return 'F'
        else:
            return 'No grade for this score'


class Roster:
    def __init__(self):
        self.student = []
        self.grades = []

    def add_student(self, student):
        self.student.append(student)
        self.grades.append(student.grade())

    def details(self):
        print("==============================================================")
        print(" Student Name   CLA  OLA  test1  test2  Final  Average  Grade")
        print("==============================================================")
        students = self.student
        for ix in students:
            print(f"{ix.student_name()}      {ix.cla()}     {ix.ola()}     {ix.test1()}   " +
                  f"{ix.test2()}     {ix.final()}     {ix.average()}     {ix.grade()}")

    def num_of_students_per_grade(self):
        num_students = Counter(sorted(self.grades))
        print("============================")
        print("  GRADE    NUM OF STUDENTS  ")
        print("============================")
        for keys, vals in num_students.items():
            print(f"   {keys}         {vals}")
        print("============================")
        # for ix in self.student:
        #     if ix.grade() is 'A':


def main():
    
    user_input = input("Pls input name of file: ")
    roster = Roster()
    with open(user_input) as f:
        # line = f.readline()
        for line in f:
            student = Student(line)
            # print(student.average())
            # print(student.grade())
            # print(student.detail())
            # roster = Roster()
            roster.add_student(student)
            # roster.details()
            # print(line)
        roster.details()
        roster.num_of_students_per_grade()
    # while line:
    #     line = f.readline()
    #     print(line)

if __name__ == '__main__':
    main()