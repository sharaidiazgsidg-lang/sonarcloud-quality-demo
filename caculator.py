"""
Módulo que proporciona operaciones matemáticas básicas a través de la clase Calculator.
"""

class Calculator:
    """
    Clase para realizar operaciones aritméticas básicas: suma, división y multiplicación.
    """

    def add(self, a: float, b: float) -> float:
        """
        Calcula la suma de dos números.
        """
        return a + b

    def divide(self, a: float, b: float) -> float:
        """
        Realiza la división de dos números con validación de seguridad.
        """
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        return a / b

    def multiply(self, a: float, b: float) -> float:
        """
        Calcula el producto de dos números de forma eficiente.
        """
        return a * b
