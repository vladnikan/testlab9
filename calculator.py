class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Деление на ноль запрещено!")
        return a / b

    @staticmethod
    def is_prime_number(n):
        """Возвращает True, если n — простое число"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True