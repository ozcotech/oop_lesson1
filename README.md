# Object-Oriented Programming (OOP) Examples in Python

This repository contains practical examples of Object-Oriented Programming (OOP) concepts implemented in Python. Each example demonstrates a specific use case of classes, attributes, and methods in Python programming.

## Table of Contents

1. [Car Class](#car-class)
2. [Telephone Class](#telephone-class)
3. [Book Class](#book-class)
4. [Student Class](#student-class)

---

### Car Class

**Description:**
A simple implementation of a `Car` class with attributes such as brand, model, and year. The class also includes a `show_info` method to display car details.

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_info(self):
        print(f"Brand: {self.brand} \nModel: {self.model} \nYear: {self.year}")
```

#### Visual Representation:
```
+---------------------+
|       Car          |
+---------------------+
| - brand: str       |
| - model: str       |
| - year: int        |
+---------------------+
| + show_info()      |
+---------------------+
```

---

### Telephone Class

**Description:**
A `Telephone` class that demonstrates the use of attributes for storing brand, model, and price. It also includes a method to display telephone details.

```python
class Telephone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_info(self):
        print(f"Brand: {self.brand} \nModel: {self.model} \nPrice: {self.price}")
```

#### Visual Representation:
```
+-----------------------+
|      Telephone       |
+-----------------------+
| - brand: str         |
| - model: str         |
| - price: float       |
+-----------------------+
| + show_info()        |
+-----------------------+
```

---

### Book Class

**Description:**
A `Book` class with attributes for name, author, and price. Includes methods for applying a discount and displaying book details.

```python
class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def show_info(self):
        print(f"Name: {self.name} \nAuthor: {self.author} \nPrice: ${self.price}")

    def discount(self, percent):
        self.price -= (self.price * percent / 100)
        print(f"New Price after {percent}% discount: ${self.price}")
```

#### Visual Representation:
```
+-----------------------+
|         Book         |
+-----------------------+
| - name: str          |
| - author: str        |
| - price: float       |
+-----------------------+
| + show_info()        |
| + discount(percent)  |
+-----------------------+
```

---

### Student Class

**Description:**
A `Student` class to manage student data including name, ID, and grades. Provides methods for adding grades, calculating averages, and displaying student information.

```python
class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades if grades else []

    def add_grades(self, grade):
        self.grades.append(grade)
        print(f"New Grade Added: {grade}")

    def calculate_average(self):
        if self.grades:
            average = sum(self.grades) / len(self.grades)
            return average
        else:
            return 0

    def show_info(self):
        average = self.calculate_average()
        print(f"{'Name':<10} :{self.name} \n{'Student ID':<10} :{self.student_id} \n{'Grades':<10} :{self.grades} \n{'Average':<10} :{average:.2f}")
```

#### Visual Representation:
```
+--------------------------+
|        Student          |
+--------------------------+
| - name: str             |
| - student_id: int       |
| - grades: list[float]   |
+--------------------------+
| + add_grades(grade)     |
| + calculate_average()   |
| + show_info()           |
+--------------------------+
```

---

## How to Run

1. Clone the repository:
   ```bash
   [git clone https://github.com/ozcotech/oop_lesson1.git](https://github.com/ozcotech/oop_lesson1.git)
   ```
2. Navigate to the project directory:
   ```bash
   cd oop-examples
   ```
3. Run any of the Python scripts to explore the examples:
   ```bash
   python car_example.py
   python telephone_example.py
   python book_example.py
   python student_example.py
   ```

## Contributions
Contributions are welcome! Feel free to submit a pull request or open an issue to enhance this repository.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
