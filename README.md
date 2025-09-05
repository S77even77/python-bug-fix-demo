# Python Bug Fix Demo  

This repository demonstrates common Python bugs and how to fix them using clean coding practices.  
It is designed to showcase debugging, refactoring, and writing maintainable code.  

---

##  Motivation  

As a software engineer, debugging is one of the most valuable skills.  
This repo highlights how to identify common mistakes and improve code quality by showing buggy examples alongside their fixed versions.  

---

##  Example: Division by Zero  

**Buggy Code:**  
```python
def divide_buggy(a, b):
    return a / b


This will crash if b == 0.

Fixed Code:

def divide_safe(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
