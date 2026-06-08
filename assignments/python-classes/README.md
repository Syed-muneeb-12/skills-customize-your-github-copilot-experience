# 📘 Assignment: Python Classes

## 🎯 Objective

Learn how to define and use classes in Python to model real-world objects and behaviors, including attributes and methods for interaction.

## 📝 Tasks

### 🛠️	Define a Simple Class

#### Description
Create a `Car` class with basic attributes and a method to return the car's information.

#### Requirements
Completed program should:

- Define a class `Car` with `make`, `model`, and `year` attributes initialized in `__init__`.
- Implement a method `display_info()` that returns a string describing the car (do not print inside the method).
- Demonstrate creating an instance of `Car` and calling `display_info()` in example usage.

Example usage:

```python
car = Car('Toyota', 'Corolla', 2020)
print(car.display_info())
# Example output: Toyota Corolla (2020)
```

### 🛠️	Add Methods and Interactions

#### Description
Extend the `Car` class to track mileage and allow updates.

#### Requirements
Completed program should:

- Add a `mileage` attribute to `Car` with default value `0`.
- Implement `update_mileage(new_mileage)` that updates the mileage only if `new_mileage` is greater than the current mileage.
- Implement `display_mileage()` that returns the current mileage as an integer or formatted string.
- Demonstrate updating and displaying mileage in example usage.

Example usage:

```python
car.update_mileage(15000)
print(car.display_mileage())  # 15000
```
