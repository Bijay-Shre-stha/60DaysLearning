## **Inheritance**

- Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). 
- The class from which it inherits is called the base class (or parent class).
- The derived class inherits features from the base class, adding new features to it.
- This results in re-usability of code.
- Pass keyword is used to inherit the base class.
- __init __() method is used to initialize the base class members.
- super() function is used to call the base class constructor.
- Using method with super() function is called method overriding.

```python
class BaseClass:
    def __init__(self):
        self.name = "Base Class"
        print("Base Class Constructor")
    
    def baseMethod(self):
        print("Base Method")

class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()
        self.name = "Derived Class"
        print("Derived Class Constructor")

    def derivedMethod(self):
        print("Derived Method")

obj = DerivedClass()
obj.baseMethod()
obj.derivedMethod()
```

## **Polymorphism**

- Polymorphism refers to methods/functions/operators with the same name but different functionality.
- It allows us to define methods in the child class with the same name as defined in their parent class.
- It is used to perform different operations using a single entity.
- It is often used in Class methods, where we can have multiple classes with same method name.
- Looping over a list of objects and calling the same method on each one.
- ``__class__.__name__`` is used to get the class name of an object.

## **Encapsulation**

- Encapsulation is restricting access to some of an object's components.
- It is used to prevent the accidental modification of data.
- It is achieved by declaring the class variables as private (denoted by a single underscore prefix).
- Getter and Setter methods are used to access and modify the private variables.
- Getter methods are used to access the private variables.
- Setter methods are used to modify the private variables.
- ``._`` is used to access the private variables.
- ``.__`` is used to access the private methods.

```python
class Encapsulation:
    def __init__(self):
        self.__name = "Encapsulation"
        self.__age = 20

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age
```

## **Summary**

- Inheritance is a way of creating a new class for using details of an existing class without modifying it.
- Polymorphism refers to methods/functions/operators with the same name but different functionality.
- Encapsulation is restricting access to some of an object's components.
- It is used to prevent the accidental modification of data.
- Getter and Setter methods are used to access and modify the private variables.
