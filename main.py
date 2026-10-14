from mylib.calc import (
    add,
    subtract,
    multiply,
    divide,
    power,
    square_root,
    absolute,
    is_even,
    is_odd,
)


def main():
    print("Add: ", add(2, 3))
    print("Subtract: ", subtract(5, 3))
    print("Multiply: ", multiply(3, 4))
    print("Divide: ", divide(10, 2))
    print("Power: ", power(2, 3))
    print("Square Root: ", square_root(16))
    print("Absolute: ", absolute(-5))
    print("Is Even: ", is_even(2))
    print("Is Odd: ", is_odd(3))


if __name__ == "__main__":
    main()
