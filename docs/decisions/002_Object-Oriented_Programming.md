# decision 002: Motivation for using OOP

## 1. Overview

This project was developed using the **Object-Oriented Programming (OOP)** paradigm. Unlike structured programming, which focuses on functions and linear flow, OOP organizes software around "objects"—units that combine related data (attributes) and behaviors (methods).

## 2. Why did we choose OOP? (Justification)

The decision to use **OOP** was based on the following technical benefits for the project:

- **Modularity and Organization**: The code is structured into classes, which separates responsibilities. This facilitates the location and correction of errors, and also allows different parts of the system to be developed independently.
- **Code Reuse (Inheritance)**: Through inheritance and polymorphism, it was possible to reuse common logic, avoiding unnecessary repetition (DRY principle - Don't Repeat Yourself).
- **Encapsulation and Security**: The implementation details of an object are hidden from the rest of the system. This protects data against accidental manipulation and makes it easier to change the internal logic without breaking the rest of the application.
- **Abstraction and Real-World Modeling**: OOP allows you to model system entities in a more natural way (e.g., *User, Product, Order*), bringing the code closer to the business rules, making it more readable and intuitive.
- **Maintainability and Scalability**: Complex systems become easier to maintain and expand. Adding new features (new subclasses, for example) is less risky than altering lengthy procedural flows.

## 3. Practical Examples in the Project

- **Example 1**: The class *[Your Class Name]* encapsulates *[attributes]* and handles *[behaviors]*, ensuring that business rule Y is applied correctly.

- **Example 2**: We use inheritance to create the *[Subclass]* class from the *[Superclass]* class, reusing methods from *[functionality]*.

## Conclusion:

The use of **OOP** was fundamental in ensuring clean, organized, and sustainable code in the long term, facilitating collaboration and future updates.