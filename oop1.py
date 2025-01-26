#OOP1
# class Car: #class
#     def __init__(self, brand, model, year): #constructor
#         self.brand = brand #attributes
#         self.model = model #attributes
#         self.year = year #attributes

#     def show_info(self): #method
#         print(f"Brand: {self.brand} \nModel: {self.model} \nYear: {self.year}") #method

# # make object from class Car
# car_one_brand = input("Enter Car One Brand: ")
# car_one_model = input("Enter Car One Model: ")
# car_one_year = int(input("Enter Car One Year: "))

# car_one = Car(car_one_brand, car_one_model, car_one_year) #object from class Car
# print()
# #car_one = Car("Toyota", "Corolla", 2022) #object from class Car
# car_two = Car("Honda", "Civic", 2021) #object from class Car

# # call method show_info
# print("Car One:")
# car_one.show_info() #call method
# print("*****************")
# print("Car Two:")
# car_two.show_info() #call method
#########################################
# class Telephone():
#     def __init__ (self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
    
#     def show_info(self):
#         print(f"Brand: {self.brand} \nModel: {self.model} \nPrice: {self.price}")

# # make object from class Telephone
# apple = Telephone("Apple", "Iphone 12", 1200)
# samsung = Telephone("Samsung", "Galaxy S21", 1000)

# # call method show_info
# print("Apple:")
# apple.show_info() #call method
# print("*****************")
# print("Samsung:")
# samsung.show_info() #call method
#########################################
# class Book():
#     def __init__(self, name, author, price):
#         self.name = name
#         self.author = author
#         self.price = price
    
#     def show_info(self):
#         print(f"Name: {self.name} \nAuthor: {self.author} \nPrice: ${self.price}")
    
#     def discount(self, percent):
#         self.price -= (self.price * percent / 100)
#         print(f"New Price after {percent}% discount: ${self.price}")

# # make object from class Book
# book_one = Book("Python Programming", "John", 100)
# book_two = Book("Java Programming", "Smith", 120)
# try:
#     new_price = float(input("Enter Discount Percent (e.g., 10 for 10%): "))
# except ValueError:
#     print("Invalid input! Please enter a valid number.")
#     new_price = 0  
# # call method show_info
# print("Book One:")
# book_one.show_info() #call method
# print("*****************")
# print("Book Two:")
# book_two.show_info() #call method
# print("*****************")
# print("Book One After Discount:")
# book_one.discount(new_price)
#########################################
# class Student():
#     def __init__(self, name, student_id, grades):
#         self.name = name
#         self.student_id = student_id
#         self. grades = grades
#         self.grades = grades if grades else [] #if grades is empty, then assign an empty list

#     def add_grades(self, grade):
#         self.grades.append(grade)
#         print(f"New Grade Added: {grade}")

#     def calculate_average(self):
#         if self.grades : 
#             average = sum(self.grades) / len(self.grades)
#             return average
#         else:
#             return 0
    
#     def show_info(self):
#         average = self.calculate_average()
#         print(f"{'Name':<10} :{self.name} \n{'Student ID':<10} :{self.student_id} \n{'Grades':<10} :{self.grades} \n{'Average':<10} :{average:.2f}")

# adam = Student("Adam", 123, [90, 80, 70])
# eve = Student("Eve", 124, [85, 75, 65])

# # call method show_info
# print("Student 1:")
# adam.show_info() #call method
# print("*****************")
# print("Student 2:")
# eve.show_info() #call method
# print("*****************")
# print("Adam After Adding New Grade:")
# adam.add_grades(95)
# print("*****************")
# print("Eve After Adding New Grade:")
# eve.add_grades(90)
# print("*****************")
# print("Adam Average:")
# adam.show_info()
# print("*****************")
# print("Eve Average:")
# eve.show_info()
#########################################
