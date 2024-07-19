# Example Python script demonstrating basic concepts using classes and functions

# Define a simple function
def greet(name):
    return f"Hello, {name}!"

# Define a class with methods and attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
    
    def birthday(self):
        self.age += 1
        return f"Happy Birthday {self.name}! You are now {self.age} years old."

# Define another class to demonstrate inheritance
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

# Define a function to demonstrate file handling
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    return f"Content written to {filename}"

# Define a function to demonstrate reading from a file
def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Define a function to demonstrate exception handling
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"

# Main function to demonstrate the usage of the above classes and functions
def main():
    # Greeting
    print(greet("Alice"))
    
    # Person instance
    person = Person("John", 30)
    print(person.introduce())
    print(person.birthday())
    
    # Student instance
    student = Student("Bob", 20, "S12345")
    print(student.introduce())
    print(student.add_grade(90))
    print(student.add_grade(85))
    print(f"Average Grade: {student.average_grade()}")
    
    # File handling
    content = "This is a test file."
    filename = "test.txt"
    print(write_to_file(filename, content))
    print(read_from_file(filename))
    
    # Exception handling
    print(divide_numbers(10, 2))
    print(divide_numbers(10, 0))

# Call the main function
if __name__ == "__main__":
    main()
