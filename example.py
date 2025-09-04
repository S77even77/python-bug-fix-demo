"""
Example: Bug Fix Demo
This script demonstrates a common bug and the fixed version.
"""

# ❌ Buggy code
def divide_buggy(a, b):
    # This version crashes if b = 0
    return a / b

# ✅ Fixed code
def divide_safe(a, b):
    # Handles division by zero safely
    if b == 0:
        return "Error: Division by zero"
    return a / b


if __name__ == "__main__":
    print("=== Buggy version ===")
    try:
        print(divide_buggy(10, 0))
    except Exception as e:
        print("Crashed with error:", e)

    print("\n=== Fixed version ===")
    print(divide_safe(10, 0))   # Will now return a safe error message
    print(divide_safe(10, 2))   # Normal case works fine
