import datetime

from utils import add, divide, multiply, subtract


print("Name: Mostofa Kamal Joy")
print("Date:", datetime.date.today())


if __name__ == "__main__":
    a = 10
    b = 5

    print(f"Addition: {a} + {b} = {add(a, b)}")
    print(f"Subtraction: {a} - {b} = {subtract(a, b)}")
    print(f"Multiplication: {a} * {b} = {multiply(a, b)}")

    try:
        print(f"Division: {a} / {b} = {divide(a, b)}")
    except ValueError as error:
        print(f"Division error: {error}")