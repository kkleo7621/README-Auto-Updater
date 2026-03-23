def factorial(n: int) -> int:
    """
    計算 n 的階乘。
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

class Calculator:
    """
    提供基礎數學運算的計算機類別。
    """
    def add(self, a, b):
        """
        將兩個數字相加。
        """
        return a + b
