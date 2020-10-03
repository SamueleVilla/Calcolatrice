# This is a brand new CALCULATOR powered by Python
# Dev --> Samuele Villa
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        return a / b
    except:
        print(" Ops I can't divide per zero :c , not yet")


print("Hi there!, Welcome to Python Calculator ")
try:
    first_number = input("Enter a number: ")
    operator = input("Enter the operator [+ | - | * | /]: ")
    second_number = input("Enter a number: ")

    print("---------------------------------------------")

    if operator == "+":
        result = add(float(first_number), float(second_number))
        print(first_number + " + " + second_number + " = " + str(result))

    elif operator == "-":
        result = sub(float(first_number), float(second_number))
        print(first_number + " - " + second_number + " = " + str(result))

    elif operator == "*":
        result = mul(float(first_number), float(second_number))
        print(first_number + " * " + second_number + " = " + str(result))

    elif operator == "/":
        result = div(float(first_number), float(second_number))

        if result is not None:
            print(first_number + " / " + second_number + " = " + str(result))

    else:
        print("The operator is wrong ...")

except:
    print("Ops! Something went wrong ...")

# The program has ended
