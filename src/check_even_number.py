def check_if_even(number):
    """
    Example 2: Basic Arithmetic and Logic

    Mathematical opeartions(addition, multiplication, modula) on a fixed size
    integers are considered O(1). The CPU performs these in a fixed number
    of cycles regardless of what "number" is.
    """

    # Calculation and comparison take the same time regardless of the input size
    return number % 2 == 0




# Arithmetic is always O(1)
print(f"Is 500 even? {check_if_even(500)}")
print(f"Is 999,999,999 even? {check_if_even(999_999_999)}")
