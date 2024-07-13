# Object-Oriented Design (OOD)

## Table of Contents


### 1. Thought Process
1. Identify key requirements and constraints
2. Break down the problem into key objects or entities involved. For each object, consider its attributes (properties) and behaviors (methods).
3. Define relationships.
   1. How objects interact with each other.
   2. Inheritance, composition, aggregation.
4. Define class structure.
   1. Design class hierarchy.
   2. Define each class with attributes and methods.
   3. Define access modifiers, `public`, `private`, `protected` properly.
5. Implement key methods.
    1. Ensure core functionalities.
   2. Consider edge cases.
6. Review and optimize.

### 2. Key Concepts and Keywords
1. **Encapsulation**: 
   - To bundle data (attributes) and methods (functions) that operate on the data into a **class**.
   - Restricts direct access to some components, preventing unintended interference and misuse.
   - Use private for attributes.
   - Create public getters and setters to access and modify private attributes.
```python
class Vehicle:
    def __init__(self, brand, year):
        self.__brand = brand
        self.__year = year

    def get_car_model(self):
        return self.__model

class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.__num_doors = num_doors
```
2. **Abstraction**:
    - Abstract away unnecessary details.
    - Focus on high-level functionalities.
    - Python achieves abstraction implicitly, or `abc` package, Java uses `abstract` keyword.
```python
from abc import ABC, abstractmethod
   
class Dog(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @abstractmethod
    def print_dog_info(self):
        pass

class Labradoodle(Dog):
    # subclass implements the abstract method
    def print_dog_info(self):
        print("Labradoodle is a mix of Labrador and Poodle.")
```
3. **Inheritance**:
   - One class can inherit attributes and methods from another class.
   - Promotes _code reusability_.
   - See example above.
4. **Polymorphism**:
   - Allows objects of different classes to be treated as objects of a common super class. 
   - Use **method overriding** and **method overloading** (same name, different parameters in terms of type and number).
   - This allows one interface to be used for a general class of actions.

```python
class Vehicle:
    def start_engine(self):
        print("Vehicle engine started.")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")
```

### Case Studies
