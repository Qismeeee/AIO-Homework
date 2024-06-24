class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    # The describe method is overridden in the Student, Teacher, and Doctor classes.
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        return f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}"

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        return f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}"

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}"

class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob)

    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def compute_average(self):
        teachers = [person for person in self.people if isinstance(person, Teacher)]
        if teachers:
            return sum(teacher.yob for teacher in teachers) / len(teachers)
        return None

    def describe(self):
        for person in self.people:
            print(person.describe())

# Example usage
student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")

print(student1.describe())
print(teacher1.describe())
print(doctor1.describe())

teacher2 = Teacher(name="teacherB", yob=1955, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

ward = Ward(name="Ward 1")
ward.add_person(student1)
ward.add_person(teacher1)
ward.add_person(doctor1)
ward.add_person(teacher2)
ward.add_person(doctor2)

ward.describe()

ward.sort_age()
print("\nSorted by age:")
ward.describe()

print("\nNumber of doctors:", ward.count_doctor())
print("Average year of birth of teachers:", ward.compute_average())
