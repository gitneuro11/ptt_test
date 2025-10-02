"""Simple math utilities demonstrating addition and multiplication."""

def add(a: float, b: float) -> float:
    """Return the sum of ``a`` and ``b``."""
    return a + b


def multiply(a: float, b: float) -> float:
    """Return the product of ``a`` and ``b"""
    return a * b


if __name__ == "__main__":
    x, y = 3, 4
    print(f"add({x}, {y}) = {add(x, y)}")
    print(f"multiply({x}, {y}) = {multiply(x, y)}")
