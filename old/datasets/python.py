
def greet(name):
    return f"Hello, {name}!"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
    
    def birthday(self):
        self.age += 1
        return f"Happy Birthday {self.name}! You are now {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
        return f"Grade {grade} added."
    
    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    return f"Content written to {filename}"

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"

def main():
    print(greet("Alice"))
    
    person = Person("John", 30)
    print(person.introduce())
    print(person.birthday())
    
    student = Student("Bob", 20, "S12345")
    print(student.introduce())
    print(student.add_grade(90))
    print(student.add_grade(85))
    print(f"Average Grade: {student.average_grade()}")
    
    content = "This is a test file."
    filename = "test.txt"
    print(write_to_file(filename, content))
    print(read_from_file(filename))
    
    print(divide_numbers(10, 2))
    print(divide_numbers(10, 0))

if __name__ == "__main__":
    main()
