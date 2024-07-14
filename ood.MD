# Object-Oriented Design (OOD)

## Table of Contents
- [Thought Process](#thought-process)
- [Key Concepts and Keywords](#key-concepts-and-keywords)
- [Case Studies](#case-studies)
  - [Dog Daycare](#1-dog-daycare)
  - [Library and Books](#2-library-system)

### Thought Process
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

### Key Concepts and Keywords
1. **Encapsulation**: 
   - To bundle data (attributes) and methods (functions) that operate on the data into a **class**.
   - Restricts direct access to some components, preventing unintended interference and misuse.
   - Use private for attributes.
   - Initialize key attributes with `__init__`.
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

#### 1. Dog Daycare
- Requirements: 
  - dogs are of different sizes, only ones of similar sizes should play together. Only dogs with valid ID and vaccination records can be admitted.
- Key objects: `Dog`, `Playground`, `Daycare`
  - `Daycare` has multiple `Playground`s.
  - When a `Dog` is checked in, the vaccination status and ID must be checked.
- `Dog` class:
  - Attributes: `name` (string), `size` (float or int), `vaccinated`, `id_valid` (boolean)
  - Methods: (1) `__init__` to initialize attributes, (2) `is_allowed()` to check if the dog is allowed to play.

```python
class Dog:
    def __init__(self, name: str, size: str, vaccinated: bool, id_valid: bool):
        self.__name = name
        self.__size = size
        self.__vaccinated = vaccinated
        self.__id_valid = id_valid

    def is_allowed(self):
        return self.__vaccinated and self.__id_valid

    def get_size(self):
        return self.__size
```

- `Playground` class:
  - Attributes: `name` or `id`, `size_group` (either for small dogs, medium dogs, or large dogs), `dogs` list to store dogs in playground.
  - Methods: (1) `__init__` to initialize attributes, (2) `add_dog()` to add a dog to the playground. (3) `remove_dog()` to remove a dog from the playground. (4) `get_dogs()` to get all dogs in the playground.

```python
class Playground:
    def __init__(self, name, size_group):
        self.__name = name
        self.__size_group = size_group
        self.__dogs = [] # store dogs

    def add_dog(self, dog):
        self.__dogs.append(dog)

    def remove_dog(self, dog):
        self.__dogs.remove(dog)

    def get_dogs(self):
        for dog in self.__dogs:
            print(dog.name)
```

- `Daycare` class:
  - Attributes: `playgrounds` to store all playgrounds.
  - Methods: (1) `__init__` to initialize attributes, (2) `check_in()` to check in a dog, (3) `check_out()` to check out a dog, (4) `assign_playground` to assign a playground to a dog.

```python
class Daycare:
    def __init__(self, playgrounds):
        self.__playgrounds = {
            'small': Playground('small playground', 'small'),
            'large': Playground('large playground', 'large')
        }

    def check_in(self, dog):
        if dog.is_allowed():
            print('Check in successful.')
            self.assign_playgrounds(dog)
        else:
            print('Check in failed.')

    def check_out(self, dog):
        return

    def assign_playgrounds(self, dog):
        # Assign playground based on size
        dog_size = dog.get_size()
        if dog_size == 'small':
            self.__playgrounds['small'].add_dog(dog)
        elif dog_size == 'large':
            self.__playgrounds['large'].add_dog(dog)
        else:
            print(f"No playground available for dog of size {dog_size}.")
```

#### 2. Library System
- **Requirements**: design a library system that has features like rent a book, return a book, search for book (by name and by author).
- Key objects: `Book`, `Library`, `User`
- `Book` class: attributes include `name`, `author`, `available` (whether this book can still be rent)
```python
class Book:
    def __init__(self, name, author):
        self.__name = name
        self.__author = author
        self.available = True

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def rent_book(self):
        if not self.available:
            print("Book not available for renting.")
            return False
        self.available = False
        return True

    def return_book(self):
        self.available = True
```
- `User` class: `id` (id of user in system), `books` (books this person rented), `rent_book(book)` and `return_book(book)` to process rentals.
```python
class User: 
    def __init__(self, id):
        self.__id = id
        self.books = []

    def rent_book(self, book):
        if not book.rent_book:
            print('Rental not successful.')
            return False
        else:
            self.books.append(book)
            return True

    def return_book(self, book):
        if book in self.books:
            book.renturn_book()
            self.books.remove(book)
            return True
        print(f'User {self.__id} did not rent {book.get_name()}.')
        return False
```


- `Library` class: attributes include `books_by_name`, `books_by_author`
```python
class Library:
    def __init__(self):
        self.books_by_name = dict()
        self.books_by_author = dict()
        return 
    
    def add_book(self, book):
        self.books_by_name[book.get_name()] = book
        self.books_by_author[book.get_author()] = book
        return 
    
    def remove_book(self, book):
        if book.get_name() in self.books_by_name:
            self.books_by_name[book.get_name()].remove(book)
        if book.get_author() in self.books_by_author:
            self.books_by_author[book.get_author()].remove(book)
        return 

    def search_by_name(self, book_name):
        return self.books_by_name.get(book_name, [])

    def search_by_author(self, author_name):
        return self.books_by_author.get(author_name, [])

    def rent_book(self, user, book):
        if user.rent_book(book):
            print('Rental successful')
        else:
            print(f"Book {book.get_name()} not available.")
        return 

    def return_book(self, user, book):
        if user.return_book():
            print('Return successful.')
        else:
            print('Return failed.')
        return
```


