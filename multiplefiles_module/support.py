def add_numbers(a, b):
    """
    Adds two numbers together.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b
class MathOperations:
    """
    A class to perform basic mathematical operations.
    """

    @staticmethod
    def multiply(a, b):
        """
        Multiplies two numbers together.

        Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

        Returns:
        int or float: The product of the two numbers.
        """
        return a * b

    @staticmethod
    def divide(a, b):
        """
        Divides one number by another.

        Parameters:
        a (int or float): The numerator.
        b (int or float): The denominator.

        Returns:
        float: The result of the division.

        Raises:
        ValueError: If the denominator is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b